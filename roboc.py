from fonctions import *
from classes import *
from cartes import carte_dispo 

print("\n Aide Roboc à sortir...\n ... du labyrinthe : \n") # message de début

for i, elt in enumerate(carte_dispo.list_cartes):  # affichage de la liste des cartes dispos
	print("{} - {}".center(15).format(i+1, elt[0:-4].capitalize()),"\n")

laby_choisi = choix_laby(carte_dispo.list_cartes) # le joueur choisit le labyrinthe... 

partie_en_cours = Carte(laby_choisi) # ... création en fonction du choix de la partie -> classe Carte
print(partie_en_cours) # ... affichage du labyrinthe

partie_gagnee = False
caractere_a_ajouter = " "
while partie_gagnee == False:
	direction_distance = choix_direction_distance() # le joueur choisit sa direction et sa distance
	partie = partie_en_cours.deplacer_roboc(caractere_a_ajouter, partie_gagnee, direction_distance) # roboc se déplacer
	partie_en_cours = partie[0]
	partie_gagnee = partie[2]
	caractere_a_ajouter = partie[1]
else:
	print("c'est fini!!!") # c'est gagné