# ############################################################################
#
# Programme : Puissance 4
# Version : 4
# Date : 20 juin 2019
# Interpréteur : Python 3.2
# Environnement de développement : EduPython 2.5.3.0
# Auteur : Jean-Christophe MICHEL
#
# ----------------------------------------------------------------------------
#
# Comme la version 3 cette version 4 :
# - demande aux joueurs à tour de role dans quelle colonne il veulent jouer
# - détecte une colonne pleine
# - détecte la grille pleine
# - détecte 4 pions alignés verticalement
# - détecte 4 pions (ou plus) alignés horizontalement
# - détecte 4 pions (ou plus) alignés en diagonale croissante
# - détecte 4 pions (ou plus) alignés en diagonale décroissante
# - filtre la saisie de l'utilisateur et envoie un message sur la sortie standard si la saisie est erronée
# - affiche la grille graphiquement dans une fenêtre de la tortue (module turtle)
# - quitte immédiatement le programme si l'utilisateur saisie f (comme Fin)
# - sauvegarde l'état de la partie (grille+joueur courant) dans le fichier texte grille.txt (saisir S)
# - restaure l'état d'une partie (grille+joueur courant) enregistré dans le fichier grille.txt afin de finir la partie (saisir R)
# - demande au démarrage le joueur qui commence (ROUGE ou BLEU)
# - affiche la fenêtre de la tortue en taille minimale dans le coin supérieur gauche de l'écran (réduire la fenêtre de Python dans la moitié droite de l'écran avant de lancer le programme)
#
# En plus pour cette version 4 :
# - le jouer BLEU est joué automatiquement par l'ordinateur : le seul joueur humain est le joueur ROUGE
#
# ############################################################################

from turtle import *
import os,random

# Structure de donnée mémorisant la grille : une liste à 2 dimensions (6 lignes et 7 colonnes) contenant :
# - un 0 si la case est vide
# - un 1 si un pion ROUGE est dans la case
# - un 2 si un pion BLEU est dans la case

grille=[7*[0], 7*[0], 7*[0], 7*[0], 7*[0], 7*[0]]

""" Repérage des éléments dans la grille :

élément grille[0][0] (coin supérieur gauche) :
[[X, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0]]

élément grille[0][6] (coin supérieur droit) :
[[0, 0, 0, 0, 0, 0, X],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0]]

élément grille[5][0] (coin inférieur gauche) :
[[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [X, 0, 0, 0, 0, 0, 0]]

élément grille[5][6] (coin inférieur droit):
[[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, X]]

 """

# tab_colonne mémorise le nombre de pions dans chacune des colonnes
tab_colonne=7*[0]
# joueur_courant indique le prochain joueur qui doit jouer : 1 pour ROUGE et 2 pour BLEU
joueur_courant=1

# ############################################################################
# La fonction qui_commence() demande à l'utilisateur le joueur qui commence (ROUGE ou BLEU)
def qui_commence():
    global joueur_courant
    s=""
    while not s in ["1","2"]:
        s=input("Quel joueur commence ? Entrez 1 pour ROUGE ou 2 pour BLEU :")
    joueur_courant=int(s)

# ############################################################################
# La fonction afficher_grille() affiche la grille sur la sortie standard
def afficher_grille():
    for i in range(6):
        print(grille[i])

    # affiche le repère des colonnes sous la grille :
    print('\n 0  1  2  3  4  5  6')


# ############################################################################
# La fonction grille_pleine() teste si la grille est pleine (aucun 0 dans la liste grille)
def grille_pleine():
    b_plein=True
    for i in range(6):
        for j in range(7):
            if grille[i][j]==0:
                b_plein=False
    return b_plein

