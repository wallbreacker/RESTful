import requests
import json

# Запрос на все данные из таблицы users

# res = requests.get('http://192.168.0.131:5000/users')

# Запрос на одного user из таблицы users

res = requests.post('http://192.168.1.139:5000/users', headers={'Content-type': 'application/json'},
                    data=json.dumps({'nickname': 'afr123', 'password': 'qwerty'},))

# Запрос на внесение одного user в таблицу users

# res = requests.post('http://192.168.0.131:5000/users/reg', headers={'Content-type': 'application/json'},
#                     data=json.dumps({'nickname': 'kdjfkshvf', 'firstname': 'kjvjsnv', 'password': 'kbm;bm',
#                                      'phonenumber': '96796587',
#                                      'email': ';oedmvmwv', 'address': 'mbenbpmbp'},))

# Запрос на все товары из таблицы items

# res = requests.get('http://192.168.0.131:5000//items/all')

# Запрос на один item из таблицы items

# res = requests.post('http://192.168.0.131:5000/items', headers={'Content-type': 'application/json'},
#                     data=json.dumps({'itemId': '1'},))

# Запрос на внесение заказа в таблицу orders

# res = requests.post('http://192.168.0.131:5000/order', headers={'Content-type': 'application/json'},
#                     # data=json.dumps({'orderId': '26032023142900', 'orderStatus': 1},))
#                     data=json.dumps({'orderId': '26032023142900', 'nickname': 'afr123', 'orderStatus': 1},))

# Запрос на внесение позиции заказа в таблицу cart

# res = requests.post('http://192.168.0.131:5000/cart', headers={'Content-type': 'application/json'},
#                     data=json.dumps({'orderId': '26032023142900', 'itemId': 1, 'numberOfItem': 15},))

# Запрос на получение информации о позициях оплаченного заказа из таблицы cart

# res = requests.post('http://192.168.0.131:5000//cartItems', headers={'Content-type': 'application/json'},
#                     data=json.dumps({'orderId': '26032023142900'},))

print(res.json())
