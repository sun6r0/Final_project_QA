import configuration
import requests
import data


# Запрос на создание нового заказа
def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=order_body)


response = post_new_order(data.order_body)

# Создание переменной для трека
t = response.json()["track"]

# Запрос на заказ по номеру трека
def get_new_order_track():
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_TRACK,
                        params={"t": track})


response = get_new_order_track()
