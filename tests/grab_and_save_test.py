from app.models import ExchangeData


def test_demo(test_client):
    data = {
        'currency': 'HUF',
        'amount': 3600,
        'rate': 260,
        'price': 311
    }

    response = test_client.post('/grab_and_save', data=data)
    assert response.status_code == 200

    ex = ExchangeData.query.first()
    assert ex.currency == 'HUF'
    assert ex.amount == 3600
    assert ex.rate == 260
    assert ex.price == 311