# ############################################################################
# La fonction pions_alignes() teste si 4 pions de même couleur sont alignés dans la grille
def pions_alignes():
    trouve=0

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # teste 4 pions alignés horizontalement en alanysant chacune des 6 lignes :
    for i in range(6):
        rouge=0
        bleu=0
        for j in range(7):
            if grille[i][j]==1:
                rouge+=1
                bleu=0
                if rouge>=4:
                    trouve=1
                    return trouve
            elif grille[i][j]==2:
                rouge=0
                bleu+=1
                if bleu>=4:
                    trouve=2
                    return trouve
            else:
                rouge=0
                bleu=0

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # teste 4 pions alignés verticalement en alanysant chacune des 7 colonnes :
    for j in range(7):
        rouge=0
        bleu=0
        for i in range(6):
            if grille[i][j]==1:
                rouge+=1
                bleu=0
                if rouge>=4:
                    trouve=1
                    return trouve
            elif grille[i][j]==2:
                rouge=0
                bleu+=1
                if bleu>=4:
                    trouve=2
                    return trouve
            else:
                rouge=0
                bleu=0

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # teste les 6 diagonales croissantes :
    """
    [0, 0, 0, X, X, X, X]
    [0, 0, X, X, X, X, X]
    [0, X, X, X, X, X, X]
    [X, X, X, X, X, X, 0]
    [X, X, X, X, X, 0, 0]
    [X, X, X, X, 0, 0, 0]

    On part d'une case de départ (D ci-dessous) puis on incrémente les indices en diagonale jusqu'à atteindre l'indice maximal de la grille :

    grille[i][j] (i=n° de la ligne de 0 à 5 et j=n° de la colonne de 0 à 6)

j :  0  1  2  3  4  5  6
    [0, 0, 0, X, X, X, X] 0
    [0, 0, X, X, X, X, X] 1
    [0, X, X, X, X, X, X] 2
    [D, X, X, X, X, X, 0] 3
    [D, X, X, X, X, 0, 0] 4
    [D, D, D, D, 0, 0, 0] 5
                          i

    Analyse du problème :
    Il y a :
        2 diagonales à 4 cases (ij) : 30 21 12 03 et 53 44 35 26
        2 diagonales à 5 cases (ij) : 40 31 22 13 04 et 52 43 34 25 16
        2 diagonales à 6 cases (ij) : 50 41 32 23 14 05 et 51 42 33 24 15 06

    Dans les 6 cas j est croissant (analyse des diagonales de gauche à droite) et i est une fonction de j :
    diagonale à 4 cases (ij) 30 21 12 03 : j de 0 à 3 et i=3-j
    diagonale à 4 cases (ij) 53 44 35 26 : j de 3 à 6 et i=8-j

    diagonale à 5 cases (ij) 40 31 22 13 04 : j de 0 à 4 et i=4-j
    diagonale à 5 cases (ij) 52 43 34 25 16 : j de 2 à 6 et i=7-j

    diagonale à 6 cases (ij) 50 41 32 23 14 05 : j de 0 à 5 et i=5-j
    diagonale à 6 cases (ij) 51 42 33 24 15 06 : j de 1 à 6 et i=6-j

    Optimisons : le compteur de base est j, les 3 autres sont fonction de j :

    diagonale à 4 cases (ij) 30 21 12 03 : j de 0 à 3 et i=3-j
    diagonale à 4 cases (kl) 53 44 35 26 : k=i+2 et l=j+3

    diagonale à 5 cases (ij) 40 31 22 13 04 : j de 0 à 4 et i=4-j
    diagonale à 5 cases (kl) 52 43 34 25 16 : k=i+1 et l=j+2

    diagonale à 6 cases (ij) 50 41 32 23 14 05 : j de 0 à 5 et i=5-j
    diagonale à 6 cases (kl) 51 42 33 24 15 06 : k=i et l=j+1
    """

    # test des 2 diagonales croissantes à 4 cases :
    rouge=[0,0]
    bleu=[0,0]

    for j in range(4):
        i=3-j
        k=i+2
        l=j+3
        if grille[i][j]==1:
            rouge[0]+=1
            bleu[0]=0
            if rouge[0]>=4:
                trouve=1
                return trouve
        elif grille[i][j]==2:
            rouge[0]=0
            bleu[0]+=1
            if bleu[0]>=4:
                trouve=2
                return trouve
        else:
            rouge[0]=0
            bleu[0]=0

        if grille[k][l]==1:
            rouge[1]+=1
            bleu[1]=0
            if rouge[1]>=4:
                trouve=1
                return trouve
        elif grille[k][l]==2:
            rouge[1]=0
            bleu[1]+=1
            if bleu[1]>=4:
                trouve=2
                return trouve
        else:
            rouge[1]=0
            bleu[1]=0

    # test des 2 diagonales croissantes à 5 cases :
    rouge=[0,0]
    bleu=[0,0]

    for j in range(5):
        i=4-j
        k=i+1
        l=j+2
        if grille[i][j]==1:
            rouge[0]+=1
            bleu[0]=0
            if rouge[0]>=4:
                trouve=1
                return trouve
        elif grille[i][j]==2:
            rouge[0]=0
            bleu[0]+=1
            if bleu[0]>=4:
                trouve=2
                return trouve
        else:
            rouge[0]=0
            bleu[0]=0

        if grille[k][l]==1:
            rouge[1]+=1
            bleu[1]=0
            if rouge[1]>=4:
                trouve=1
                return trouve
        elif grille[k][l]==2:
            rouge[1]=0
            bleu[1]+=1
            if bleu[1]>=4:
                trouve=2
                return trouve
        else:
            rouge[1]=0
            bleu[1]=0

    # test des 2 diagonales croissantes à 6 cases :
    rouge=[0,0]
    bleu=[0,0]

    for j in range(6):
        i=5-j
        k=i
        l=j+1
        if grille[i][j]==1:
            rouge[0]+=1
            bleu[0]=0
            if rouge[0]>=4:
                trouve=1
                return trouve
        elif grille[i][j]==2:
            rouge[0]=0
            bleu[0]+=1
            if bleu[0]>=4:
                trouve=2
                return trouve
        else:
            rouge[0]=0
            bleu[0]=0

        if grille[k][l]==1:
            rouge[1]+=1
            bleu[1]=0
            if rouge[1]>=4:
                trouve=1
                return trouve
        elif grille[k][l]==2:
            rouge[1]=0
            bleu[1]+=1
            if bleu[1]>=4:
                trouve=2
                return trouve
        else:
            rouge[1]=0
            bleu[1]=0



    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # teste les 6 diagonales décroissantes :
    """
    grille[i][j] (i=n° de la ligne de 0 à 5 et j=n° de la colonne de 0 à 6)

j :  0  1  2  3  4  5  6
    [X, X, X, X, 0, 0, 0] 0
    [X, X, X, X, X, 0, 0] 1
    [X, X, X, X, X, X, 0] 2
    [0, X, X, X, X, X, X] 3
    [0, 0, X, X, X, X, X] 4
    [0, 0, 0, X, X, X, X] 5
                          i

    Analyse du problème :
    Il y a :
        2 diagonales décroissantes à 4 cases (ij) : 03 14 25 36 et 20 31 42 53
        2 diagonales décroissantes à 5 cases (ij) : 02 13 24 35 46 et 10 21 32 43 54
        2 diagonales décroissantes à 6 cases (ij) : 01 12 23 34 45 56 et 00 11 22 33 44 55

    Dans les 6 cas j est croissant (analyse des diagonales de gauche à droite) et i est une fonction de j :
    diagonale à 4 cases (ij) 03 14 25 36 : j de 3 à 6 et i=j-3
    diagonale à 4 cases (ij) 20 31 42 53 : j de 0 à 3 et i=j+2

    diagonale à 5 cases (ij) 02 13 24 35 46 : j de 2 à 6 et i=j-2
    diagonale à 5 cases (ij) 10 21 32 43 54 : j de 0 à 4 et i=j+1

    diagonale à 6 cases (ij) 01 12 23 34 45 56 : j de 1 à 6 et i=j-1
    diagonale à 6 cases (ij) 00 11 22 33 44 55 : j de 0 à 5 et i=j

    Optimisons : le compteur de base est j, les 3 autres sont fonction de j :

    diagonale à 4 cases (ij) 03 14 25 36 : j de 3 à 6 et i=j-3
    diagonale à 4 cases (kl) 20 31 42 53 : k=j-1 et l=i

    diagonale à 5 cases (ij) 02 13 24 35 46 : j de 2 à 6 et i=j-2
    diagonale à 5 cases (kl) 10 21 32 43 54 : k=j-1 et l=i

    diagonale à 6 cases (ij) 01 12 23 34 45 56 : j de 1 à 6 et i=j-1
    diagonale à 6 cases (kl) 00 11 22 33 44 55 : k=i et l=i
    """

    # test des 2 diagonales décroissantes à 4 cases :
    rouge=[0,0]
    bleu=[0,0]

    for j in range(3,7):
        i=j-3
        k=j-1
        l=i
        if grille[i][j]==1:
            rouge[0]+=1
            bleu[0]=0
            if rouge[0]>=4:
                trouve=1
                return trouve
        elif grille[i][j]==2:
            rouge[0]=0
            bleu[0]+=1
            if bleu[0]>=4:
                trouve=2
                return trouve
        else:
            rouge[0]=0
            bleu[0]=0

        if grille[k][l]==1:
            rouge[1]+=1
            bleu[1]=0
            if rouge[1]>=4:
                trouve=1
                return trouve
        elif grille[k][l]==2:
            rouge[1]=0
            bleu[1]+=1
            if bleu[1]>=4:
                trouve=2
                return trouve
        else:
            rouge[1]=0
            bleu[1]=0

    # test des 2 diagonales décroissantes à 5 cases :
    rouge=[0,0]
    bleu=[0,0]

    for j in range(2,7):
        i=j-2
        k=j-1
        l=i
        if grille[i][j]==1:
            rouge[0]+=1
            bleu[0]=0
            if rouge[0]>=4:
                trouve=1
                return trouve
        elif grille[i][j]==2:
            rouge[0]=0
            bleu[0]+=1
            if bleu[0]>=4:
                trouve=2
                return trouve
        else:
            rouge[0]=0
            bleu[0]=0

        if grille[k][l]==1:
            rouge[1]+=1
            bleu[1]=0
            if rouge[1]>=4:
                trouve=1
                return trouve
        elif grille[k][l]==2:
            rouge[1]=0
            bleu[1]+=1
            if bleu[1]>=4:
                trouve=2
                return trouve
        else:
            rouge[1]=0
            bleu[1]=0

    # test des 2 diagonales décroissantes à 6 cases :
    rouge=[0,0]
    bleu=[0,0]

    for j in range(1,7):
        i=j-1
        k=i
        l=i
        if grille[i][j]==1:
            rouge[0]+=1
            bleu[0]=0
            if rouge[0]>=4:
                trouve=1
                return trouve
        elif grille[i][j]==2:
            rouge[0]=0
            bleu[0]+=1
            if bleu[0]>=4:
                trouve=2
                return trouve
        else:
            rouge[0]=0
            bleu[0]=0

        if grille[k][l]==1:
            rouge[1]+=1
            bleu[1]=0
            if rouge[1]>=4:
                trouve=1
                return trouve
        elif grille[k][l]==2:
            rouge[1]=0
            bleu[1]+=1
            if bleu[1]>=4:
                trouve=2
                return trouve
        else:
            rouge[1]=0
            bleu[1]=0



    # si on n'a rien trouvé on retourne 0 :
    return trouve

