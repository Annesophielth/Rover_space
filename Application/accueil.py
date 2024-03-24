import tkinter as tk
from PIL import Image, ImageTk


import variables as var
import choix 


PRINCIPAL_COLOR = "#5c83d2"


def check_identifiant(event):
    """
    A finir de coder proprement 
        Quand on fait la touche entrer, ça doit vérifier que dans le fichier bdd username 
        et password soit:
            °soit correcte
            °ou alors on l'ajoute car nouvelle connexion avec un nouveau scientifique
    """
    file = open("bdd.txt", "w")

    #AJOUT DE USERNAME ET PASSWORD DANS LE FICHIER
    texte = "password: " + var.entry_pass.get() + "\n" + "username: " + var.entry_user.get() + "\n"
    file.write(texte)

    #POUR CETTE PARTIE IL FAUT QUE LE LOGIN SOIT BIEN CODER
    #MAIS POUR LE TEST ON PART DU PRINCIPE QUE TOUT VA BIEN DONC EN 
    #FESANT <ENTRER>, ON PART SUR LA PAGE CHOIX: NOUVELLE MISSIN OU ÉVALUATION
    
    var.left_.pack_forget()
    var.right_.pack_forget()
    var.top_.pack_forget() 
    page_choix = choix.Choix()
    page_choix.left()
    page_choix.midlle()
    page_choix.right()


class Accueil:
    def top(self):
        var.top_ = tk.Frame(var.root, height=200, bg = "blue") 
        var.top_.pack(fill=tk.X, side=tk.TOP, padx=5, pady=5)

        titre = tk.Label(var.top_, text="e-Wali", bg="blue")
        titre.pack(fill=tk.X)

    def left(self):
        var.left_ = tk.Frame(var.root, width=400, bg=PRINCIPAL_COLOR)
        var.left_.pack(fill=tk.Y, side=tk.LEFT, padx=5, pady=5)

        #======================#
        #PARTIE CHARGEMENT IMAGE
            #chargement image
        image = Image.open("rover_space.png")

            #redimensionnement de l'image
        image = image.resize((400, 400), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)

        #=========================#
        #PARTIE IMAGE DANS LA FRAME
        label_image = tk.Label(var.left_, width=400, height=700, bg = PRINCIPAL_COLOR, image=photo)
        label_image.image = photo  
        label_image.pack()


    def right(self):
        var.right_ = tk.Frame(var.root, width=500, bg = PRINCIPAL_COLOR)
        var.right_.pack(fill=tk.BOTH, side=tk.RIGHT, padx=5, pady=5)

        top = tk.Frame(var.right_, height=233, bg=PRINCIPAL_COLOR)
        top.pack(fill=tk.X)

        midlle = tk.Frame(var.right_, height=233, bg=PRINCIPAL_COLOR)
        midlle.pack(fill=tk.X)

        bottom = tk.Frame(var.right_, height=233, bg=PRINCIPAL_COLOR)
        bottom.pack(fill=tk.X)
        #================================#
        #PARTIE POUR LES USERNAME A ENTRER
        username = tk.Frame(midlle, height=100, width=400, bg=PRINCIPAL_COLOR)
        username.pack(padx=5, pady=5)


            #label pour le titre "username"
        titre_user = tk.Label(username, text="Username")
        titre_user.pack(side=tk.LEFT)


            #pour entrer du texte
        var.entry_user = tk.Entry(username)
        var.entry_user.pack(side=tk.RIGHT)


            #pour verifier que le username est correcte

        #===============================#
        #PARTIE POUR LE PASSWORD A ENTRER
        password = tk.Frame(midlle, height=100, width=400, bg=PRINCIPAL_COLOR)
        password.pack(padx=5, pady=5)


            #label pour le titre "password"
        titre_pass = tk.Label(password, text="Password")
        titre_pass.pack(side=tk.LEFT)


            #pour entrer du texte
        var.entry_pass = tk.Entry(password)
        var.entry_pass.pack(side=tk.RIGHT)


            #pour verifier que le mot de passe est correcte
        var.entry_pass.bind("<Return>", check_identifiant)

        

        

    