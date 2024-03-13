import socket

# Définir l'adresse IP et le port sur lesquels le serveur écoutera
HOST = '127.0.0.1'  # localhost
PORT = 12345  # Port arbitraire

# Créer un socket IPv4, de type TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Lier le socket à l'adresse et au port spécifiés
server_socket.bind((HOST, PORT))

# Commencer à écouter les connexions entrantes, avec un maximum de 1 connexion en attente
server_socket.listen(1)

print('Le serveur est prêt à écouter...')

# Attendre qu'une connexion soit établie
client_socket, client_address = server_socket.accept()

print('Connexion établie avec', client_address)

# Recevoir des données du client
while True:
    data = client_socket.recv(1024)
    if not data:
        break
    print('Reçu:', data.decode())

# Fermer la connexion avec le client
client_socket.close()

# Fermer le socket du serveur
server_socket.close()

