from tkinter import *

def callback(selection):
	print(selection)


root = Tk()

options = StringVar()
sel = [l for l in "casa"]
menu = OptionMenu(root, options, *sel, command=callback)
menu.pack()
options.set('')
root.mainloop()

