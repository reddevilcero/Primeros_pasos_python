import sqlite3

conexion = sqlite3.connect('productos.db')
cursor = conexion.cursor()

#cursor.execute('''
#	CREATE TABLE usuarios(
#		dni VARCHAR(9) PRIMARY KEY,
#		nombre VARCHAR(100),
#		edad INTEGER,
#		Email VARCHAR(100)
#	)
#	''')

#usuarios = [
#	('11111111A', 'Hector', 27, 'Hector@ejemplo.com'),
#	('11111111B', 'Mario', 51, 'Mario@ejemplo.com'),
#	('11111111C', 'Mercedes', 38, 'Mercedes@ejemplo.com'),
#	('11111111D', 'Juan', 19, 'Juan@ejemplo.com')
#
#]

#cursor.executemany('''
#	INSERT INTO usuarios 
#	VALUES (?,?,?,?)
#	''', usuarios)
#cursor.execute('''
#	CREATE TABLE productos(
#		id INTEGER PRIMARY KEY AUTOINCREMENT,
#		nombre VARCHAR(100) NOT NULL,
#		marca VARCHAR(50) NOT NULL,
#		price FLOAT NOT NULL
#
#	)
#	''')

productos = [
	('Teclado', 'Logitech', 19.95),
	('Pantalla 19"','LG',89.95)
]

cursor.executemany('INSERT INTO productos VALUES (null,?,?,?)', productos)


conexion.commit()
conexion.close()