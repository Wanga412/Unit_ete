<h1 align=center>Capteurs Wireless</h1>



Se projet permet de recevoir des données transmise par un pycom et un pysence par le wifi. Les données reçus sont ensuite envoyer sur un site internet qui les transformes pour les mettre dans des graphiques qui nous permettent de voir les fluctuation des données.



## Fonctionnement:

Pour faire fonctionner le projet il y a des conditions à respecter. Il faudra en premier lieux que tous les appareils soient connecter sur le même réseau Wifi. Ensuite, il faudra démarrer un serveur Flask qui permettra d'avoir un site internet qu'on pourra accéder avec l'adresse IP du serveur sur le port 5000. Les fichiers qui permettent de recevoir les données de la pycom devra se trouver dans un environnement Flask. Enfin, il faudra faire des modifications à  certains fichier pour qu'ils puisse communiquer entre eux.



## Modification à apporter au fichier :

### main.py :

Il faudra apporter une modification au programme. Il faut modifier l'IP de connexion avec celle de la machine qui contient le serveur.

![image-20210909170829657](C:\Users\Admin\AppData\Roaming\Typora\typora-user-images\image-20210909170829657.png)



### servReception.py :

Il faut modifier l'IP de connexion avec celle de la machine qui contient le serveur.

![image-20210913095212908](C:\Users\Admin\AppData\Roaming\Typora\typora-user-images\image-20210913095212908.png)



### lecteureCapteur.py :

Dans ce fichier il faudra modifier l'adresse IP qui est avec celle du serveur.

![image-20210913095035839](C:\Users\Admin\AppData\Roaming\Typora\typora-user-images\image-20210913095035839.png)

Il faudra changer aussi la connexion Wifi. c'est à dire le nom et le mot de passe ![image-20210913094954261](C:\Users\Admin\AppData\Roaming\Typora\typora-user-images\image-20210913094954261.png)
