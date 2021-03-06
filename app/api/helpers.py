import json
import decimal
import requests
from flask import current_app


def get_supported_currencies():
    with open('app/api/currencies.json', 'r') as json_file:
        currencies = json.load(json_file)
        return currencies.keys()


def calculate_price(amount, rate):
    my_context = decimal.Context(rounding=decimal.ROUND_HALF_UP)
    cents = decimal.Decimal('0.00000000')
    dec_amount = my_context.create_decimal(amount)
    dec_rate = my_context.create_decimal(rate)

    exchange_price = (dec_amount / dec_rate).quantize(cents, my_context)

    return dec_amount, dec_rate, exchange_price


def get_price_info(currency):
    params = {
        'app_id': current_app.config['OPENEXCHANGE_APP_ID'],
        'base': current_app.config['OPENEXCHANGE_BASE_CURRENCY'],
        'symbols': currency
    }

    resp = requests.get(current_app.config['OPENEXCHANGE_API_URL'], params=params)
    rates = resp.json()['rates']

    return rates


class NotSupportedCurrecyException(Exception):
    pass
