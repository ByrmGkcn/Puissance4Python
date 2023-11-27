import time
from objets import joueur
def Verif(grille : list[list[str]], menu : int, j1:joueur, j2:joueur) -> bool :
    """
    Fonction permettant de vérifier si la partie est terminée ou non
    Entrée : grille de Puissance 4, choix du mode de jeu, nom du joueur s'il y en a un, score
    Sortie : booléen indiquant si la partie est terminée ou non
    """
    #déclaration et initialisation des variables
    fin : bool
    fin = False
    compteur : int
    compteur1 : int
    compteur2 :int
    compteur3 : int
    #on vérifie ensuite chaque ligne, colonne et diagonale pour voir s'il n'y a pas 4 jetons alignés côte à côte 
    compteur = 13
    while compteur > 2 and not fin :
        compteur1 = 1
        while compteur1<14 and not fin :
            if grille[compteur][compteur1]== grille[compteur-2][compteur1] == grille[compteur-4][compteur1] == grille[compteur - 6][compteur1] and grille[compteur][compteur1] !='   ':
                #le booléen fin prend la valeur 'True' pour indiquer que la partie est terminée
                fin = True
                for compteur2 in range(0,15):
                    for compteur3 in range(0,15) :
                        #on affiche les 4 jetons alignés en vert pour indiquer où se finit la partie 
                        if compteur == compteur2 and compteur1 == compteur3 :
                            print("\33[1;32;42m", '  ',end="") 
                            print("\33[1;37;40m",end="")
                        elif compteur-2 ==compteur2 and compteur1 == compteur3 :
                            print("\33[1;32;42m", '  ',end="")
                            print("\33[1;37;40m",end="")
                        elif compteur-4 ==compteur2 and compteur1 == compteur3 :
                            print("\33[1;32;42m", '  ',end="")
                            print("\33[1;37;40m",end="")
                        elif compteur-6 ==compteur2 and compteur1 == compteur3 :
                            print("\33[1;32;42m", '  ',end="")
                            print("\33[1;37;40m",end="")
                        elif grille[compteur2][compteur3] == ' r ' :
                            print("\33[1;31;41m", '  ',end="")
                            print("\33[1;37;40m",end="")
                        elif grille[compteur2][compteur3] == ' y ' :
                            print("\33[1;33;43m", '  ',end="")
                            print("\33[1;37;40m",end="")
                        else :
                            print(grille[compteur2][compteur3], end='')
                    print()
            if compteur1 < 8 :
                if grille[compteur][compteur1] == grille[compteur][compteur1 + 2] == grille[compteur][compteur1 + 4] == grille[compteur][compteur1 + 6] and grille[compteur][compteur1] !='   '  :
                    fin = True
                    for compteur2 in range(0,15):
                        for compteur3 in range(0,15) :
                            if compteur == compteur2 and compteur1 == compteur3 :
                                print("\33[1;32;42m", '  ',end="") 
                                print("\33[1;37;40m",end="")
                            elif compteur ==compteur2 and compteur1+2 == compteur3 :
                                print("\33[1;32;42m", '  ',end="")
                                print("\33[1;37;40m",end="")
                            elif compteur ==compteur2 and compteur1 +4== compteur3 :
                                print("\33[1;32;42m", '  ',end="")
                                print("\33[1;37;40m",end="")
                            elif compteur==compteur2 and compteur1 +6== compteur3 :
                                print("\33[1;32;42m", '  ',end="")
                                print("\33[1;37;40m",end="")
                            elif grille[compteur2][compteur3] == ' r ' :
                                print("\33[1;31;41m", '  ',end="")
                                print("\33[1;37;40m",end="")
                            elif grille[compteur2][compteur3] == ' y ' :
                                print("\33[1;33;43m", '  ',end="")
                                print("\33[1;37;40m",end="")
                            else :
                                print(grille[compteur2][compteur3], end='')
                        print() 
                if grille[compteur][compteur1] == grille[compteur -2][compteur1 +2] == grille[compteur-4][compteur1+4] == grille[compteur-6][compteur1+6] and grille[compteur][compteur1] != '   ' :
                    fin = True
                    for compteur2 in range(0,15):
                        for compteur3 in range(0,15) :
                            if compteur == compteur2 and compteur1 == compteur3 :
                                print("\33[1;32;42m", '  ',end="") 
                                print("\33[1;37;40m",end="")
                            elif compteur-2 ==compteur2 and compteur1+2 == compteur3 :
                                print("\33[1;32;42m", '  ',end="")
                                print("\33[1;37;40m",end="")
                            elif compteur-4 ==compteur2 and compteur1+4 == compteur3 :
                                print("\33[1;32;42m", '  ',end="")
                                print("\33[1;37;40m",end="")
                            elif compteur-6 ==compteur2 and compteur1+6 == compteur3 :
                                print("\33[1;32;42m", '  ',end="")
                                print("\33[1;37;40m",end="")
                            elif grille[compteur2][compteur3] == ' r ' :
                                print("\33[1;31;41m", '  ',end="")
                                print("\33[1;37;40m",end="")
                            elif grille[compteur2][compteur3] == ' y ' :
                                print("\33[1;33;43m", '  ',end="")
                                print("\33[1;37;40m",end="")
                            else :
                                print(grille[compteur2][compteur3], end='')
                        print()
            if compteur1 > 6 :
                if grille[compteur][compteur1] == grille[compteur-2][compteur1-2] == grille[compteur-4][compteur1-4] == grille[compteur-6][compteur1-6] and grille[compteur][compteur1] != '   ' :
                    fin = True
                    for compteur2 in range(0,15):
                        for compteur3 in range(0,15) :
                            if compteur == compteur2 and compteur1 == compteur3 :
                                print("\33[1;32;42m", '  ',end="") 
                                print("\33[1;37;40m",end="")
                            elif compteur-2 ==compteur2 and compteur1-2 == compteur3 :
                                print("\33[1;32;42m", '  ',end="")
                                print("\33[1;37;40m",end="")
                            elif compteur-4 ==compteur2 and compteur1-4 == compteur3 :
                                print("\33[1;32;42m", '  ',end="")
                                print("\33[1;37;40m",end="")
                            elif compteur-6 ==compteur2 and compteur1-6 == compteur3 :
                                print("\33[1;32;42m", '  ',end="")
                                print("\33[1;37;40m",end="")
                            elif grille[compteur2][compteur3] == ' r ' :
                                print("\33[1;31;41m", '  ',end="")
                                print("\33[1;37;40m",end="")
                            elif grille[compteur2][compteur3] == ' y ' :
                                print("\33[1;33;43m", '  ',end="")
                                print("\33[1;37;40m",end="")
                            else :
                                print(grille[compteur2][compteur3], end='')
                        print()
            #si le jeu est fini, on affiche le vainqueur
            if fin :
                if grille[compteur][compteur1]==' r ' :
                    print('Victoire de',j1.nom ,'(rouge) ')
                    j1.score=j1.score+1
                else :
                    print('Victoire de',j2.nom,' (jaune) ')
                    j2.score=j2.score+1
            compteur1 = compteur1 + 2
        compteur = compteur - 2
    
    return fin

