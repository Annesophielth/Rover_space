import tkinter as tk

import variables as var

def simu_main():
    var.left_.pack_forget()
    var.right_.pack_forget()
    var.top_.pack_forget()
    var.midlle_.pack_forget()

    simu = Simulation()
    simu.left()
    simu.right()


class Simulation:
    def left(self):
        var.left_ = tk.Frame(var.root, width=300, bg="black")
        var.left_.pack(fill=tk.Y, side=tk.LEFT, padx=5, pady=5)

    def right(self):
        var.right_ = tk.Frame(var.root, width=600, bg="blue")
        var.right_.pack(fill=tk.Y, side=tk.LEFT) 

        #PARTIE AFFICHE LE ROVER SELECTIONNE
        affiche_rover = tk.Frame(var.right_, width=600, height=500, bg="black")
        affiche_rover.pack(padx=5, pady=5)

        #PARTIE  DESCRIPTION DU ROVER SELECTIONNE
        descrip = tk.Frame(var.right_, width=600, height=200, bg="black")
        descrip.pack(fill=tk.Y, padx=5, pady=5)
        









