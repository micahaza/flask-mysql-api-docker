from flask import jsonify, current_app
from flask_restful import Resource, reqparse
from app.models import ExchangeData
from .validators import amount_validator, currency_validator
from .helpers import calculate_price
from .schemas import ExchangeDataSchema
import requests


class ExchangeDataResource(Resource):
    def post(self):
        request_parser = reqparse.RequestParser()
        request_parser.add_argument('amount', type=amount_validator, location='form', required=True)
        request_parser.add_argument('currency', type=currency_validator, location='form', required=True)

        args = request_parser.parse_args()
        currency = args.get('currency')
        amount = args.get('amount')

        params = {
            'app_id': current_app.config['OPENEXCHANGE_APP_ID'],
            'base': current_app.config['OPENEXCHANGE_BASE_CURRENCY'],
            'symbols': currency
        }

        try:
            resp = requests.get(current_app.config['OPENEXCHANGE_API_URL'], params=params)
            resp.raise_for_status()
        except Exception as e:
            response = jsonify({"message": str(e)})
            response.status_code = 400
            return response

        rates = resp.json()['rates']
        if currency not in rates:
            response = jsonify({"message": "Exchange rate not found"})
            response.status_code = 400
            return response

        dec_amount, dec_rate, dec_price = calculate_price(amount, rates[currency])

        exchange_data = ExchangeData(currency=currency, amount=dec_amount, price=dec_price, rate=dec_rate)
        exchange_data.save()

        sch = ExchangeDataSchema()
        response = jsonify(sch.dump(exchange_data))
        # response = jsonify(exchange_data)
        response.status_code = 201

        return response


class LastOperationsResouce(Resource):
    def get(self):
        ex = ExchangeData.query.first()

        ret = {
            'id': ex.id,
            'currency': ex.currency,
            'rate': str(ex.rate),
            'price': str(ex.price),
            'created_at': ex.created_at
        }

        return jsonify(ret)
