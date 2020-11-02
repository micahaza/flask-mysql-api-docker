import json
from decimal import Decimal


def get_supported_currencies():
    with open('app/api/currencies.json', 'r') as json_file:
        currencies = json.load(json_file)
        return currencies.keys()


def calculate_price(amount, rate):
    dec_amount = Decimal(amount)
    dec_rate = Decimal(rate)
    exchange_price = (dec_amount / dec_rate)
    return dec_amount, dec_rate, exchange_price