# ############################################################################
# La fonction pions_rouges_alignes() teste si 2 ou 3 pions (n pions) rouges sont alignés dans la grille
# afin de savoir où l'ordinateur (joueur BLEU) doit jouer
# Si 3 pions sont alignés elle renvoie le numéro de la colonne suivante
# Si rien n'est trouvé elle renvoie -1
def pions_rouges_alignes(n):
    trouve=-1

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # teste 4 pions alignés horizontalement en alanysant chacune des 6 lignes :
    for i in range(6):
        rouge=0
        for j in range(7):
            if grille[i][j]==1:
                rouge+=1
                if rouge==n:
                    if i==5: # cas particulier de la première ligne
                        if j!=6 and grille[i][j+1]==0:
                            trouve=j+1
                            return trouve
                        elif j==6 and grille[i][j-n]==0:
                            trouve=j-n
                            return trouve
                    else: # une ligne haute
                        if j!=6 and grille[i][j+1]==0 and grille[i+1][j+1]!=0:
                            trouve=j+1
                            return trouve
                        elif j==6 and grille[i][j-n]==0 and grille[i+1][j-n]!=0:
                            trouve=j-n
                            return trouve

            else:
                rouge=0

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # teste 4 pions alignés verticalement en alanysant chacune des 7 colonnes :
    for j in range(7):
        rouge=0
        for i in range(6):
            if grille[5-i][j]==1:
                rouge+=1
                if rouge==n and grille[4-i][j]==0:
                    trouve=j
                    return trouve
            else:
                rouge=0

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # teste les 6 diagonales croissantes :

    # test des 2 diagonales croissantes à 4 cases :
    rouge=[0,0]

    for j in range(4):
        i=3-j
        k=i+2
        l=j+3
        if grille[i][j]==1:
            rouge[0]+=1
            if rouge[0]==n and i!=0 and grille[i-1][j+1]==0 and grille[i][j+1]!=0:
                trouve=j+1
                return trouve
        else:
            rouge[0]=0

        if grille[k][l]==1:
            rouge[1]+=1
            if rouge[1]==n and k!=0 and l!=6 and grille[k-1][l+1]==0 and grille[k][l+1]!=0:
                trouve=l+1
                return trouve
        else:
            rouge[1]=0

    # test des 2 diagonales croissantes à 5 cases :
    rouge=[0,0]

    for j in range(5):
        i=4-j
        k=i+1
        l=j+2
        if grille[i][j]==1:
            rouge[0]+=1
            if rouge[0]==n and i!=0 and grille[i-1][j+1]==0 and grille[i][j+1]!=0:
                trouve=j+1
                return trouve
        else:
            rouge[0]=0

        if grille[k][l]==1:
            rouge[1]+=1
            if rouge[1]==n and k!=0 and l!=6 and grille[k-1][l+1]==0 and grille[k][l+1]!=0:
                trouve=l+1
                return trouve
        else:
            rouge[1]=0

    # test des 2 diagonales croissantes à 6 cases :
    rouge=[0,0]

    for j in range(6):
        i=5-j
        k=i
        l=j+1
        if grille[i][j]==1:
            rouge[0]+=1
            if rouge[0]==n and i!=0 and grille[i-1][j+1]==0 and grille[i][j+1]!=0:
                trouve=j+1
                return trouve
        else:
            rouge[0]=0

        if grille[k][l]==1:
            rouge[1]+=1
            if rouge[1]==n and k!=0 and l!=6 and grille[k-1][l+1]==0 and grille[k][l+1]!=0:
                trouve=l+1
                return trouve
        else:
            rouge[1]=0

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # teste les 6 diagonales décroissantes :

    # test des 2 diagonales décroissantes à 4 cases :
    rouge=[0,0]

    for j in range(3,7):
        i=j-3
        k=j-1
        l=i
        if grille[i][j]==1:
            rouge[0]+=1
            if rouge[0]==n and i<=3 and j!=6 and grille[i+1][j+1]==0 and grille[i+2][j+1]!=0:
                trouve=j+1
                return trouve
        else:
            rouge[0]=0

        if grille[k][l]==1:
            rouge[1]+=1
            if rouge[1]==n and k<=3 and l!=6 and grille[k+1][l+1]==0 and grille[k+2][l+1]!=0:
                trouve=l+1
                return trouve
        else:
            rouge[1]=0

    # test des 2 diagonales décroissantes à 5 cases :
    rouge=[0,0]

    for j in range(2,7):
        i=j-2
        k=j-1
        l=i
        if grille[i][j]==1:
            rouge[0]+=1
            if rouge[0]==n and i<=3 and j!=6 and grille[i+1][j+1]==0 and grille[i+2][j+1]!=0:
                trouve=j+1
                return trouve
        else:
            rouge[0]=0

        if grille[k][l]==1:
            rouge[1]+=1
            if rouge[1]==n and k<=3 and l!=6 and grille[k+1][l+1]==0 and grille[k+2][l+1]!=0:
                trouve=l+1
                return trouve
        else:
            rouge[1]=0

    # test des 2 diagonales décroissantes à 6 cases :
    rouge=[0,0]

    for j in range(1,7):
        i=j-1
        k=i
        l=i
        if grille[i][j]==1:
            rouge[0]+=1
            if rouge[0]==n and i<=3 and j!=6 and grille[i+1][j+1]==0 and grille[i+2][j+1]!=0:
                trouve=j+1
                return trouve
        else:
            rouge[0]=0

        if grille[k][l]==1:
            rouge[1]+=1
            if rouge[1]==n and k<=3 and l!=6 and grille[k+1][l+1]==0 and grille[k+2][l+1]!=0:
                trouve=l+1
                return trouve
        else:
            rouge[1]=0

    # si on n'a rien trouvé on retourne -1 :
    return trouve

