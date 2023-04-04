import mysql.connector 

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "NoaLilly13600@",
    database = "LaPlateforme"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM employes WHERE salaire > 3000.00;")
result = cursor.fetchall()
print(result)

cursor.execute("SELECT employes.id, employes.nom, employes.prenom, employes.salaire, services.nom AS service FROM employes JOIN services ON employes.id_service = services.id")
for (id, nom, prenom, salaire, service) in cursor:
    print(f"{id} - {nom} {prenom} ({salaire} €) - {service}")

sql = "INSERT INTO employes (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
val = ("Maurte", "Adèle", 3200.00, 2)
cursor.execute(sql, val)
conn.commit()

sql = "DELETE FROM employes WHERE id = %s"
val = (5,)
cursor.execute(sql, val)
conn.commit()

sql = "SELECT * FROM employes"
cursor.execute(sql)
result = cursor.fetchall()
for record in result:
    print(record)


cursor.close()
conn.close()