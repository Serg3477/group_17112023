from pprint import pprint
import requests
url_carts = "https://dummyjson.com/carts"
response = requests.get(url = url_carts)
data_from_net = response.json()
id_carts = data_from_net['carts']
for key in id_carts:
    if (key['userId'] == 56 ):
        print("Кошик користувача з Id:56\n" + ("*" * 50))
        pprint(key['products'])
        print("*" * 50)
        user_products = key['products']
        for product in user_products:
            if product['discountPercentage'] >= 15:
                print("*" * 50)
                print("Назва продукту: " + str(product['title']))
                print("Зі знижкою: " + str(product['discountPercentage']))

