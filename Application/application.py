import tkinter as tk

import variables as var
import accueil


def quitter(event):
    var.root.destroy()





#===========================================
#CODE PRINCIPALE
var.root = tk.Tk()
var.root.geometry("900x900")


page = accueil.Accueil()
page.top()
page.left()
page.right()



var.root.bind("<Escape>", quitter)
var.root.mainloop()
