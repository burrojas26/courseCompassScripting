import mysql.connector

mydb = mysql.connector.connect(
    host = '10.78.64.121',
    user = "navigator",
    password = "P@$$w0rd",
    database="7hills",
)

cursor = mydb.cursor()

cursor.execute('''SELECT * FROM CourseInfo''')
result = cursor.fetchall()
for i in result:
    print(i)
