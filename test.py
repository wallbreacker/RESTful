import pymysql.cursors
from PIL import Image
import base64
import os
con = pymysql.connect(host='localhost',
                      user='root',
                      password='Akatzuki666$',
                      database='myasolubi',
                      charset='utf8mb4',
                      cursorclass=pymysql.cursors.DictCursor)

# with con:
#     with con.cursor() as cursor:
#         cursor.execute('''SELECT * FROM items''')
#         items_db = cursor.fetchall()
#         print(items_db)
#         image_db = base64.b64encode(items_db[0]['itemImage'])
#         image_db_new = base64.b64decode(image_db)
#         with open('image_db_new.jpg', mode='wb') as f:
#             f.write(image_db_new)

# myImage = Image.open("C:/Users/Имя/Pictures/Диплом/top_blade_c1.jpg")
# print(myImage)
# myImage.load()
# os.mkdir(images)
# with open('C:/Users/Имя/Pictures/Диплом/top_blade_c1.jpg') as f:
#     f.(images)

# dict_list = []
# for i in items_db:
# for j,v in i.items():
#     print(f'{j}:{v}')
#     for j in i:
#         print(f'{j}:{i[j]}')
# print(i)
# print(i['itemName'])
# i['itemImage'] = base64.b64encode(i['itemImage']).decode('utf-8')
# print(i['itemImage'])
# dict_list.append(i)

# print(dict_list)
