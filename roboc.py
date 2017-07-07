from fonctions import *
from classes import *
from cartes import carte_dispo

quitter_partie = False
while quitter_partie == False:
    print("\n Aide Roboc à sortir...\n ... du labyrinthe :")
    for i, elt in enumerate(carte_dispo.list_cartes):  # affichage de la liste des cartes dispos
        print("\n{} - {}".center(15).format(i+1, elt[0:-4].capitalize()))

    laby_choisi = choix_laby(carte_dispo.list_cartes) # le joueur choisit le labyrinthe...
    partie_en_cours = Partie(laby_choisi) # ... création de la partie en fonction du choix du labyrinthe -> classe Partie
    print(partie_en_cours) # ... affichage du labyrinthe choisi

    partie_gagnee = False
    while partie_gagnee == False:
        direction_distance = choix_direction_distance() # le joueur choisit sa direction et sa distance
        if direction_distance[0] == "Q": # le joueur choisit de quitter le jeu
            quitter_partie = True
            break
        else:
            partie_gagnee = partie_en_cours.deplacer_roboc(direction_distance) # ça joue!!!

    if partie_gagnee == True: # C'est gagné!!! on demande au joueur s'il veut rejouer ou quitter
        rejouer_quitter = input("q pour (Q)uitter et ce que tu veux pour rejouer: ")
        if rejouer_quitter.upper() == "Q": # il en a marre et quitte le jeu
            quitter_partie = True

print("\nBye!!! Bye!!! Bye!!!")

