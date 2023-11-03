#Tabla camara tortuga db
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
        WHERE  table_name   = 'camara'
    )
""")
exists = cursor.fetchone()[0]
if not exists:
    cursor.execute("""
        CREATE TABLE camara (
            url TEXT,
            tiempo TIMESTAMP,
            temperatura FLOAT
        )
    """)

url_imagen = 'https://cdn.discordapp.com/attachments/1166612482253668373/1169800024444637254/WhatsApp_Image_2023-11-02_>while True:
    # Genera un número aleatorio entre 25 y 35
    temperatura = random.uniform(25, 35)

    # Guarda la URL de la imagen y la temperatura en tu base de datos
    cursor.execute("INSERT INTO camara (url, tiempo, temperatura) VALUES (%s, NOW(), %s)", (url_imagen, temperatura))
    connection.commit()

    time.sleep(60)
