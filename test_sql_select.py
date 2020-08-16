
import mysql.connector

mydb = mysql.connector.connect(
  host="176.126.165.135",
  user="user8745_login",
  password="W1ww6y2c",
  database="user8745_login"
)

mycursor = mydb.cursor()

def sql_select(colown, inn):
    sql = ("SELECT {} FROM blacklist WHERE inn = %s ").format(colown)
    inn = str(inn)
    value = tuple([inn])
    mycursor.execute(sql, value)
    myresult = mycursor.fetchall()
    result = []
    for x in myresult:
    
        result.append(x)
    result = tuple([result])
    
    return result
value = ("1234567890")  


print(sql_select("personname", value))