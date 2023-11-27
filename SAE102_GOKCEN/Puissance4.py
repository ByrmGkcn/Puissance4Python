from objets import joueur


def Verif(grille : list[list[str]], j1:joueur, j2:joueur) -> bool :
    """
    Fonction permettant de vérifier si la partie est terminée ou non
    Entrée : grille de Puissance 4, nom des Joueurs, score
    Sortie : Booléen indiquant si la partie est terminée
    """
    #déclaration et initialisation des variables
    fin : bool
    fin = False
    compteur : int 
    compteur1 : int
    compteur2 : int
    compteur3 : int
    """#on vérifie que la colonne du jeux existe dans le fichier des scores, sinon on la crée
    for compteur in range(0,len(score[0])) :
        if score[0][compteur] == "Puissance 4" :
            colonne = compteur
        if compteur == len(score[0]) -1 and colonne == -1 :
            score[0].append('Puissance 4')
            colonne = compteur +1"""
    #on vérifie s'il y a 4 jetons alignés quelque part dans la grille
    #on part de compteur = 13 car ça correspond à la ligne la plus basse
    compteur = 13
    while compteur > 2 and not fin :
        compteur1 = 1
        while compteur1<14 and not fin :
            #on vérifie donc les jetons
            if grille[compteur][compteur1]== grille[compteur-2][compteur1] == grille[compteur-4][compteur1] == grille[compteur - 6][compteur1] and grille[compteur][compteur1] !='   ':
                #s'il y a un alignement des 4 jetons, le booléen fin prend la valeur True pour finir la partie
                fin = True
                for compteur2 in range(0,15):
                    for compteur3 in range(0,15) :
                        #s'il y en a 4 d'alignés, on les affiche en vert pour voir où la partie se finit
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
                        #on affiche tout le reste dans la bonne couleur
                        elif grille[compteur2][compteur3] == ' r ' :
                            print("\33[1;31;41m", '  ',end="")
                            print("\33[1;37;40m",end="")
                        elif grille[compteur2][compteur3] == ' y ' :
                            print("\33[1;33;43m", '  ',end="")
                            print("\33[1;37;40m",end="")
                        else :
                            print(grille[compteur2][compteur3], end='')
                    print()
            #on continue pour tous les alignements possibles
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
            #si la partie est finie, on affiche le vainqueur
            if fin :
                if grille[compteur][compteur1]==' r ' :
                    print('Victoire de', j1.nom, '(rouge). Il gagne 1 point !')
                    j1.score=j1.score+1
                else :
                    print('Victoire de', j2.nom, '(jaune). Il gagne 1 point !')
                    j2.score=j2.score+1
                compteur = 0
            compteur1 = compteur1 + 2
        compteur = compteur - 2
    
    return fin


def Puissance4(grille : list[list[str]], j1:joueur, j2:joueur) :
    """
    Procédure permettant à deux joueurs de s'affronter sur le jeu Puissance 4
    Entrée : grille de Puissance 4, joueurs
    Sortie : Rien
    """
    #déclaration et initialisation des variables
    colonne : int
    colonnetest : int
    plein : bool
    ligne : int
    fin : bool
    fin = False
    compteur1 : int
    compteur2 : int
    compteur : int
    compteur = 0
    #on joue tant qu'il reste des cases libres et qu'il n'y a pas de ligne de quatre
    while compteur <42 and not fin :
        if compteur%2==0 :
            #le joueur choisit sa colonne
            colonne = int(input(j1.nom + ",dans quelle colonne voulez-vous jouer ? "))
            plein = True
            #on vérifie si la colonne n'est pas pleine
            if colonne == 1 :
                    colonnetest = 1
            else :
                colonnetest = 2*colonne -1
            if grille[3][colonnetest] != '   ' :
                print("Erreur, colonne pleine.")
            #sinon on modifie la case libre la plus basse de la colonne choisie
            else :
                ligne = 13
                while ligne>=3  and plein :
                    if grille[ligne][colonnetest] == '   ' :
                        grille[ligne][colonnetest] = ' r '
                        plein = False
                    else : 
                        ligne = ligne - 2
                compteur = compteur + 1
        else :
            #même chose pour le second joueur
            colonne = int(input(j2.nom + ",dans quelle colonne voulez-vous jouer ? "))
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
        #après chaque tour, on vérifie que la partie n'est pas finie
        fin = Verif(grille, j1,j2)
        #si la partie n'est pas finie, on affiche la grille avec les modifications
        if not fin :
            for compteur2 in range(0,15):
                for compteur1 in range(0,15) :
                    #on affiche les couleurs en fonction de la case
                    if grille[compteur2][compteur1] == ' r ' :
                        print("\33[1;31;41m", '  ',end="")
                        print("\33[1;37;40m",end="")
                    elif grille[compteur2][compteur1] == ' y ' :
                        print("\33[1;33;43m", '  ',end="")
                        print("\33[1;37;40m",end="")
                    else :
                        print(grille[compteur2][compteur1], end='')
                print()

                
                

def GrilleP4(j1:joueur,j2:joueur) :
    """
    Procédure permettant de créer une grille pour jouer au Puissance4
    Entrée : joueurs
    Sortie : Rien
    """
    #déclaration et initialisation des variables
    grille : list[list[str]]
    grille = []
    compteur2 : int
    compteur2 = 1
    element : str
    compteur : int
    compteur1 : int
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
    #on affiche ensuite la grille une fois quelle est créée
    for compteur in range(0,15):
        for compteur1 in range(0,15) :
            print(grille[compteur][compteur1], end='')
        print()
    #puis on lance le programme pour jouer
    Puissance4(grille,j1,j2)


def ChoixP4(j1:joueur,j2:joueur) :
    """
    Procédure permettant de lancer les fonctions et procédures nécessaires pour jouer au mode choisi par l'utilisateur
    Entrée : joueurs
    Sortie : rien en soit
    """
    #déclaration et saisie de la variable menu 
    mode : int
    if j1.typo=="Humain" and j2.typo=="Humain":
        mode=1
    elif j1.typo=="Humain" and j2.typo=="Robot":
        mode=2
    elif j2.typo=="Humain" and j1.typo=="Robot":
        mode=4    
    else :
        mode=3
    
    if mode == 1 :
        GrilleP4(j1,j2)
    elif mode == 2 or mode == 3: 
        from Puissance4Bot import Grille
        Grille(j1,j2,mode)
    elif mode == 4: 
        from Puissance4Bot import Grille
        Grille(j2,j1,mode)