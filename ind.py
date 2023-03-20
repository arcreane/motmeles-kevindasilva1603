import string
import random


 

def add_mot(liste_mots,grille):
    liste_mots = random.choice([liste_mots,liste_mots[::-1]]) 

    direction = random.choice([[1,0],[0,1]])
    
 
    taille_x = Longueur if direction[0] == 0 else Longueur - len(liste_mots) 
    taille_y = Hauteur if direction[1] == 0 else Hauteur - len(liste_mots)
    global x,y
    x = random.randrange(0,taille_x)
    y = random.randrange(0,taille_y)
    

    for i in range(0,len(liste_mots)):
        
        grille[y+direction[1]*i][x+direction[0]*i] = liste_mots[i]
        
    return grille
reponse = []
if Lvl == 'Facile':
    liste_mots = ["WEB","PHP","SQL","BUG","BIT","IP"]
         
    for mot in liste_mots:
        grille = add_mot(mot,grille)
        reponse.append(mot)
        reponse.append(x)
        reponse.append(y)
        
if Lvl == 'Moyen':
    liste_mots = ["PATCHS","PYTHON","JAVA","ASCII"]
    for mot in liste_mots:
        grille = add_mot(mot,grille)
        reponse.append(mot)
        reponse.append(x)
        reponse.append(y)
if Lvl == 'Difficile':
    liste_mots = ["JAVASCRIPT","VULNERABILITE","CYBERATTAQUE","ALGORITHMIE"]
    for mot in liste_mots:
        grille = add_mot(mot,grille)
        reponse.append(mot)
        reponse.append(x)
        reponse.append(y)

mot=input("Rentrez le mot que vous avez trouvé: ")
print(reponse)
if mot(mot,liste_mots):
     print("Le mot",mot,"est présent dans la liste.")
else:
    print("Le mot",mot,"n'est pas présent dans la liste, veuillez verifier votre mot")
    exit()

cordo_x=int(input("Rentrez la cordonnée x (horizontale): "))
cordo_y=int(input("Rentrez la cordonnée y (verticale): "))
