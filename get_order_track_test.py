import sender_stand_request


# Тест на проверку получения кода 200:
def test_get_order_by_track():
    response = sender_stand_request.get_new_order_track()
    assert response.status_code == 200