# ############################################################################
# La fonction tester_saisie demande au joueur de saisir un nombre entre 0 et 6,
# et réitère la demande tant que la valeur saisie n'ets pas un entier dans cet intervale
def tester_saisie():
    global grille,joueur_courant,tab_colonne
    if joueur_courant==1:
        joueur='ROUGE'
    else:
        joueur='BLEU'
        # le joueur 2 est remplacé par l'ordinateur qui renvoie ici un numéro de colonne entre 0 et 6

        # NIVEAU 1 : l'ordinateur recherche des pions rouges déjà alignés dans la grille

        # teste si 3 pions rouges sont alignés :
        prochain=pions_rouges_alignes(3)
        if prochain!=-1:
            if prochain<7:
                if tab_colonne[prochain]<6:
                    return prochain
            else:
                if tab_colonne[3]<6:
                    return 3

        # teste si 2 pions rouges sont alignés :
        if prochain!=-1:
            if prochain<7:
                if tab_colonne[prochain]<6:
                    return prochain
            else:
                if tab_colonne[4]<6:
                    return 4

        # NIVEAU 0 : l'ordinateur renvoie un numéro au hasard entre 0 et 6 en recherchant une colonne non pleine :
        n=random.randint(0,6)
        while tab_colonne[n]>=6:
            n=random.randint(0,6)
        return n

    saisie_correct=False
    # gestion des erreur et filtrage des entrées : demande une saisie jusqu'à ce que la valeur entrée soit un chiffre entre 0 et 6
    # Les messages d'erreurs orientant l'utilisateur sont affichés sur la sortie standard (sans provoquer d'erreur)
    while not saisie_correct:
        s_colonne=input("%s : entrez la colonne où jouer (de 0 à 6) :" % joueur)

        # commence par tester la saisie des commandes spéciales (f, s ou r) :
        if s_colonne.upper()=='F':
            # quitte le programme et ferme la fenêtre de la tortue si l'utilisateur saise f (comme fin)
            print("Fin du programme car l'utilisateur a saisie F")
            bye()
            exit()
        elif s_colonne.upper()=='S':
            # sauvegarde la sérialisation de la grille dans un fichier texte :
            fic=open('grille.txt','w')
            # convertit l'objet liste grile en chaine de caractères (sérialistation) :
            serialisation=str(grille)
            # enregistre la grille sur la première ligne du fichier grille.txt :
            fic.write(serialisation)
            fic.write('\n')
            # enregistre le joueur courant sur la deuxième ligne du fichier grille.txt :
            fic.write(str(joueur_courant))
            fic.close()
            print("\nL'état de la partie vient d'être enregistré dans le fichier grille.txt mais la partie continue.")
            print("C'est encore au joueur %s à jouer." % joueur)
        elif s_colonne.upper()=='R':
            if os.path.exists('grille.txt'):
                # restaure la grille et le joueur courant à partir du fichier texte grille.txt :
                fic=open('grille.txt','r')
                # fic est un itérateur pointant sur les lignes du fichier : on le convertit en liste
                ligne=list(fic)
                fic.close()
                # première ligne sans le \n : c'est la grille
                s_grille=ligne[0].strip()
                # deuxième ligne sans le \n : c'est le joueur courant
                s_joueur_courant=ligne[1].strip()
                # désérialisation des objets enregistrés en chaine de caractères :
                grille=eval(s_grille)
                joueur_courant=eval(s_joueur_courant)
                # ré-initialise la grille graphique dans la fenêtre de la tortue :
                reset()
                speed(0)
                hideturtle()
                dessiner_grille()
                # compte le nombre de pions dans chaque colonne et complète la grille graphique :
                tab_colonne=7*[0]
                for i in range(6):
                    for j in range(7):
                        if grille[i][j]!=0:
                            tab_colonne[j]+=1
                            dessiner_pion(j,5-i,grille[i][j])

                print('\n\n\n\n\n\n=============================================')
                print(' PUISSANCE 4 : FINIR UNE PARTIE')
                print('=============================================')
                if joueur_courant==1:
                    joueur='ROUGE'
                else:
                    joueur='BLEU'
                print("\nL'état de la partie vient d'être restaurée à partir du fichier grille.txt.")
                print("C'est au joueur %s à jouer." % joueur)
                afficher_grille()
            else:
                print("\nLe fichier grille.txt n'existe pas.")
                print("Avant de vouloir restaurer une partie avec la commande R il faut en sauvegarder une avec la commande S.")

        # teste si la chaine saise est un entier :
        elif not s_colonne.isdigit():
            print("Erreur de saise : la valeur entrée par le joueur %s n'est pas un nombre entier. Recommencez." % joueur)
        # teste si la valeur numérique est comprise entre 0 et 6 :
        elif int(s_colonne)<0 or int(s_colonne)>6:
            print("Erreur de saise : la valeur numérique entrée par le joueur %s n'est pas comprise entre 0 et 6. Recommencez." % joueur)
        else:
            saisie_correct=True
    # la chaine s_colonne est un chiffre entre 0 et 6 : on la convertit en entier et on la renvoie
    return int(s_colonne)


