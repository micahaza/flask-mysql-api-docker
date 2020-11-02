from app.models import ExchangeData
from decimal import Decimal, ROUND_HALF_UP
import pytest


@pytest.mark.skip(reason="This still makes an external call.")
def test_post_grab_and_save(test_client):
    """
    How it could be fixed: If OpenExchange API call is extracted to it's own function
    then I'll be able to mock.patch that call.
    """
    request_data = {
        'currency': 'BTC',
        'amount': 0.42,
    }

    response = test_client.post('/grab_and_save', data=request_data)
    assert response.status_code == 201

    ex = ExchangeData.query.first()

    digits = '0.{}1'.format('0' * (7))
    digits = Decimal(digits)

    assert ex.currency == 'BTC'
    assert ex.amount == Decimal(0.42000000).quantize(digits, ROUND_HALF_UP)
    assert ex.rate == Decimal(0.00007304).quantize(digits, ROUND_HALF_UP)
    assert ex.price == Decimal(5750.66126785).quantize(digits, ROUND_HALF_UP)
