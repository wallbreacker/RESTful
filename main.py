from flask import Flask, request, jsonify, send_from_directory
from flask_restful import Api
from flask_mysqldb import MySQL
import logging
import base64
import json
import os

app = Flask(__name__)
api = Api(app)
logging.basicConfig(level=logging.DEBUG)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Akatzuki666$'
app.config['MYSQL_DB'] = 'myasolubi'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)


# Запрос на одного user из таблицы users

@app.route('/users', methods=['POST'])
def login():
    data = request.json
    cur = mysql.connection.cursor()
    nickname = data.get('nickname')
    password = data.get('password')
    cur.execute('''SELECT * FROM users WHERE nickname=%s AND password=%s''',
                (nickname, password))
    users = cur.fetchone()
    app.logger.info(f'username: {data.get("nickname")} '
                    f'password: {data.get("password")}')
    return users


# Запрос на внесение одного user в таблицу users


# @app.route('/users/reg', methods=['POST'])
# def registration():
#     data = request.json
#     cur = mysql.connection.cursor()
#     nickname = data.get('nickname')
#     firstname = data.get('firstname')
#     password = data.get('password')
#     phonenumber = data.get('phonenumber')
#     email = data.get('email')
#     address = data.get('address')
#     cur.execute('''INSERT INTO users (nickname,firstname,
#                  password, phonenumber, email, address) VALUES (%s, %s, %s, %s, %s, %s)''',
#                 (nickname, firstname, password, phonenumber, email, address))
#     mysql.connection.commit()
#     cur.close()
#     return 200


# @app.route('/users/reg', methods=['POST'])
# def registration():
#     data = request.json
#     cur = mysql.connection.cursor()
#     nickname = data.get('nickname')
#     cur.execute('''INSERT INTO users (nickname) VALUES (%s)''', nickname)
#     mysql.connection.commit()
#     cur.close()
#     return 200


# Запрос на проверку юзера при регистрации
@app.route('/users/check', methods=['POST'])
def check_user():
    data = request.json
    app.logger.info(f'data:{data}')
    cur = mysql.connection.cursor()
    nickname = data.get('nickname')
    app.logger.info(f'nickname:{nickname}')
    sql = f'INSERT INTO users (nickname) VALUES (\"{nickname}\")'
    # sql = f'SELECT * FROM users WHERE nickname=\"{nickname}\"'
    cur.execute(sql)
    # cur.execute('''SELECT * FROM users WHERE nickname=%s''', nickname)
    # users = cur.fetchone()
    mysql.connection.commit()
    cur.close()
    # app.logger.info(f'users:{users}')
    resp = jsonify(success=True)
    return resp
    # return users


# Запрос на внесение личных данных нового юзера при регистрации
@app.route('/users/reg/all', methods=['POST'])
def registration_all():
    data = request.json
    app.logger.info(f'data:{data}')
    cur = mysql.connection.cursor()
    nickname = data.get('nickname')
    app.logger.info(f'nickname:{nickname}')
    firstname = data.get('firstname')
    app.logger.info(f'firstname:{firstname}')
    password = data.get('password')
    app.logger.info(f'password:{password}')
    phonenumber = data.get('phonenumber')
    app.logger.info(f'phonenumber:{phonenumber}')
    email = data.get('email')
    app.logger.info(f'email:{email}')
    address = data.get('address')
    app.logger.info(f'address:{address}')
    # cur.execute('''INSERT INTO users (nickname,firstname, password, phonenumber, email, address) VALUES (%s, %s, %s,
    # %s, %s, %s)''', (nickname, firstname, password, phonenumber, email, address))
    sql = f'UPDATE users SET firstname=\"{firstname}\", password=\"{password}\", phonenumber=\"{phonenumber}\", email=\"{email}\", address=\"{address}\" WHERE nickname=\"{nickname}\"'
    app.logger.info(f'sql:{sql}')
    cur.execute(sql)
    # cur.execute('''UPDATE users SET firstname=%s, password=%s, phonenumber=%s, email=%s,
    #                 address=%s WHERE nickname=%s''',
    #             (firstname, password, phonenumber, email, address, nickname))
    mysql.connection.commit()
    cur.close()
    return jsonify(success=True)


# Запрос на получение всех товаров из таблицы items

