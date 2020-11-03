from flask import jsonify
from flask_restful import Resource, reqparse
from app.models import ExchangeData
from .validators import amount_validator, currency_validator
from .helpers import calculate_price, get_price_info, NotSupportedCurrecyException
from .schemas import ExchangeDataSchema
from requests.exceptions import ConnectionError, ConnectTimeout


class ExchangeDataResource(Resource):
    def post(self):
        request_parser = reqparse.RequestParser()
        request_parser.add_argument('amount', type=amount_validator, location='form', required=True)
        request_parser.add_argument('currency', type=currency_validator, location='form', required=True)

        args = request_parser.parse_args()
        currency = args.get('currency')
        amount = args.get('amount')

        try:
            rates = get_price_info(currency)
        except (ConnectionError, ConnectTimeout) as e:
            response = jsonify({'error': str(e)})
            response.status_code = 400
            return response

        try:
            rate = rates[currency]
        except NotSupportedCurrecyException:
            response = jsonify({'error': "Exchange rate not found"})
            response.status_code = 400
            return response

        dec_amount, dec_rate, dec_price = calculate_price(amount, rate)

        exchange_data = ExchangeData(currency=currency, amount=dec_amount, price=dec_price, rate=dec_rate)
        exchange_data.save()

        sch = ExchangeDataSchema()
        response = jsonify(sch.dump(exchange_data))
        response.status_code = 201

        return response


class LastOperationsResouce(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('num_records', type=amount_validator, location='args', required=False)
        parser.add_argument('currency', type=currency_validator, location='args', required=False)

        args = parser.parse_args()
        currency = args.get('currency', "")
        num_records = args.get('num_records', None)
        num_records = num_records
        if not num_records and not currency:
            num_records = 1

        queryset = ExchangeData.query

        if currency:
            queryset = queryset.filter_by(currency=currency)

        queryset = queryset.order_by(ExchangeData.id.desc())

        if num_records:
            queryset = queryset.limit(num_records)

        sch = ExchangeDataSchema()
        response = jsonify([sch.dump(i) for i in queryset])
        response.status_code = 200

        return response