import random
def JouerBot(caseLibre : list[int], grille: list[list[str]]) ->int:
    """
    Fonction permettant à l'ordinateur de choisir sa case de façon plus ou moins intelligente
    Entrée : Liste des cases libres, grille du Puissance 4
    Sortie : choix du bot
    """
    #déclaration et initialisation des variables
    choix : int
    joue : bool
    joue = False
    compteur : int
    compteur1 :int
    compteur = 13
    #on vérifie s'il y a possibilités de finir la partie ou d'empêcher l'adversaire de finir
    while compteur > 2 and not joue :
        compteur1 = 1
        while compteur1<14 and not joue :
            #on vérifie les colonnes
            if grille[compteur][compteur1]== grille[compteur-2][compteur1] == grille[compteur-4][compteur1]  and grille[compteur-6][compteur1] =='   ' and grille[compteur][compteur1] !='   ' :
                choix = (compteur1+1)//2
                #print(choix, 'ici') pour les jeux d'essais
                joue = True
            if compteur1+6 < 14 :
                #puis les diagonales
                if grille[compteur][compteur1]== grille[compteur-2][compteur1+2] == grille[compteur-4][compteur1+4]  and grille[compteur-6][compteur1+6] =='   ' and grille[compteur-4][compteur1+6] !='   'and grille[compteur-4][compteur1+4]!='   ':
                    choix = (compteur1+7)//2
                    #print(choix, 'ici') pour les jeux d'essais
                    joue = True
                if grille[compteur][compteur1]== grille[compteur-6][compteur1+6] == grille[compteur-4][compteur1+4]  and grille[compteur-2][compteur1+2] =='   ' and grille[compteur][compteur1+2] !='   ' and grille[compteur-4][compteur1+4]!='   ':
                    choix = (compteur1+3)//2
                    #print(choix, 'ici') pour les jeux d'essais
                    joue = True
                if grille[compteur][compteur1]== grille[compteur-6][compteur1+6] == grille[compteur-2][compteur1+2]  and grille[compteur-4][compteur1+4] =='   ' and grille[compteur-2][compteur1+4] !='   ' and grille[compteur-2][compteur1+2]!='   ':
                    choix = (compteur1+5)//2
                    #print(choix, 'ici') pour les jeux d'essais
                    joue = True
                if compteur<13 :
                    if grille[compteur-2][compteur1+2] == grille[compteur-4][compteur1+4] == grille[compteur-6][compteur1+6] and grille[compteur][compteur1] == '   ' and grille[compteur+2][compteur1]!='   ' and grille[compteur-2][compteur1+2]!='   ' :
                        choix = (compteur1+1)//2
                        #print(choix, 'ici') pour les jeux d'essais
                        joue = True
                    #on teste les lignes et les diagonales
                    if grille[compteur][compteur1+6] == grille[compteur][compteur1+2] == grille[compteur][compteur1+4] and grille[compteur][compteur1+2] !='   ' and grille[compteur][compteur1] == '   ' and grille[compteur+2][compteur1]!='   ':
                        choix = (compteur1+1)//2
                        #print(choix, 'ici') pour les jeux d'essais
                        joue = True
                    if grille[compteur][compteur1] == grille[compteur][compteur1+2] == grille[compteur][compteur1+4] and grille[compteur][compteur1] !='   ' and grille[compteur][compteur1+6] == '   ' and grille[compteur+2][compteur1+6]!='   ':
                        choix = (compteur1+7)//2
                        #print(choix, 'ici') pour les jeux d'essais
                        joue = True
                    if grille[compteur][compteur1] == grille[compteur][compteur1+2] == grille[compteur][compteur1+6] and grille[compteur][compteur1] !='   ' and grille[compteur][compteur1+4] == '   ' and grille[compteur+2][compteur1+4]!='   ':
                        choix = (compteur1+5)//2
                        #print(choix, 'ici') pour les jeux d'essais
                        joue = True
                    if grille[compteur][compteur1] == grille[compteur][compteur1+6] == grille[compteur][compteur1+4] and grille[compteur][compteur1] !='   ' and grille[compteur][compteur1+2] == '   ' and grille[compteur+2][compteur1+2]!='   ':
                        choix = (compteur1+3)//2
                        #print(choix, 'ici') pour les jeux d'essais
                        joue = True
                else :
                    if grille[compteur-2][compteur1+2] == grille[compteur-4][compteur1+4] == grille[compteur-6][compteur1+6] != '   'and grille[compteur][compteur1] == '   ' :
                        choix = (compteur1+1)//2
                        #print(choix, 'ici') pour les jeux d'essais
                        joue = True
                    if grille[compteur][compteur1+6] == grille[compteur][compteur1+2] == grille[compteur][compteur1+4] and grille[compteur][compteur1+2] !='   ' and grille[compteur][compteur1] == '   ' :
                        choix = (compteur1+1)//2
                        #print(choix, 'ici') pour les jeux d'essais
                        joue = True
                    if grille[compteur][compteur1] == grille[compteur][compteur1+2] == grille[compteur][compteur1+4] and grille[compteur][compteur1] !='   ' and grille[compteur][compteur1+6] == '   ' :
                        choix = (compteur1+7)//2
                        #print(choix, 'ici') pour les jeux d'essais
                        joue = True
                    if grille[compteur][compteur1] == grille[compteur][compteur1+2] == grille[compteur][compteur1+6] and grille[compteur][compteur1] !='   ' and grille[compteur][compteur1+4] == '   ' :
                        choix = (compteur1+5)//2
                        #print(choix, 'ici') pour les jeux d'essais
                        joue = True
                    if grille[compteur][compteur1] == grille[compteur][compteur1+6] == grille[compteur][compteur1+4] and grille[compteur][compteur1] !='   ' and grille[compteur][compteur1+2] == '   ' :
                        choix = (compteur1+3)//2
                        #print(choix, 'ici') pour les jeux d'essais
                        joue = True
            if compteur1-6>0 :
                #on teste l'autre type de diagonales
                if grille[compteur][compteur1]== grille[compteur-2][compteur1-2] == grille[compteur-4][compteur1-4]  and grille[compteur-6][compteur1-6] =='   ' and grille[compteur-4][compteur1-6] !='   'and grille[compteur-4][compteur1-4]!='   ':
                    choix = (compteur1-5)//2
                    #print(choix, 'ici') pour les jeux d'essais
                    joue = True
                if grille[compteur][compteur1]== grille[compteur-6][compteur1-6] == grille[compteur-4][compteur1-4]  and grille[compteur-2][compteur1-2] =='   ' and grille[compteur][compteur1-2] !='   ' and grille[compteur-4][compteur1-4]!='   ':
                    choix = (compteur1-1)//2
                    #print(choix, 'ici') pour les jeux d'essais
                    joue = True
                if grille[compteur][compteur1]== grille[compteur-6][compteur1-6] == grille[compteur-2][compteur1-2]  and grille[compteur-4][compteur1-4] =='   ' and grille[compteur-2][compteur1-4] !='   ' and grille[compteur-2][compteur1-2]!='   ':
                    choix = (compteur1-3)//2
                    #print(choix, 'ici') pour les jeux d'essais
                    joue = True
                if compteur<13 :
                    if grille[compteur-2][compteur1-2] == grille[compteur-4][compteur1-4] == grille[compteur-6][compteur1-6] and grille[compteur][compteur1] == '   ' and grille[compteur+2][compteur1]!='   ' and grille[compteur-2][compteur1-2]!='   ' :
                        choix = (compteur1+1)//2
                        #print(choix, 'ici') pour les jeux d'essais
                        joue = True
                else :
                    if grille[compteur-2][compteur1-2] == grille[compteur-4][compteur1-4] == grille[compteur-6][compteur1-6] != '   'and grille[compteur][compteur1] == '   ' :
                        choix = (compteur1+1)//2
                        #print(choix, 'ici') pour les jeux d'essais
                        joue = True
            compteur1 = compteur1 + 2
        compteur = compteur - 2
    #si il n'y a pas possibilité de finir ou empêcher de finir, on joue au hasard
    if not joue :
        choix = random.choice(caseLibre)
        #print('hasard') pour les jeux d'essais
    #comme il y a chaque case libre dans la liste, il faut ramener le numéro de la case au numéro de la colonne. 
    while choix > 7 or choix < 1 :
        choix = choix - 7
    #print(choix) cela permet de savoir dans les jeux d'essais quelle case est choisie
    #puis on retourne le choix
    time.sleep(1.5)
    return choix



