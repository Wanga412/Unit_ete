import socket
import time
import binascii
import pycom


from network import LoRa
from CayenneLPP import CayenneLPP
from pysense import Pysense
from LIS2HH12 import LIS2HH12
from SI7006A20 import SI7006A20
from LTR329ALS01 import LTR329ALS01
from MPL3115A2 import MPL3115A2, ALTITUDE, PRESSURE
from network import WLAN
import machine

py = Pysense()
si = SI7006A20(py)
lt = LTR329ALS01(py)
li = LIS2HH12(py)

SERVER_ADDRESS = "172.20.10.5" # Ip de connection au serveur
SERVER_PORT = 30921 # Port de connection au serveur

wlan = WLAN(mode=WLAN.STA)

# Se connect au WIFI indiqué
# Nom du Wifi Lucas
# Mot de passe '123456789'
wlan.connect(ssid='Lucas', auth=(WLAN.WPA2, '123456789'))

# Regarde s'il n'y a pas de connection 
while not wlan.isconnected():
    machine.idle() # Met en attente le programme jusqu'a la connection au WIFI

print("WiFi connected succesfully")

print(wlan.ifconfig())


s = socket.socket() # Create a socket object

s.connect((SERVER_ADDRESS, SERVER_PORT)) # Establish connection

while(1):
    lpp = CayenneLPP()

    #Lumière
    s.send(str(lt.light()[0]).encode("ASCII"))
    lpp.add_luminosity(2, lt.light()[0])
    print("Lumière :{}".format(lt.light()[0]))


    #Humidité
    s.send(str(si.humidity()).encode("ASCII"))
    lpp.add_relative_humidity(3, si.humidity())
    print("Humidité : {}".format(si.humidity()))

    #Température
    s.send(str(si.temperature()).encode("ASCII"))
    lpp.add_temperature(4, si.temperature())
    print("Température : {}".format(si.temperature()))

    #Pression
    mpPress = MPL3115A2(py,mode=PRESSURE)
    s.send(str(mpPress.pressure()/100).encode("ASCII"))
    lpp.add_barometric_pressure(5, mpPress.pressure()/100)
    print("Pression : {}".format(mpPress.pressure()/100))
    
    print("Message envoyé")