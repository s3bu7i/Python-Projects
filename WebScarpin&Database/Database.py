import sqlite3

# Establish a connection to the database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price REAL
    )
''')

# Insert data into the table
products = [
    ('Product 1', 10.99),
    ('Product 2', 19.99),
    ('Product 3', 15.49)
]
cursor.executemany('INSERT INTO products (name, price) VALUES (?, ?)', products)

# Fetch data from the table
cursor.execute('SELECT * FROM products')
data = cursor.fetchall()
for row in data:
    print(row)

# Update a record
cursor.execute('UPDATE products SET price = 12.99 WHERE id = 1')

# Delete a record
cursor.execute('DELETE FROM products WHERE id = 2')

# Commit changes and close the connection
conn.commit()
conn.close()
