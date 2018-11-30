import sqlite3

conexion = sqlite3.connect('ejemplo.db')

cursor = conexion.cursor()

#cursor.execute('CREATE TABLE usuarios (nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))')

#cursor.execute("INSERT INTO usuarios VALUES ('Pedro', 27, 'ejemplo@ejemplo.com')")

#cursor.execute('SELECT * FROM usuarios')
#usuario = cursor.fetchone()


#usuarios = [
#	('Delia', 39, 'Delia@da.c'),
#	('Pedro', 36, 'Pedro@da.c'),
#	('Bianca', 11, 'Bianca@da.c')
#]

#cursor.executemany('INSERT INTO usuarios VALUES(?,?,?)',usuarios)

cursor.execute('''
	SELECT * FROM usuarios
''')

usuarios = cursor.fetchall()

for usuario in usuarios:
	print(usuario[0])


conexion.commit()
conexion.close()