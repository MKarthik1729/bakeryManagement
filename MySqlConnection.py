import mysql.connector
from mysql.connector import errorcode
# jdbc:mysql://localhost:3306/?user=root
try:
    cnx = mysql.connector.connect(user='root', password='1234',host='localhost',database='bakery_management')
    if cnx.is_connected():
        cursor = cnx.cursor()
        # if True:
        print("Connected Successfully !!!!")

except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)

# # cnx.close()

# # import datetime
# # import mysql.connector



# query = ("select * from users;")
# cursor = cnx.cursor()
# cursor.execute(query)

# # print(cursor)

# k = cursor.fetchall()
# for username in k:
#     print(username)

# cursor.close()
# cnx.close()