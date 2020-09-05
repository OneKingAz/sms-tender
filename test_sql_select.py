
import mysql.connector

mydb = mysql.connector.connect(
  host="aff.f.d.d",
  user="asda",
  password="asd",
  database="asd"
)

mycursor = mydb.cursor()
def check_cookie(cookie,username,ip):
     cookie = str("'" + cookie + "'")
     username = str("'" + username + "'")
     ip = str("'" + ip + "'")
     sql = ("SELECT * FROM cookie WHERE cookie = {} and name = {} and ip = {}").format(cookie,username,ip)
     mycursor = mydb.cursor()
     mycursor.execute(sql)
     myresult = mycursor.fetchone()
     mycursor.close()
     if myresult is None:
         return False    
     else:
         return True

# #     user_account_password = (myresult[0])
# #     if user_account_password != password:
# #         return False
# #     elif user_account_password == password:
# #         return True
     
cookie = "ee895dad-eb42-4856-8e6d-8573e5fc18f5"
name = "oneking"
ip = "146.120.213.135"

print(check_cookie(cookie,name,ip))

# sql = ('SELECT * FROM cookie WHERE cookie = "ee895dad-eb42-4856-8e6d-8573e5fc18f5" and name = "oneking" and ip = "146.120.213.135"')
# mycursor.execute(sql)
# myresult = mycursor.fetchone()
# for x in myresult:
#     print(x)
#     
# mycursor.close()