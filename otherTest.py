import sqlite3

# Connect to the database (creates it if it doesn't exist)
conn = sqlite3.connect('test.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table (optional)
cursor.execute('UPDATE users SET name="Ethan", password="Avera" WHERE id=0')
conn.commit()
cursor.execute('SELECT name FROM users')
rows = cursor.fetchall()
for row in rows:
    print(row[0]);

# Close the connection
conn.close()