import random
import string
def choix_level(Lvl):
    
    global Longueur
    global Hauteur
    
    if (Lvl=="Facile"):
        Longueur = 10
        Hauteur = 5
    if (Lvl=="Moyen"):
        Longueur = 15
        Hauteur = 7
    if (Lvl=="Difficile"):
        Longueur = 30
        Hauteur = 15
Level = input("Facile \t Moyen \t Difficile \n Tapez votre niveau de jeu :")
choix_level(Lvl)

grille = [[random.choice(string.ascii_uppercase) for i in range(0,Longueur)] for j in range(0,Hauteur)]

def mot(mot, liste_mots):
    for i in liste_mots:
        if mot in i:
            return True
    return False

def cord(mot,reponse,cordo_x,cordo_y):
    for i in reponse:
        
        if mot==reponse[0] and cordo_x==reponse[1] and cordo_y==reponse[2] or mot==reponse[3] and cordo_x==reponse[4] and cordo_y==reponse[5] or mot==reponse[6] and cordo_x==reponse[7] and cordo_y==reponse[8] or mot==reponse[9] and cordo_x==reponse[10] and cordo_y==reponse[11] or mot==reponse[12] and cordo_x==reponse[13] and cordo_y==reponse[14] or mot==reponse[15] and cordo_x==reponse[16] and cordo_y==reponse[17]:  
            return True
        else:
            return False
        
        ##pas fini
