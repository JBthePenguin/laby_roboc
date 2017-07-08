import pickle
from fonctions import *
from classes import *
from cartes import carte_dispo

quitter_partie = False
while quitter_partie == False:
    print("\n Aide Roboc à sortir...\n ... du labyrinthe :")
    for i, elt in enumerate(carte_dispo.list_cartes):  # affichage de la liste des cartes dispos
        print("\n{} - {}".center(15).format(i+1, elt[0:-4].capitalize()))

    sauvegarde_dispo = False
    try: # vérification si une sauvegarde est présente...
        sauvegarde = open("save", "rb")
    except FileNotFoundError:
        pass
    else: #...si le fichier save existe...
        with open("save", "rb") as fichier:
            sauvegarde = pickle.Unpickler(fichier)
            partie_sauvegardee = sauvegarde.load()
        if partie_sauvegardee != None: #...et qu'une partie est sauvegardée...
            sauvegarde_dispo = True

    if sauvegarde_dispo == True and partie_sauvegardee != None: #..., affichage dans la liste de choix
        print("\n{} - Partie en cours".format(len(carte_dispo.list_cartes)+1))
        laby_dispo = carte_dispo.list_cartes + [sauvegarde_dispo]
    else:
        laby_dispo = carte_dispo.list_cartes

    laby_choisi = choix_laby(laby_dispo) # le joueur choisit le labyrinthe...

    if laby_dispo[int(laby_choisi) - 1] == sauvegarde_dispo: #...sauvegardé...
        partie_en_cours = partie_sauvegardee
    else:
        partie_en_cours = Partie(laby_dispo[int(laby_choisi) - 1]) #...sinon création de la partie en fonction du choix -> classe Partie

    print(partie_en_cours) # ... affichage du labyrinthe choisi

    partie_gagnee = False
    while partie_gagnee == False:
        direction_distance = choix_direction_distance() # le joueur choisit sa direction et sa distance
        if direction_distance[0] == "Q": # le joueur choisit de quitter le jeu
            quitter_partie = True
            break
        else:
            partie_gagnee = partie_en_cours.deplacer_roboc(direction_distance) # ça joue!!!
            sauvegarder(partie_en_cours)

    if partie_gagnee == True: # C'est gagné!!! on demande au joueur s'il veut rejouer ou quitter
        partie_en_cours = None
        sauvegarder(partie_en_cours)
        rejouer_quitter = input("q pour (Q)uitter et ce que tu veux pour rejouer: ")
        if rejouer_quitter.upper() == "Q": # il en a marre et quitte le jeu
            quitter_partie = True

print("\nBye!!! Bye!!! Bye!!!")

