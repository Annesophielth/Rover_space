import tkinter as tk

import variables as var
import simulation
import eval_simu

class Choix:
    """
    ---------------------------------
    |          |          |         |
    |          |          |         |
    |          |          |         |
    |          |          |         |
    |  LEFT    | MIDLLE   | RIGHT   |
    |          |          |         |
    |          |          |         |
    |          |          |         |
    |          |          |         |
    ---------------------------------
    """
    def left(self):
        var.left_ = tk.Frame(var.root, width=300, bg="blue")
        var.left_.pack(fill=tk.Y, side=tk.LEFT)

    def midlle(self):
        var.midlle_ = tk.Frame(var.root, width=300, bg="black")
        var.midlle_.pack(fill=tk.Y, side=tk.LEFT)

        #PARTIE CHOIX "NOUVELLE SIMULATON"
        new_simu = tk.Button(var.midlle_, width=40, text="Nouvelle simulation", command=simulation.simu_main)
        new_simu.pack(expand=True)

        #PARTIE CHOIX "EVALUATION D'UNE SIMULATION"
        eval_simu_ = tk.Button(var.midlle_, width=40, text="Evaluation de simulation(s)", command=eval_simu.simu_main)
        eval_simu_.pack(expand=True)

    def right(self):
        var.right_ = tk.Frame(var.root, width=300, bg="blue")
        var.right_.pack(fill=tk.Y, side=tk.RIGHT)