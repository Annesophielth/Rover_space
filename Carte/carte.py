import tkinter as tk
import random
import time


import variables as var


def create_map():
    # Creation du canvas principal pour notre carte
    var.canvas_map = tk.Canvas(var.root, width=800, height=900, bg="#2fbdc4")
    var.canvas_map.pack(padx=5, pady=5, side=tk.LEFT)

    # Creation du cadrillage
    for c in range(0, 800, 20):
        var.canvas_map.create_line(c, 0, c, 900)

    for c in range(0, 900, 30):
        var.canvas_map.create_line(0, c, 800, c)


def gen_obstacle():
    #Génaration de la map avec les obstacles
    map = var.matrice
    taille = len(map)

    for i in range(taille-1):
        x = i * 20
        for j in range(len(map[0])-1):
            y = j * 30

            if (map[i][j] != 0):
                if map[i][j] == 1:
                    dim = var.dico_obstacle[1]["dimensions"]
                    couleur = var.dico_obstacle[1]["couleur"]
                    var.canvas_map.create_rectangle(x, y, x + dim[0], y + dim[1], fill=couleur)

                if map[i][j] == 2:
                    dim = var.dico_obstacle[2]["dimensions"]
                    couleur = var.dico_obstacle[2]["couleur"]
                    var.canvas_map.create_rectangle(x, y, x + dim[0], y + dim[1], fill=couleur)


                if map[i][j] == 3:
                    dim = var.dico_obstacle[3]["dimensions"]
                    couleur = var.dico_obstacle[3]["couleur"]
                    var.canvas_map.create_rectangle(x, y, x + dim[0], y + dim[1], fill=couleur)

                if map[i][j] == 4:
                    dim = var.dico_obstacle[4]["dimensions"]
                    couleur = var.dico_obstacle[4]["couleur"]
                    var.canvas_map.create_rectangle(x, y, x + dim[0], y + dim[1], fill=couleur)

def gen_materiaux():
    #Génaration de la map avec les obstacles
    map = var.matrice
    taille = len(map)

    for i in range(taille-1):
        x = i * 20
        for j in range(len(map[0])-1):
            y = j * 30

            if (map[i][j] != 0):
                if map[i][j] == 5:
                    couleur = var.dico_obstacle[1]["couleur"]
                    var.canvas_map.create_oval(x, y, x + 20, y + 30, fill=couleur)

                if map[i][j] == 6:
                    couleur = var.dico_obstacle[2]["couleur"]
                    var.canvas_map.create_oval(x, y, x + 20, y + 30, fill=couleur)


                if map[i][j] == 7:
                    couleur = var.dico_obstacle[3]["couleur"]
                    var.canvas_map.create_oval(x, y, x + 20, y + 30, fill=couleur)

                if map[i][j] == 8:
                    couleur = var.dico_obstacle[4]["couleur"]
                    var.canvas_map.create_oval(x, y, x + 20, y + 30, fill=couleur)


def move_rover():
    map_rover = var.matrice
    # Initialisation des coordonnées du rover et création du rectangle initial
    i = 0
    j = 0
    rover = var.canvas_map.create_rectangle(i, j, i + 20, j + 30, fill="black")
    var.canvas_map.update()  # Mettre à jour l'affichage initial

    continuer = 1
    # Boucle de déplacement du rover
    #Corriger le fais que un obstacle à une taille 
    while continuer: 
        choix = random.randint(0, 1)
        x = i * 20
        y = j * 30

        # Supprimer le rectangle précédent du canvas
        var.canvas_map.delete(rover)

        if choix == 1:  # on va à droite
            rover = var.canvas_map.create_rectangle(x, y, x + 20, y+30, fill="black")
            i += 1
        else:  # on va tout droit en descendant si on veut
            rover = var.canvas_map.create_rectangle(x, y, x+20, y + 30, fill="black")
            j +=1
        var.canvas_map.update()  # Mettre à jour l'affichage
        time.sleep(0.5)  # Attendre un peu pour voir le mouvement

        if (map_rover[i][j] == 1 or map_rover[i][j] == 2 or map_rover[i][j] == 3 or map_rover[i][j] == 4):
            continuer = 0
            nom = var.dico_obstacle[map_rover[i][j]]["nom"]
            print(f"Je suis bloqué par un {nom}")

        if 4 < map_rover[i][j] <= 8:
            collect_info(map_rover[i][j])
        



def collect_info(ele):
    materiaux = var.dico_materiaux[ele]["nom"]
    print(f"collecte de: {materiaux}")

def main():
    # Creation de la fenetre principale
    var.root = tk.Tk()
    var.root.geometry("900x900")

    #Carte
    create_map()
    gen_obstacle()
    gen_materiaux()
    move_rover()    

    tk.mainloop()


if __name__ == "__main__":
    main()




