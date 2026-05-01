import mysql
import mysql.connector as s
ql 

db = sql.connect(
    host = "localhost",
    user = "root",
    password = "armaan123",
    use_pure = True
)

cr = db.cursor()
cr.execute("show databases")
for i in cr :
    print(i)
    