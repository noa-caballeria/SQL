import mysql.connector 

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "NoaLilly13600@",
    database = "LaPlateforme"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM etudiants")
result = cursor.fetchall()
print(result)

cursor.close()
conn.close()