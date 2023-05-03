import pymysql.cursors
from base64 import b64encode as enc64
from base64 import b64decode as dec64

con = pymysql.connect(host='localhost',
                      user='root',
                      password='Akatzuki666$',
                      database='myasolubi',
                      charset='utf8mb4',
                      cursorclass=pymysql.cursors.DictCursor)




def binary_pict(pict):
    with open(pict, 'rb') as f:
        binary = f.read()
        print(binary)
        return binary
        # with con:
        #     with con.cursor() as cursor:
        #         sql = f'INSERT INTO items (itemName, itemCost, typeOfItem, itemImage) values ("Стейк Топ-блейд 500 ' \
        #               f'г",700 ,"говядина", \{binary_pict(pict)}\ ));'
        #         print(sql)
        #         cursor.execute(sql, ('Стейк Топ-блейд 500 г', 700, 'говядина', binary_pict(pict)))
        #     con.commit()


pict = 'C:/Users/Имя/Pictures/Диплом/stake_part_o_m2.jpg'
# binary_pict(pict)

with con:
    with con.cursor() as cursor:
        itemName = "Стейк Рибай из мраморной говядины 400 г"
        typeOfItem = "говядина"
        itemCost = 2490
        itemImage = binary_pict(pict)
        print(itemImage)
        # sql = 'INSERT INTO items (itemName, itemCost, typeOfItem, itemImage) values (%s, %s, &s, %s));'
        # sql = f'INSERT INTO items (itemName, itemCost, typeOfItem, itemImage) VALUES (\"{itemName}\", {itemCost}, \"{typeOfItem}\", {itemImage})'
        sql = """INSERT INTO items (itemName, itemCost, typeOfItem, itemImage) VALUES (%s, %s, %s, %s)"""
        print(sql)
        insert_blob_tuple = (itemName, itemCost, typeOfItem, itemImage)
        result = cursor.execute(sql, insert_blob_tuple)
        con.commit()

        # cursor.execute(sql, ('Стейк Топ-блейд 500 г', 700, 'говядина', binary_pict(pict)))
