from app.models import ExchangeData
from decimal import Decimal, ROUND_HALF_UP


def test_with_no_arguments(test_client):
    exchange_data = ExchangeData(currency='BTC', amount='0.744', price='8632.34', rate=1.34)
    exchange_data.save()

    response = test_client.get('/last')
    assert response.status_code == 200

    json_data = response.get_json()
    assert len(json_data) == 1

    json_data = json_data[0]

    digits = Decimal('0.{}1'.format('0' * (7)))

    assert json_data['currency'] == 'BTC'
    assert json_data['amount'] == str(Decimal(0.744).quantize(digits, ROUND_HALF_UP))
    assert json_data['price'] == str(Decimal(8632.34).quantize(digits, ROUND_HALF_UP))
    assert json_data['rate'] == str(Decimal(1.34).quantize(digits, ROUND_HALF_UP))


def test_with_num_records(test_client):
    ExchangeData(currency='HUF', amount='0.744', price='8632.34', rate=1.34).save()
    ExchangeData(currency='EUR', amount='0.2', price='8633.34', rate=1.34).save()
    ExchangeData(currency='BTC', amount='0.734', price='8630.34', rate=1.34).save()
    ExchangeData(currency='HUF', amount='0.734', price='8630.34', rate=1.34).save()

    response = test_client.get('/last?num_records=1')
    assert response.status_code == 200
    json_data = response.get_json()
    assert len(json_data) == 1

    response = test_client.get('/last?num_records=2')
    assert response.status_code == 200
    json_data = response.get_json()
    assert len(json_data) == 2

    response = test_client.get('/last?num_records=3')
    assert response.status_code == 200
    json_data = response.get_json()
    assert len(json_data) == 3

    response = test_client.get('/last?num_records=4')
    assert response.status_code == 200
    json_data = response.get_json()
    assert len(json_data) == 4

    response = test_client.get('/last?num_records=50')
    assert response.status_code == 200

    json_data = response.get_json()
    assert len(json_data) == 5


def test_with_currency(test_client):
    response = test_client.get('/last?currency=BTC')
    assert response.status_code == 200
    json_data = response.get_json()
    assert len(json_data) == 2

    response = test_client.get('/last?currency=HUF')
    assert response.status_code == 200
    json_data = response.get_json()
    assert len(json_data) == 2

    response = test_client.get('/last?currency=eur')
    assert response.status_code == 200
    json_data = response.get_json()
    assert len(json_data) == 1


def test_with_currency_and_num_records(test_client):
    response = test_client.get('/last?currency=BTC&num_records=1')
    assert response.status_code == 200
    json_data = response.get_json()
    assert len(json_data) == 1

    response = test_client.get('/last?currency=BTC&num_records=2')
    assert response.status_code == 200
    json_data = response.get_json()
    assert len(json_data) == 2

    response = test_client.get('/last?currency=BTC&num_records=1322')
    assert response.status_code == 200
    json_data = response.get_json()
    assert len(json_data) == 2
