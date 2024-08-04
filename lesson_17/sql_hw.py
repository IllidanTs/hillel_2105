import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        price REAL NOT NULL,
        category_id INTEGER,
        FOREIGN KEY (category_id) REFERENCES categories(id)
    )
''')

categories_data = [
    ('Electronics',),
    ('Books',),
    ('Clothing',)
]
cursor.executemany('INSERT INTO categories (name) VALUES (?)', categories_data)

products_data = [
    ('Smartphone', 'Latest model smartphone with 128GB storage', 699.99, 1),
    ('Laptop', 'High performance laptop for work and gaming', 1199.99, 1),
    ('Python Programming Book', 'Comprehensive guide to Python programming', 39.99, 2),
    ('T-shirt', 'Comfortable cotton t-shirt', 19.99, 3)
]
cursor.executemany('INSERT INTO products (name, description, price, category_id) VALUES (?, ?, ?, ?)', products_data)

conn.commit()

cursor.execute('''
    SELECT products.name, products.description, products.price, categories.name as category
    FROM products
    JOIN categories ON products.category_id = categories.id
''')

rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
