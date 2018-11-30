from tkinter import *

# configuracion de la raiz
root = Tk()

menubar = Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label="Nuevo")
filemenu.add_command(label="Abrir")
filemenu.add_command(label="Guardar")
filemenu.add_command(label="Cerrar")
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)



editmenu = Menu(menubar, tearoff = 0)
editmenu.add_command(label="Cortar")
editmenu.add_command(label="Copiar")
editmenu.add_command(label="Pegar")

helpmenu = Menu(menubar, tearoff = 0)
helpmenu.add_command(label="Ayudar")
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de....")



menubar.add_cascade(label="File", menu= filemenu)
menubar.add_cascade(label="Edit", menu= editmenu)
menubar.add_cascade(label="Help", menu= helpmenu)




# Finalmente bucle de la aplicacion
root.mainloop()