import sqlite3
from tkinter import *

#Configuracion de la raiz

root = Tk()

root.title("Casa Rusu")
root.resizable(0,0)
root.config(bd=25, relief='sunken')
menubar = Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label="Agregar Categoria")
filemenu.add_command(label="Agregar Plato")
filemenu.add_command(label="Mostrar Menu")
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)
menubar.add_cascade(label="Gestor", menu= filemenu)

Button(root, text="Agregar Categoria").pack()
Button(root, text="Agregar Plato").pack()
Button(root, text="Mostrar Menu").pack()





root.mainloop()