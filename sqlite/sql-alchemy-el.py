import sqlalchemy as sa

connection_string = 'sqlite:///sql-alchemy-el-jedi-order.db'

connection = sa.create_engine(connection_string)

meta = sa.MetaData()

table_jedi = sa.Table(
    'jedi', meta,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('name', sa.String),
    sa.Column('phone', sa.String)
)
meta.create_all(connection)

connection.execute(
    table_jedi.insert((1, 'Qui-Gon Jinn', '777-999-50-50'))
)
connection.execute(
    table_jedi.insert((2, 'Obi-Wan Kenobi', '777-999-51-51'))
)
connection.execute(
    table_jedi.insert((3, 'Anakin Skywalker', '777-999-52-52'))
)

result = connection.execute(table_jedi.select())
rows = result.fetchall()
print(rows)
