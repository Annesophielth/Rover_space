import tkinter as tk
import random
import time


import variables as var





# Création de la fenetre principale
root = tk.Tk()
root.geometry("900x900")

# Creation du canvas principal pour notre carte
canvas_map = tk.Canvas(root, width=800, height=900, bg="#2fbdc4")
canvas_map.pack(padx=5, pady=5, side=tk.LEFT)

# Creation du cadrillage
for c in range(0, 800, 20):
    canvas_map.create_line(c, 0, c, 900)

for c in range(0, 900, 30):
    canvas_map.create_line(0, c, 800, c)


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
                canvas_map.create_rectangle(x, y, x + dim[0], y + dim[1], fill=couleur)

            if map[i][j] == 2:
                dim = var.dico_obstacle[2]["dimensions"]
                couleur = var.dico_obstacle[2]["couleur"]
                canvas_map.create_rectangle(x, y, x + dim[0], y + dim[1], fill=couleur)


            if map[i][j] == 3:
                dim = var.dico_obstacle[3]["dimensions"]
                couleur = var.dico_obstacle[3]["couleur"]
                canvas_map.create_rectangle(x, y, x + dim[0], y + dim[1], fill=couleur)

            if map[i][j] == 4:
                dim = var.dico_obstacle[4]["dimensions"]
                couleur = var.dico_obstacle[4]["couleur"]
                canvas_map.create_rectangle(x, y, x + dim[0], y + dim[1], fill=couleur)

map_rover = var.matrice
# Initialisation des coordonnées du rover et création du rectangle initial
i = 0
j = 0
rover = canvas_map.create_rectangle(i, j, i + 20, j + 30, fill="black")
canvas_map.update()  # Mettre à jour l'affichage initial

# Boucle de déplacement du rover
while map_rover[i][j] == 0:
    choix = random.randint(0, 1)
    x = i * 20
    y = j * 30

    # Supprimer le rectangle précédent du canvas
    canvas_map.delete(rover)

    if choix == 1:  # on va à droite
        rover = canvas_map.create_rectangle(x, y, x + 20, y+30, fill="black")
        i += 1

    else:  # on va tout droit en descendant si on veut
        rover = canvas_map.create_rectangle(x, y, x+20, y + 30, fill="black")
        j += 1

    canvas_map.update()  # Mettre à jour l'affichage
    time.sleep(1)  # Attendre un peu pour voir le mouvement


if (0): #EXEMPLE DE TEST 
    # Dessin d'un obstacle
    # x varie de 20 en 20
    # y varie de 30 en 30
    x = 200
    y = 210  # Ajustement pour l'alignement avec la grille
    canvas_map.create_rectangle(x, y, x + 20, y + 30, fill="#047c49")

    x = 200
    y = 240  # Ajustement pour l'alignement avec la grille
    canvas_map.create_rectangle(x, y, x + 20, y + 30, fill="#047c49")



tk.mainloop()
