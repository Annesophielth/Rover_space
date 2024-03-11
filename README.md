# Rover_space
Il faut que vous vous créez vos propre branch de travail.
Ça permet de copier toute la branch main et si ya un soucis de ne pas modifier d'un coup la branche main.

Commande pour créer votre branche:

	git checkout -b <nom de votre branch>
	git branch #Pour connaitre toutes les branches

Commandes pour push dans la branch main:

	git checkout <nom de votre branche>
	git add . 
	git commit -m"< Ajout d'un comm sur ce que vous avez fait>"
	

	git checkout main	
	git merge <nom de votre branche> 
	git push origin main




commandes pour recup la branch du main: 
!!!À FAIRE À CHAQUE FOIS QUE L'ON TRAVAIL EN DÉBUT!!!

	git checkout <nom branch> 					#s'assurer d'être dans la branch main
	git pull origin main				#récup les modifs de tous


!!!!! TOUJOURS TRAVAILLER DANS VOTRE BRANCHE !!!!
!!!!! NORMALEMENT PERSONNE NE DOIT PUSH LA BRANCH MAIN !!!!


Autres commandes:

	git branch #savoir dans quel branch vous êtes 
	
	git checkout <nom branch> #comme un cd 
	
	git checkout -b <nom branch> #pour créer une nouvelle branch 
	git checkout -D <nom branch> #pour supp une branch !!!!NE SURTOUT PAS LE FAIRE SUR LE MAIN !!!!
	
