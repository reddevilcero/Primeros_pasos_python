import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def popup_bonus():
    win = tk.Toplevel()
    win.wm_title("Window")

    l = tk.Label(win, text="Input")
    l.grid(row=0, column=0)

    b = ttk.Button(win, text="Okay", command=win.destroy)
    b.grid(row=1, column=0)

def popup_showinfo():
    showinfo("Window", "Hello World!")

class Application(ttk.Frame):

    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.pack()

        self.button_bonus = ttk.Button(self, text="Bonuses", command=popup_bonus)
        self.button_bonus.pack()

        self.button_showinfo = ttk.Button(self, text="Show Info", command=popup_showinfo)
        self.button_showinfo.pack()

root = tk.Tk()

app = Application(root)

root.mainloop()

  # initial value
'''
    top = Toplevel(root)
    option = OptionMenu(top, categoria_usuario, *ind_categorias)
    option.grid(row=1, column=1, sticky=W)
    Label(top, text='Seleciona Categoria').grid(row=1, column=0)
    Label(top, text="Nuevo Plato").grid(row=2)
    nuevo_plato = Entry(top).grid(row=2, column=1, sticky=W)
    print(nuevo_plato)'''