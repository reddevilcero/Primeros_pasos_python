from tkinter import *
from tkinter import filedialog as FileDialog
from io import open

ruta='' # La utilizaremos para almacenar la ruta del fichero
typefile= (('Fichero de Texto', '*.txt'),('Todos los archivos', '*.*'))
def nuevo():
	global ruta
	mensaje.set("Nuevo fichero")
	ruta = ''
	texto.delete(1.0, 'end') # borra desde el primer caracter hasta el final
	root.title('Mi editor')
def abrir():
	global ruta
	mensaje.set("Abrir fichero")
	ruta = FileDialog.askopenfilename(
		initialdir='.',
		filetype=typefile,			
		title="Abrir un fichero de texto"
		)
	if ruta != '':
		fichero= open(ruta, 'r')
		contenido = fichero.read()
		texto.delete(1.0, 'end')
		texto.insert('insert', contenido)
		fichero.close()
		root.title(ruta + ' - Mi editor')


def guardar():
	global ruta
	mensaje.set("Guardar fichero")
	if ruta !='':
		contenido = texto.get(1.0, 'end-1c')
		fichero = open(ruta, 'w+')
		fichero.write(contenido)
		fichero.close()
		mensaje.set('Fichero guardado correctamente')
	else:
		guardar_como()
		


def guardar_como():
	global ruta
	mensaje.set("Guardar fichero como..")
	fichero = FileDialog.asksaveasfile(
		title='Guardar fichero como..',
		mode='w',
		defaultextension='.txt',
		filetype=typefile
		)
	if fichero is not None:
		ruta = fichero.name
		contenido = texto.get(1.0, 'end-1c')
		fichero = open(ruta, 'w+')
		fichero.write(contenido)
		fichero.close()
		mensaje.set('Fichero guardado correctamente')
	else:
		mensaje.set('Guardado Cancelado')
		ruta=''	





# Configuracion de la raiz
root = Tk()
root.title("Mi editor")


#Menu superior

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='Nuevo', command=nuevo)
filemenu.add_command(label='Abir', command=abrir)
filemenu.add_command(label='Guardar',command=guardar)
filemenu.add_command(label='Guardar como..',command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label='Salir', command=root.quit)
menubar.add_cascade(menu=filemenu, label="Archivo")

# Caja de texto Central

texto = Text(root)
texto.pack(fill='both', expand=1)
texto.config(bd=0, padx=6, pady=4, font=('Consolas',12))


#Monitor inferior

mensaje = StringVar()
mensaje.set('Bienvenidor a tu Editor')
monitor = Label(root, textvar=mensaje)
monitor.pack(side='left')

root.config(menu=menubar)
# Bucle de la aplicacion
root.mainloop()