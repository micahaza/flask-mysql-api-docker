
def test_demo(test_client):
    response = test_client.post('/grab_and_save', data=dict(amount=1))
    assert response.status_code == 200
