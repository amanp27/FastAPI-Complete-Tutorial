import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in the database:")
for table in tables:
    print(table[0])

if tables:
    table_name = tables[0][0]
    cursor.execute(f"SELECT * FROM {table_name};")
    rows = cursor.fetchall()
    print(f"Data in the '{table_name}' table:")
    for row in rows:
        print(row)

conn.close()