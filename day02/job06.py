import mysql.connector 

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "NoaLilly13600@",
    database = "LaPlateforme"
)

cursor = conn.cursor()

cursor.execute("SELECT capacite FROM salles")
result = cursor.fetchall()
capacite = 0

for i in result:
    capacite += i[0]

print("La capacité de toutes les salles est de :", capacite)

cursor.close()
conn.close()