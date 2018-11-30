from tkinter import *
from funcionalidad import *

def update_monitor():

    conexion = sqlite3.connect('Menu_del_dia.db')
    cursor = conexion.cursor()
    cursor.execute('SELECT COUNT(*) FROM categoria')
    call1 = cursor.fetchone()
    cursor.execute('SELECT COUNT(*) FROM plato')
    call2 = cursor.fetchone()
    numplatos.set(f'Numero de platos: {call2[0]}')
    numcatg.set(f'Numero de Categorias: {call1[0]}')
    conexion.close()

def agregar_categoria():
    while True:
        nueva_categoria = SimpleDialog.askstring("Crear Nueva Categoria", "Cual es el Nombre de la nueva categoria?")
        conexion = sqlite3.connect('Menu_del_dia.db')
        cursor = conexion.cursor()
        if nueva_categoria != None:
            try:
                cursor.execute(f'INSERT INTO categoria VALUES(null, "{nueva_categoria}")')
            except sqlite3.IntegrityError:
                MessageBox.showwarning("Advertencia",f"Categoria {nueva_categoria} ya existe. ")
            else:
                mensaje.set(f"La Categoria {nueva_categoria} ha sido creada")
            finally:
                repeat = MessageBox.askyesno("Nueva Categoria","Crear una Nueva Categoria?")

                if repeat == True:
                    conexion.commit()
                    update_monitor()
                else:
                    conexion.commit()
                    conexion.close()
                    update_monitor()
                    return
        else:
             MessageBox.showwarning("Advertencia",f"No se ha creado ninguna categoria")
             return         
    




def crear_plato():

    conexion = sqlite3.connect('Menu_del_dia.db')
    cursor = conexion.cursor()

    categorias = cursor.execute('SELECT * FROM categoria').fetchall()

    ind_categorias = [c for c in categorias]

    selecion = StringVar()
   ########### obtiene la categoria elegida ####################
    def eleccion(selection):
        dropvar = selection
  
  ################ Obteniendo la seleccion de usario y enviandolo a la base de datos ##########################

    def datos():
        categoria_usuario = dropvar.get()
        nuevo_plato = entry.get()

        if categoria_usuario != "" and nuevo_plato != "":
            try:
                cursor.execute(f'INSERT INTO plato VALUES(null, "{nuevo_plato}","{categoria_usuario[1]}", 0)')
                conexion.commit()
                conexion.close()
                update_monitor()
            except sqlite3.IntegrityError:
                print("El plato ya Existe")
            else:
                mensaje.set(f"El plato {nuevo_plato} ha sido creado correctamente")
            finally:
                again = MessageBox.askyesno("Nuevo Plato","Quieres crear un nuevo plato?")
                if again == True:
                    top.destroy()
                    crear_plato()
                else:
                    top.destroy()    

        else:
            MessageBox.showwarning("Advertencia","No se ha creado ningun plato")
            repeat = MessageBox.askyesno('Sugerencia',"Quieres Salir sin crear un nuevo plato?")

            if repeat == True:
                conexion.close()
                top.destroy()
            else:
                top.destroy()
                crear_plato()      

    

 ############# creando el POPUP ##################################       
    top = Toplevel(root)
    ancho = 250
    alto = 100
    top.grab_set()
    dropvar = StringVar()
    dropmenu = OptionMenu(top, dropvar, *ind_categorias, command=eleccion)
    dropmenu.grid(row=1, column=1, sticky=W)
    Label(top, text='Seleciona Categoria').grid(row=1, column=0)
    Label(top, text="Nuevo Plato").grid(row=2)
    entry = Entry(top)
    entry.grid(row=2, column=1, sticky=W)
    Button(top, text='Agregar Plato', command=datos).grid(columnspan=2, pady=10)
    # Gets the requested values of the height and widht.
    screen_width = top.winfo_screenwidth()
    screen_height = top.winfo_screenheight()

    # Gets both half the screen width/height and window width/height
    co0rdenada_x = int((screen_width/2) - (ancho/2))
    coordenada_y = int((screen_height/2) - (alto/2))

    # Positions the window in the center of the page.
    top.geometry(f'{ancho}x{alto}+{co0rdenada_x}+{coordenada_y}')

def mostrar_menu():

    conexion = sqlite3.connect('Menu_del_dia.db')
    cursor = conexion.cursor()

    categorias = cursor.execute('SELECT * FROM categoria').fetchall()
    for categoria in categorias:
        print('\n',categoria[1])
        print('*'*10)
        platos = cursor.execute(f'SELECT * FROM plato WHERE categoria_id={categoria[0]}').fetchall()
        for plato in platos:
            print('\t',plato[1])    



################## Configuracion de la raiz ####################   

root = Tk()
root.title("Gestor Menu del dia")
alto = 500
ancho = 400
root.resizable(0,0)
root.config(bd=1)
menubar = Menu(root)
root.config(menu=menubar)


# Gets the requested values of the height and widht.
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
 
# Gets both half the screen width/height and window width/height
co0rdenada_x = int((screen_width/2) - (alto/2))
coordenada_y = int((screen_height/2) - (ancho/2))
 
# Positions the window in the center of the page.
root.geometry(f'{alto}x{ancho}+{co0rdenada_x}+{coordenada_y}')

#################### MENU BAR ##################################

filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label="Agregar Categoria", command=agregar_categoria)
filemenu.add_command(label="Agregar Plato", command=crear_plato)
filemenu.add_command(label="Mostrar Menu", command=mostrar_menu)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)
menubar.add_cascade(label="Gestor", menu= filemenu)

################### Monitor inferior #############################

mensaje = StringVar()
mensaje.set('Conectado a la Base de Datos')
monitor = Frame(bg='#D3D3D3')
monitor.pack(side=BOTTOM, fill=X)
l = Label(monitor, textvar=mensaje, bg='#D3D3D3')
l.pack(side='left')
numcatg = StringVar()
numplatos = StringVar()
l2 = Label(monitor, textvar=numplatos, bg='#D3D3D3')
l2.pack(side='right')
l3 = Label(monitor, textvar=numcatg, bg='#D3D3D3')
l3.pack(side='right')
update_monitor()

############################## Frame principal ##########################

f1 = Frame(bg = 'red')
f1.pack(fill =Y)




root.mainloop()
