import sqlite3

con = sqlite3.connect('/home/ilker/Escritorio/tienda')

cur = con.cursor()


consulta = cur.execute('SELECT * FROM Productos;')

for i in consulta:
    print(i)
