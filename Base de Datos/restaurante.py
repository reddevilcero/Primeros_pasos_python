import sqlite3, tkinter

def crear_db():
    conexion = sqlite3.connect('restaurant.db')
    cursor = conexion.cursor()
    try:
        cursor.execute('''
            CREATE TABLE categoria(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL
            )
        ''')
    except sqlite3.OperationalError:
        print("La Tabla de categoria ya existe")
    else:
        print("La Tabla de categoria se ha creado correctamente")


    try:
        cursor.execute('''
            CREATE TABLE plato(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(100) UNIQUE NOT NULL,
            categoria_id INTEGER NOT NULL,
            FOREIGN KEY(categoria_id) REFERENCES categoria(id)
            )
        ''')
    except sqlite3.OperationalError:
        print("La Tabla de Platos ya existe")
    else:
        print("La Tabla de Platos se ha creado correctamente")   

    conexion.close()

def agregar_categoria():

    categoria = input('nombre de la Nueva Categoria?\n> ')

    conexion = sqlite3.connect('restaurant.db')
    cursor = conexion.cursor()
    try:
        cursor.execute(f'INSERT INTO categoria VALUES(null, "{categoria}")')
    except sqlite3.IntegrityError:
        print("La cateoria ya Existe")
    else:
        print(f"Categoria {categoria} creada correctamente")   

    conexion.commit()
    conexion.close()


def agregar_plato():
    
    conexion = sqlite3.connect('restaurant.db')
    cursor = conexion.cursor()

    categorias = cursor.execute('SELECT * FROM categoria').fetchall()
    print('seleciona una categoria para agregar el plato')

    ind_categorias = []

    for categoria in categorias:
        print(f'[{categoria[0]}] {categoria[1]}')
        ind_categorias.append(categoria[0])
    
    categoria_usuario = int(input('\n>>>'))

    if categoria_usuario in ind_categorias:
        plato = input('Nombre del nuevo Plato?\n')

        try:
            cursor.execute(f'INSERT INTO plato VALUES(null, "{plato}","{categoria_usuario}")')
        except sqlite3.IntegrityError:
            print("El plato ya Existe")
        else:
            print(f"El Plato {plato} creado correctamente")

    else:
        print("La categoria indicada no existe")       
    
    conexion.commit()
    conexion.close()    

  # Crear la base de Datos 

def mostrar_menu():

    conexion = sqlite3.connect('restaurant.db')
    cursor = conexion.cursor()

    categorias = cursor.execute('SELECT * FROM categoria').fetchall()
    for categoria in categorias:
        print('\n',categoria[1])
        print('*'*10)
        platos = cursor.execute(f'SELECT * FROM plato WHERE categoria_id={categoria[0]}').fetchall()
        for plato in platos:
            print('\t',plato[1])

  

    conexion.close()


crear_db()
#  Menu de opciones del programa     
while  True:
    print('\nBienvenido al gestor del restaurante!')
    opcion= input('\nIntroduce una opcion:\n[1] Agregar una categoria\n[2] Agregar un Plato\n[3] Mostrar Menu\n[4] Salir del programa\n>>>')

    if opcion == '1':
        agregar_categoria()

    elif opcion == '2':
        agregar_plato() 

    elif opcion == '3':
        mostrar_menu()     

    elif opcion == '4':
        print("Gracias por usar este Gestor")
        break

    else:
        print("Opcion Incorrecta")    
        
