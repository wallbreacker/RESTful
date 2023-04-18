from flask import Flask, request, jsonify
from flask_restful import Api
from  flask_mysqldb import MySQL
import logging

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

@app.route('/users/', methods=['POST'])
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


@app.route('/users/reg', methods=['POST'])
def registration():
    data = request.json
    cur = mysql.connection.cursor()
    nickname = data.get('nickname')
    firstname = data.get('firstname')
    password = data.get('password')
    phonenumber = data.get('phonenumber')
    email = data.get('email')
    address = data.get('address')
    cur.execute('''INSERT INTO users (nickname,firstname,
                 passwemail, address) VALUES (%s, %s, %s, %s, %s, %s)''',
                (nickname, firstname, password, phonenumber, email, address))
    mysql.connection.commit()
    cur.close()
    return "Done"


# Запрос на получение всех товаров из таблицы cart

@app.route('/items/all', methods=['GET'])
def items():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM items''')
    items = cur.fetchall()
    app.logger.info(f'items: {items}')
    app.logger.info(f'items: {type(items)}')
    return jsonify(items)

# Запрос на один item из таблицы items


@app.route('/items', methods=['POST'])
def take_item():
    data = request.json
    cur = mysql.connection.cursor()
    itemId = data.get('itemId')
    cur.execute('''SELECT * FROM items WHERE itemId=%s''', (itemId,))
    item = cur.fetchone()
    app.logger.info(f'item: {data.get("itemId")}')
    return item

# Запрос на внесение заказа в таблицу orders


@app.route('/order', methods=['POST'])
def ordering():
    data = request.json
    cur = mysql.connection.cursor()
    orderId = data.get('orderId')
    nickname = data.get('nickname')
    orderStatus = data.get('orderStatus')
    cur.execute('''INSERT INTO orders (orderId, nickname,
                  orderStatus) VALUES (%s, %s, %s)''',
                (orderId, nickname, orderStatus))
    mysql.connection.commit()
    cur.close()
    return "Done"


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
    return "Done"


# Запрос на получение информации о позициях оплаченного заказа из таблицы cart

@app.route('/cartItems', methods=['POST'])
def items_cart():
    data = request.json
    cur = mysql.connection.cursor()
    orderId = data.get('orderId')
    cur.execute('''SELECT * FROM cart WHERE orderId=%s''', (orderId, ))
    userItem = cur.fetchall()
    return jsonify(userItem)


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
