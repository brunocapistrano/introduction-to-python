import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres", 
    user="postgres", 
    password="admin"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM produto;")

rows = cursor.fetchall()

print(rows)

# for row in rows:
#     print(row)

conn.close()