def Puissance(grille : list[list[str]], menu : int, j1:joueur, j2:joueur, difficulté : int) :
    """
    Procédure permettant de jouer au Puissance 4, que ce soit en joueur contre ordinateur ou ordinateur contre lui-même
    Entrée : grille du Puissance 4, choix du mode de Puissance 4, score
    Sortie : rien
    """
    #déclaration et initialisation des variables
    colonne : int
    colonnetest : int
    ligne : int
    plein : bool
    fin : bool
    fin = False
    trouve : bool
    compteur1 : int
    compteur2 : int
    compteur = 0
    compteur3 : int
    caseLibre : list[int]
    caseLibre = [] 
    proba : int
    chance : int
    #on détermine les probas en fonction de la difficulté
    if difficulté == 1 :
        proba = 50
    elif difficulté ==2 : 
        proba = 90
    else :
        print('Erreur, difficulté Normal choisi')
        proba = 50
    #on crée une liste contenant toutes les cases libres de la grille pour aider le bot à choisir sa case
    for compteur3 in range(0,42) :
        caseLibre.append(compteur3+1)
    #on joue tant que ce n'est pas fini
    while compteur <42 and not fin :
        if compteur%2==0 :
            #on saisie la case en fonction du mode de jeu
            if menu == 2 or menu== 4:
                colonne = int(input( j1.nom + ", dans quelle colonne jouer ? "))
            else :
                colonne = JouerBot(caseLibre, grille)
            plein = True
            #on en déduit ensuite la place de la colonne dans la grille
            if colonne == 1 :
                    colonnetest = 1
            else :
                colonnetest = 2*colonne -1
            #si la colonne est pleine, on affiche une erreur
            if grille[3][colonnetest] != '   ' :
                print("Erreur, colonne pleine.")
            else :
                #sinon, on rempli la case libre la plus basse de la colonne 
                ligne = 13
                while ligne>=3  and plein :
                    if grille[ligne][colonnetest] == '   ' :
                        grille[ligne][colonnetest] = ' r '
                        plein = False
                    else : 
                        ligne = ligne - 2
                compteur = compteur + 1
        else :
            #on fait la même chose pour le deuxième joueur
            #on détermine la proba de jouer au hasard en fonction de la difficulté chosie
            chance = random.randint(1,100)
            #print(chance) pour jeux d'essais
            if chance > proba and (menu == 2 or menu==3) :
                colonne = random.choice(caseLibre)
                while colonne > 7 or colonne < 1 :
                    colonne = colonne - 7
                print('Mince !')
            else :
                colonne = JouerBot(caseLibre, grille)
            plein = True
            if colonne == 1 :
                    colonnetest = 1
            else :
                colonnetest = 2*colonne -1
            if grille[3][colonnetest] != '   ' :
                print("Erreur, colonne pleine.")
            else :
                ligne = 13
                while ligne>=3  and plein :
                    if grille[ligne][colonnetest] == '   ' :
                        grille[ligne][colonnetest] = ' y '
                        plein = False
                    else : 
                        ligne = ligne - 2
                compteur = compteur + 1
        #puis on appelle la fonction qui vérifie si la partie est terminée ou non
        fin = Verif(grille,menu,j1,j2)
        #si la partie n'est pas terminée, on affiche la grille modifiée
        if not fin :
            for compteur2 in range(0,15):
                for compteur1 in range(0,15) :
                    if grille[compteur2][compteur1] == ' r ' :
                        print("\33[1;31;41m", '  ',end="")
                        print("\33[1;37;40m",end="")
                    elif grille[compteur2][compteur1] == ' y ' :
                        print("\33[1;33;43m", '  ',end="")
                        print("\33[1;37;40m",end="")
                    else :
                        print(grille[compteur2][compteur1], end='')
                print()
        #puis on retire la case saisie de la liste des cases libres
        compteur2 =0        
        trouve = False
        while compteur2 < 6 and not trouve:
            if compteur2*7+colonne in caseLibre :
                caseLibre.remove(compteur2*7+colonne)
                trouve = True
            compteur2 = compteur2 + 1

                

