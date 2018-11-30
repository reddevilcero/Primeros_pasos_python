import sqlite3
from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import simpledialog as SimpleDialog
   
def crear_db():
    
    conexion = sqlite3.connect('Menu_del_dia.db')
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


    try:
        cursor.execute('''
            CREATE TABLE plato(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(100) UNIQUE NOT NULL,
            categoria_id INTEGER NOT NULL,
            menu INTEGER DEFAULT 0,
            FOREIGN KEY(categoria_id) REFERENCES categoria(id)
            )
        ''')
    except sqlite3.OperationalError:
        print("La Tabla de Platos ya existe")
      

    conexion.close()




crear_db()    





