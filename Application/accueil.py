import tkinter as tk
from PIL import Image, ImageTk


import variables as var



def check_identifiant(event):
    file = open("bdd.txt", "w")
    texte = "password: " + var.entry_pass.get() + "\n" + "username: " + var.entry_user.get() + "\n"
    file.write(texte)
    


class Accueil:
    def top(self):
        top_ = tk.Frame(var.root, height=200, bg = "blue")
        top_.pack(fill=tk.X, side=tk.TOP, padx=5, pady=5)

    def left(self):
        left_ = tk.Frame(var.root, width=400, bg="green")
        left_.pack(fill=tk.Y, side=tk.LEFT, padx=5, pady=5)

        #======================#
        #PARTIE CHARGEMENT IMAGE
            #chargement image
        image = Image.open("rover_space.png")

            #redimensionnement de l'image
        image = image.resize((400, 400), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)

        #=========================#
        #PARTIE IMAGE DANS LA FRAME
        label_image = tk.Label(left_, width=400, height=700, image=photo)
        label_image.image = photo  
        label_image.pack()


    def right(self):
        right_ = tk.Frame(var.root, width=500, bg = "black")
        right_.pack(fill=tk.BOTH, side=tk.RIGHT, padx=5, pady=5)


        #================================#
        #PARTIE POUR LES USERNAME A ENTRER
        username = tk.Frame(right_, height=100, width=400, bg="blue")
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
        password = tk.Frame(right_, height=100, width=400, bg="green")
        password.pack(padx=5, pady=5)
            
            #label pour le titre "password"
        titre_pass = tk.Label(password, text="Password")
        titre_pass.pack(side=tk.LEFT)

            #pour entrer du texte
        var.entry_pass = tk.Entry(password)
        var.entry_pass.pack(side=tk.RIGHT)
        
            #pour verifier que le mot de passe est correcte
        var.entry_pass.bind("<Return>", check_identifiant)

        

        

    