from . import api
from flask import jsonify, request
from app.models import ExchangeData


@api.route('/', methods=['GET'])
def one():
    ex = ExchangeData.query.first()

    ret = {
        'id': ex.id,
        'currency': ex.currency,
        'rate': str(ex.rate),
        'price': str(ex.price),
        'created_at': ex.created_at
    }

    return jsonify(ret)


@api.route('/last', methods=['GET'])
def last():
    return 'yooo'


@api.route('/grab_and_save', methods=['POST'])
def grab_and_save():
    currency = request.form['currency']
    amount = request.form['amount']
    rate = request.form['rate']
    price = request.form['price']

    ex = ExchangeData(currency=currency, amount=amount, rate=rate, price=price)

    ex.save()
    return 'ok'
