import time

class Partie():
    """docstring for Partie : classe d'objet avec les attributs:
    - self.affichage : labyrinthe qui s'affiche sous forme de chaine de caractères
    - self.nbre_ligne : nombre de lignes du labyrinthe -> y
    - self.nbre_caractere_par_ligne : nombre de caractères par ligne -> x
    - self.caractere_a_ajouter : caractère à ajouter à la place de Roboc (X) après un déplacement"""
    def __init__(self, nom_du_fichier):
        """fonction de construction de l'objet et de ses attributs
        prenant en paramètre le fichier contenant le labyrinthe (.txt)"""
        with open("cartes/{}".format(nom_du_fichier), "r") as labyrinthe_file:
            laby = labyrinthe_file.read()

        self.affichage = laby.strip()

        list_ligne_partie_en_cours = self.affichage.split("\n")
        self.nbre_ligne = len(list_ligne_partie_en_cours)

        nbre_caractere = len(self.affichage) + 1
        self.nbre_caractere_par_ligne = nbre_caractere // self.nbre_ligne

        self.caractere_a_ajouter = " "


    def __str__(self):
        """fonction d'affichage du labyrinthe -> print(self)"""
        return "\n{}\n".format(self.affichage)


    def deplacer_roboc(self, direction_distance):
        """fonction qui déplace Roboc (X) dans le labyrinthe
        prenant en paramètre la direction et la distance
        en vérifiant qu'il:
        - ne sort pas des limites du jeu
        - ne traverse pas les murs dans le jeu (O)
        qui affiche son déplacement pas à pas
        et qui renvoie True ou False à la fin du déplacement
        selon que la partie soit gagnée ou non"""
        list_chaine_avant_apres_x = self.affichage.split("X")    # on trouve roboc...
        chaine_avant_x = list_chaine_avant_apres_x[0] #...dans le labyrinthe...
        chaine_apres_x = list_chaine_avant_apres_x[1] #...et on lui donne...
        position_x = (len(chaine_avant_x) + 1) % (self.nbre_caractere_par_ligne) #...une position x...
        position_y = (len(chaine_avant_x) + 1) // (self.nbre_caractere_par_ligne) + 1 #...et une position y

        if direction_distance[0] == "S": # on trouve la future position...
            nvelle_position = (position_x, position_y + direction_distance[1])
        elif direction_distance[0] == "N": #...après le déplacement...
            nvelle_position = (position_x, position_y - direction_distance[1])
        elif direction_distance[0] == "O": #...en fonction de la direction...
            nvelle_position = (position_x - direction_distance[1], position_y)
        elif direction_distance[0] == "E": #...et de la distance choisies
            nvelle_position = (position_x + direction_distance[1], position_y)

        if nvelle_position[0] <= 0 or nvelle_position[0] >= self.nbre_caractere_par_ligne or nvelle_position[1] <= 0 or nvelle_position[1] > self.nbre_ligne: # Attention joueur sans limite, sûrement un rebel
            print("\nAttention!!! avec une telle distance dans cette direction, Roboc sort des limites de jeu.\n")
            print(self, "\n")
            return False
        else:
            caractere_a_ajouter_debut_deplacement = self.caractere_a_ajouter
            i = 1
            deplacement_affichage = self.affichage
            while i <= direction_distance[1]:
                if direction_distance[0] == "E": # déplacement vers la droite
                    caractere_a_remplacer = chaine_apres_x[0]
                    chaine_avant_x = chaine_avant_x + self.caractere_a_ajouter
                    chaine_apres_x = chaine_apres_x[1:]
                elif direction_distance[0] == "O": # déplacement vers la gauche
                    caractere_a_remplacer = chaine_avant_x[-1]
                    chaine_avant_x = chaine_avant_x[0:-1]
                    chaine_apres_x = self.caractere_a_ajouter + chaine_apres_x
                elif direction_distance[0] == "S": # déplacement vers le bas
                    caractere_a_remplacer = chaine_apres_x[self.nbre_caractere_par_ligne-1]
                    chaine_avant_x = chaine_avant_x + self.caractere_a_ajouter + chaine_apres_x[0:self.nbre_caractere_par_ligne-1]
                    chaine_apres_x = chaine_apres_x[self.nbre_caractere_par_ligne:]
                elif direction_distance[0] == "N": # déplacement vers le haut
                    caractere_a_remplacer = chaine_avant_x[-self.nbre_caractere_par_ligne]
                    chaine_apres_x = chaine_avant_x[(len(chaine_avant_x)-self.nbre_caractere_par_ligne)+1:] + self.caractere_a_ajouter + chaine_apres_x
                    chaine_avant_x = chaine_avant_x[:-self.nbre_caractere_par_ligne]

                if caractere_a_remplacer == "O": # Attention joueur qui croit pouvoir passer à travers les murs
                    print("\nAttention!!! Roboc n'est pas un fantôme mais un robot, il ne traverse pas les murs.\nRetour au point de départ!!!\n")
                    self.caractere_a_ajouter = caractere_a_ajouter_debut_deplacement
                    print(self) # Roboc remit à sa position avant le déplacement
                    return False
                elif caractere_a_remplacer == "U":
                    if i == direction_distance[1]: # Enfin un joueur digne de ce superbe jeu
                        deplacement_affichage = chaine_avant_x + "X" + chaine_apres_x
                        print("\n")
                        print(deplacement_affichage)
                        print("\n!!! GAGNE !!!\n".center(30))
                        self.affichage = deplacement_affichage
                        return True
                    else: # Attention joueur aveugle qui passe devant la sortie sans s'arrêter
                        deplacement_affichage = chaine_avant_x + "X" + chaine_apres_x
                        print("\n")
                        print(deplacement_affichage)
                        self.caractere_a_ajouter = "U"
                        time.sleep(1)
                        i += 1
                elif caractere_a_remplacer == ".": # Attention que le joueur n'embarque pas la porte
                    deplacement_affichage = chaine_avant_x + "X" + chaine_apres_x
                    print("\n")
                    print(deplacement_affichage)
                    self.caractere_a_ajouter = "."
                    time.sleep(1)
                    i += 1
                else: # La voie est libre
                    deplacement_affichage = chaine_avant_x + "X" + chaine_apres_x
                    print("\n")
                    print(deplacement_affichage)
                    self.caractere_a_ajouter = " "
                    time.sleep(1)
                    i += 1

            self.affichage = deplacement_affichage
            return False
