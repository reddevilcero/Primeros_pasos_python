from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog



# Configuracion de la raiz

root = Tk()


def test():
	#MessageBox.showinfo("Hola!","Hola mundo")
	#MessageBox.showwarning("Alerta","seccion solo para admins")
	#MessageBox.showerror("Error!","Ha Ocurrido un error inesperado")
	#restultado = MessageBox.askquestion("Salir","Estas seguro que quieres salir")
	#f restultado == 'yes':
		#root.destroy()

#	restultado = MessageBox.askokcancel("Salir","Sobreescribir el fichero actual?")
#	if restultado == True:
#		root.destroy()

#	restultado = MessageBox.askyesno("Salir","Sobreescribir el fichero actual?")
#	if restultado:
#		root.destroy()	

#	restultado = MessageBox.askretrycancel("Reintentar","No se puede conectar")
#	if restultado:
#		root.destroy()
#
#	color = ColorChooser.askcolor(title="Elige un color")

    #ruta = FileDialog.askopenfilename(
    #	title="Abrir un fichero",
    #	initialdir="C:/",
    #	filetypes = (
    #		("jpeg files","*.jpg"),
    #		)
    #	)
    # Equivale a open('ruta','w')
    fichero = FileDialog.asksaveasfile(
        title="Guardar un fichero", 
        mode='w',
        defaultextension='.txt',
        filetypes=(
            ("txt files", '*.txt'),
            ('all files', '*.*')
            )
        )
    if fichero is not None:
        fichero.write("Adios")
        fichero.close()


    
    
	

Button(root, text="Click me", command=test).pack()



# Bucle de la app
root.mainloop()