def Grille(j1:joueur,j2:joueur,mode:int) :
    """
    Procédure permettant de crée une grille pour jouer au Puissance 4
    Entrée : score, choix du mode de Puissance 4
    Sortie : rien en soit
    """
    #déclaration et initialisation des variables
    grille : list[list[str]]
    grille = list([])
    compteur : int
    compteur1 : int
    compteur2 : int
    compteur2 = 1
    element : str
    diff:int
    #on crée la grille de Puissance 4
    for compteur in range(0,15) :
        ligne : list[str]
        ligne = []
        if compteur%2==0 :
            for compteur1 in range(0,15) :
                if compteur1%2 == 0 :
                    ligne.append('-')
                else :
                    ligne.append('---')
        else :
            for compteur1 in range(0,15) :
                if compteur1%2==0 :
                    ligne.append('|')
                else  :
                    if compteur == 1 :
                        element = ' ' + str(compteur2) + ' '
                        ligne.append(element)
                    else :
                        ligne.append('   ')
                    compteur2 = compteur2 + 1
        grille.append(ligne)
    #puis on affiche la grille
    for compteur in range(0,15):
        for compteur1 in range(0,15) :
            print(grille[compteur][compteur1], end='')
        print()
    #si un des deux joueurs machines est intelligent
    if j1.typo=="Robot" and j2.typo=="Robot":
        if j1.mode=="Intelligent" or j2.mode=="Intelligent":
            diff=2
        else :
            diff=1
    elif j1.typo=="Robot":
        if j1.mode=="Intelligent":
            diff=2
        else:
            diff=1
    elif j2.typo=="Robot":
        if j2.mode=="Intelligent":
            diff=2
        else :
            diff=1
    else :
        diff=1
    print()
    #enfin, on lance la procédure du jeu
    Puissance(grille, mode, j1, j2, diff)