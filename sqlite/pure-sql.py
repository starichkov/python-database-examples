import sqlite3

# open connection and cursor
connection = sqlite3.connect('pure-sql-jedi-order.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE jedi(id integer primary key, name varchar(100), phone varchar(40))''')

create_jedi = 'INSERT INTO jedi (id, name, phone) VALUES (?, ?, ?)'

cursor.execute(create_jedi, (1, 'Qui-Gon Jinn', '777-999-50-50'))
cursor.execute(create_jedi, (2, 'Obi-Wan Kenobi', '777-999-51-51'))
cursor.execute(create_jedi, (3, 'Anakin Skywalker', '777-999-52-52'))

cursor.execute('SELECT * FROM jedi ORDER BY id')

rows = cursor.fetchall()
print(rows)

# close connection and cursor
cursor.close()
connection.close()