# ############################################################################
# La fonction jouer() demande au joueur courant dans quelle colonne (de 0 à 6) il veut jouer
def jouer():
    global joueur_courant
    joueur=["ROUGE","BLEU"]
    # La fonction tester_saisie renvoie forcément un chiffre entre 0 et 6 :
    colonne=tester_saisie()
    while tab_colonne[colonne]==6:
        print('La colonne %d est pleine ! %s jouez dans une colonne non pleine' % (colonne,joueur[joueur_courant-1]))
        colonne=tester_saisie()
    grille[5-tab_colonne[colonne]][colonne]=joueur_courant
    # dessine le pion sur la grille graphique :
    dessiner_pion(colonne,tab_colonne[colonne],joueur_courant)
    tab_colonne[colonne]+=1
    print('\nLe joueur %s vient de jouer dans la colonne %d :' % (joueur[joueur_courant-1],colonne))

# ############################################################################
# La fonction dessiner_grille() dessine une grille vide dans la fenêtre de la tortue
def dessiner_grille():
    up()
    goto(x_base,y_base)
    down()
    # traits horizontaux :
    for i in range(8):
        forward(7*largeur)
        up()
        goto(x_base,y_base+i*largeur)
        down()
    # traits verticaux :
    up()
    goto(x_base,y_base)
    setheading(90)
    down()
    for i in range(9):
        forward(6*largeur)
        up()
        goto(x_base+i*largeur,y_base)
        down()
    # affiche le numéro des colonnes sous la grille :
    for i in range(7):
        up()
        goto(x_base+i*largeur+largeur//2,y_base-largeur//2)
        down()
        write(str(i))

# ############################################################################
# La fonction dessiner_pion(x,y,couleur) ajoute un pion dans la case (x,y)
def dessiner_pion(x,y,couleur):
    # x de 0 à 6 et y de 0 à 5
    up()
    goto(x_base+(x+1)*largeur-largeur//8,y_base+(y+1)*largeur-largeur//2)
    down()
    if couleur==1:
        # pion ROUGE si couleur=1 :
        color('red')
    else:
        # pion BLEU si couleur=2 :
        color('blue')
    begin_fill()
    circle(largeur/2.5)
    end_fill()


# ############################################################################
#    P R O G R A M M E      P R I N C I P A L
# ############################################################################

# initialise l'affichage graphique de la grille :
largeur=60
x_base=-220
y_base=-150
setup(7*largeur+30, 430, 0, 0)
speed(0)
hideturtle()
dessiner_grille()

print('\n\n\n\n\n\n=============================================')
print(' PUISSANCE 4 : NOUVELLE PARTIE')
print('=============================================\n\n')
print("Avant de lancer le programme réduisez la fenêtre de Python sur la moitié droite de l'écran.")
print("La fenêtre de la tortue sera affichée dans le coin supérieur gauche de l'écran.\n\n")
print("Dans cette version le joueur BLEU est l'ordinateur. Vous êtes le joueur ROUGE.\n\n")
qui_commence()
print('Caractères particuliers à saisir à la place du numéro de la colonne à jouer :')
print('S : Sauvegarde la partie dans le fichier grille.txt')
print('R : Restaure la partie à partir du fichier grille.txt')
print('F : Fin du jeu (pour quitter le programme)')
print('\nLe nom des joueurs sera ici ROUGE et BLEU.')
if joueur_courant==1:
    print('Le joueur ROUGE commence.')
else:
    print('Le joueur BLEU commence.')
print('\nDébut de la partie (la grille est vide) :')
gagnant=0
while not grille_pleine() and gagnant==0:
    afficher_grille()
    jouer()
    joueur_courant=3-joueur_courant
    gagnant=pions_alignes()
    if gagnant==1:
        print('Bravo ! Le joueur ROUGE a gagné !')
    elif gagnant==2:
        print('Bravo ! Le joueur BLEU a gagné !')


afficher_grille()
if gagnant==0:
    print("Fin de la partie : la grille est pleine et il n'y a pas 4 pions alignés")
elif grille_pleine():
    print("Fin de la partie : 4 pions sont alignés et la grille est pleine")
else:
    print("Fin de la partie : 4 pions sont alignés et la grille n'est pas pleine")

done()

# ############################################################################
#    F I N     D U     P R O G R A M M E
# ############################################################################