@app.route('/items/all', methods=['GET'])
def items():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM items''')
    items_db = cur.fetchall()
    return jsonify(items_db)
    # app.logger.info(f'items:{items}')
    # list_items = []
    # for i in items_db:
    #     i['itemImage'] = base64.b64encode(i['itemImage']).decode('utf-8')
    #     app.logger.info(f":{i['itemImage']}")
    #     list_items.append(i)
    # return json.dumps(list_items)


@app.route('/items/image/<itemImage>', methods=['GET'])
def items_image(itemImage):
    directory = 'C:/Users/Имя/PycharmProjects/pythonProject/images'
    return send_from_directory(directory, itemImage)

    # return jsonify(items)
    # result = []
    # app.logger.info(f'result:{result}')
    # for item in items:
    #     item_dict = {
    #         "itemId": item[0],
    #         "itemName": item[1],
    #         "itemCost": item[2],
    #         "typeOfItem": item[3],
    #         "itemImage": item[4]
    #     }
    #     app.logger.info(f'item_dict:{item_dict}')
    #     # Получить данные картинки в виде байтов
    #     image_data = item_dict['itemImage']
    #     app.logger.info(f'image_data:{image_data}')
    #     # Преобразовать данные картинки в base64
    #     encoded_image = base64.b64encode(image_data).decode('utf-8')
    #     app.logger.info(f'encoded_image:{encoded_image}')
    #     # dict_list = dict(items)
    #     # app.logger.info(f'item_list:{dict_list}')
    #     # dict_list[4] = encoded_image
    #     # app.logger.info(f'item_list:{dict_list}')
    #     return jsonify(item_dict)
    # #     # result.append(items)

    # Отправить результат на клиентское приложение
    # return jsonify(result)
    # return jsonify(items)


# Запрос на один item из таблицы items


@app.route('/items/one', methods=['POST'])
def take_item():
    data = request.json
    cur = mysql.connection.cursor()
    itemId = data.get('itemId')
    cur.execute('''SELECT * FROM items WHERE itemId=%s''', (itemId,))
    item = cur.fetchone()
    return item


# Запрос на внесение заказа в таблицу orders

@app.route('/order', methods=['POST'])
def ordering():
    data = request.json
    app.logger.info(f'data:{data}')
    cur = mysql.connection.cursor()
    orderId = data.get('orderId')
    nickname = data.get('nickname')
    orderStatus = data.get('orderStatus')
    cur.execute('''INSERT INTO orders (orderId, nickname,
                  orderStatus) VALUES (%s, %s, %s)''',
                (orderId, nickname, orderStatus))
    mysql.connection.commit()
    cur.close()
    return jsonify()


# Запрос на внесение позиции заказа в таблицу cart

@app.route('/cart', methods=['POST'])
def carting():
    data = request.json
    cur = mysql.connection.cursor()
    orderId = data.get('orderId')
    itemId = data.get('itemId')
    numberOfItem = data.get('numberOfItem')
    cur.execute('''INSERT INTO cart (orderId, itemId,
                 numberOfItem) VALUES (%s, %s, %s)''',
                (orderId, itemId, numberOfItem))
    mysql.connection.commit()
    cur.close()
    return 200


# Запрос на получение информации о позициях оплаченного заказа из таблицы cart

@app.route('/cart/items', methods=['POST'])
def cart_change():
    data = request.json
    cur = mysql.connection.cursor()
    orderId = data.get('orderId')
    cur.execute('''SELECT * FROM cart WHERE orderId=%s''', (orderId,))
    userItem = cur.fetchall()
    return jsonify(userItem)


# Запрос на изменение количества товара в корзине

# @app.route('/cart/items/change', methods=['POST'])
# def cart_update():
#     data = request.json
#     cur = mysql.connection.cursor()
#     orderId = data.get('orderId')
#     itemId = data.get('itemId')
#     numberOfItem = data.get('numberOfItem')
#     cur.execute('''UPDATE cart SET numberOfItem = %s WHERE orderId = %s AND itemId = %s''',
#                 (numberOfItem, orderId, itemId,))
#     userItem = cur.fetchone()
#     return jsonify(userItem)


# Запрос на удаление товара из корзины

# @app.route('/cart/items/delete', methods=['POST'])
# def cart_delete():
#     data = request.json
#     cur = mysql.connection.cursor()
#     orderId = data.get('orderId')
#     itemId = data.get('itemId')
#     cur.execute('''DELETE FROM cart WHERE orderId = "%s" AND itemId = %s''',
#                 (orderId, itemId,))
#     mysql.connection.commit()
#     cur.close()
#     return 200


# @app.route('/cart/items/delete', methods=['POST'])
# def cart_delete():
#     data = request.json
#     app.logger.info(f'data: {data}')
#     cur = mysql.connection.cursor()
#     orderId = data.get('orderId')
#     app.logger.info(f'orderId: {orderId}')
#     itemId = data.get('itemId')
#     app.logger.info(f'itemId: {itemId}')
#     sql = f'DELETE FROM cart WHERE orderId=\"{orderId}\" AND itemId={itemId}'
#     app.logger.info(f'sql: {sql}')
#     cur.execute(sql)
#     mysql.connection.commit()
#     cur.close()
#     return "Done"


# Запрос на удаление всех товаров из корзины
# @app.route('/cart/items/delete/all', methods=['POST'])
# def cart_delete_all():
#     data = request.json
#     cur = mysql.connection.cursor()
#     orderId = data.get('orderId')
#     cur.execute('''DELETE FROM cart WHERE orderId="%s"''', (orderId, ))
#     mysql.connection.commit()
#     cur.close()
#     return 200


@app.route('/cart/all', methods=['GET'])
def cart_all_items():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM cart''')
    items = cur.fetchall()
    return jsonify(items)


# @app.route('/orders/all', methods=['GET'])
# def orders_all_items():
#     cur = mysql.connection.cursor()
#     sql = f'SELECT * FROM orders'
#     # cur.execute('''SELECT * FROM cart''')
#     cur.execute(sql)
#     app.logger.info(f'sql: {sql}')
#     items = cur.fetchall()
#     app.logger.info(f'items: {items}')
#     return jsonify(items)

@app.route('/item/insert', methods=['POST'])
def item_insert():
    data = request.json
    cur = mysql.connection.cursor()
    orderId = data.get('orderId')
    itemId = data.get('itemId')
    numberOfItem = data.get('numberOfItem')
    cur.execute('''INSERT INTO cart (orderId, itemId,
                 numberOfItem) VALUES (%s, %s, %s)''',
                (orderId, itemId, numberOfItem))
    mysql.connection.commit()
    cur.close()
    return 200


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
