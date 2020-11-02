from .helpers import get_supported_currencies


def currency_validator(value):
    if value.upper() not in get_supported_currencies():
        raise ValueError('Currency is not supported')
    return value


def amount_validator(value):
    if float(value) <= 0:
        raise ValueError('Value must be greater than zero')
    return value
