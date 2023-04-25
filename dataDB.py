# create a database and table for sales data and insert data into the table using Faker
import sqlite3
from faker import Faker
# create a sqlite database and table
db = sqlite3.connect('sales.db')
# create a cursor
cursor = db.cursor()
# check if table exists and if it does, drop it
cursor.execute('''DROP TABLE IF EXISTS sales''')

# create a table called sales with 4 columns
cursor.execute('''CREATE TABLE sales (id INTEGER PRIMARY KEY, name TEXT, address TEXT, city TEXT, state TEXT, zip TEXT, phone TEXT, email TEXT, product TEXT, price REAL, quantity INTEGER, total REAL)''')
# insert 5 rows of data into the table using Faker
for i in range(5):
    cursor.execute('''INSERT INTO sales (name, address, city, state, zip, phone, email, product, price, quantity, total) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (Faker().name(), Faker(
    ).address(), Faker().city(), Faker().state(), Faker().zipcode(), Faker().phone_number(), Faker().email(), Faker().word(), Faker().pyfloat(), Faker().pyint(), Faker().pyfloat()))
# commit the changes
db.commit()
# query the table for quantity and total and print the results
result = cursor.execute('''SELECT * FROM sales''')
# print the results
print(result.fetchall())
