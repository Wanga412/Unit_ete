# coding: utf-8
import socket     # Import socket module
from datetime import datetime
import requests
import json

URL = 'http://127.0.0.1:5000/getValue'
HOST = "172.20.10.5"  # Ip de connection au serveur
PORT = 30921 # Port de connection au serveur

s = socket.socket()
try:
    s.bind((HOST, PORT))    # Bind to the port
    s.listen(1)
    # Now wait for client connection. On at the time.

    print("Server listening on port : {0}".format(PORT))

    # Indication de chaque valeur 0: lumiere  1: humidite  2: temperature  3: pression  4: heure d'envoie des données
    dictionnaire_capteur = {0: [], 1: [], 2: [], 3: [], 4: []}
    
    count = 0
    
    # Establish connection with client.
    conn, addr = s.accept()
    while True:
        # Recover 64 bytes of data from the socket.
        msg_bytes = conn.recv(64)
    
        dictionnaire_capteur[count].append(msg_bytes.decode("ASCII"))
        
        count += 1
    
        if count > 3:
            dictionnaire_capteur[count].append(datetime.now().strftime("%H:%M"))
            requests.post(URL, data = dictionnaire_capteur)
            count = 0
    
        # Decode bytes to ASCII
        #msg = msg_bytes.decode("ASCII")
    
        #print("Message received : \"{}\"".format(msg))
        print(dictionnaire_capteur)

except Exception as e:
    print(e)
    print("Connexion déjà établi")
