import json
from decimal import Decimal
import requests
from flask import current_app


def get_supported_currencies():
    with open('app/api/currencies.json', 'r') as json_file:
        currencies = json.load(json_file)
        return currencies.keys()


def calculate_price(amount, rate):
    dec_amount = Decimal(amount)
    dec_rate = Decimal(rate)
    exchange_price = (dec_amount / dec_rate)
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
