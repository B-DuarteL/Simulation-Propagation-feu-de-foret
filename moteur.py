import random
VIDE , ARBRE , FEU , CENDRES = 0 , 1 , 2 , 3
def generer_foret (n , densite =0.65) :
""" Genere une grille n x n avec ’densite ’ d’arbres ."""
return [[ ARBRE if random . random () < densite else VIDE
for _ in range ( n ) ] for _ in range ( n ) ]