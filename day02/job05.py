import mysql.connector 

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "NoaLilly13600@",
    database = "LaPlateforme"
)

cursor = conn.cursor()

cursor.execute("SELECT superficie FROM etage")
result = cursor.fetchall()
superficie = 0

for i in result:
    superficie += i[0]

print("La superficie de LaPlateforme est de ", superficie, "m²")

cursor.close()
conn.close()