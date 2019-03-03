import sqlalchemy as sa

# dialect + driver :// user : password @ host : port / dbname

# in case of SQLite explicit driver mention ('+pysqlite') is redundant
connection_string = 'sqlite+pysqlite:///sql-alchemy-jedi-order.db'

connection = sa.create_engine(connection_string)

connection.execute('''CREATE TABLE jedi(id integer primary key, name varchar(100), phone varchar(40))''')

create_jedi = 'INSERT INTO jedi (id, name, phone) VALUES (?, ?, ?)'

connection.execute(create_jedi, (1, 'Qui-Gon Jinn', '777-999-50-50'))
connection.execute(create_jedi, (2, 'Obi-Wan Kenobi', '777-999-51-51'))
connection.execute(create_jedi, (3, 'Anakin Skywalker', '777-999-52-52'))

rows = connection.execute('SELECT * FROM jedi ORDER BY id')
for row in rows:
    print(row)
