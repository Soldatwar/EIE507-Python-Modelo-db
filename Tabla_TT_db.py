#Tabla temperatura tortuga db
import psycopg2
import time
import random

#Conéctate a tu base de datos PostgreSQL
connection = psycopg2.connect(
    user="postgres",
    password="123456",
    host="192.168.0.16",
    port="5432",
    database="postgres"
)
cursor = connection.cursor()

cursor.execute("""
    SELECT EXISTS (
        SELECT FROM information_schema.tables
        WHERE  table_name   = 'mi_tabla'
    )
""")
exists = cursor.fetchone()[0]
if not exists:
    cursor.execute("""
        CREATE TABLE mi_tabla (
            temperatura FLOAT
        )
    """)

while True:
    # Genera un número aleatorio entre 25 y 35
    temperatura = random.uniform(25, 35)

    # Inserta la temperatura en tu base de datos
    cursor.execute("INSERT INTO mi_tabla (temperatura) VALUES (%s)", (temperatura,))
    connection.commit()

    time.sleep(5)
