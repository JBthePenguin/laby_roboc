def choix_laby(list_cartes):
	""" fonction qui demande au joueur de choisir son labyrinthe,
	qui valide le choix du labyrinthe:
	-- vérifie que le joueur a bien saisi un entier
	-- vérifie que le numéro saisi corespond bien à un labyrinthe dispo,
	et qui renvoie le nom du fichier correspondant"""

	numero_valide = False
	while numero_valide == False:
		laby_choisi = input("Entre le numéro du labyrinthe: ") # le joueur fait son choix
		try:
			int(laby_choisi)
			assert int(laby_choisi) > 0 and int(laby_choisi) <= len(list_cartes)
		except ValueError: # Attention, joueur pas très doué car il n'a pas saisi un entier
			print("\nAllons!!! On te demande un numéro, pas une lettre ou je ne sais quoi.\n Essaye encore...\n")
			numero_valide = False
		except AssertionError: # Attention, joueur qui ne sait pas compter car le numéro choisi n'est pas dans la liste
			print("\nCe labyrinthe n'existe pas!!!! Il faut choisir un numéro présent dans la liste.\n Essaye encore...\n")
			numero_valide = False
		else: # on valide le choix du joueur, ce qui ne veut pas dire que le joueur est malin, attention pour la suite
			numero_valide = True
		 
	laby_choisi = list_cartes[int(laby_choisi) - 1]
	return laby_choisi
	

def choix_direction_distance():
	""" fonction qui demande au joueur de choisir sa direction,
	qui valide le choix de la direction:
	-- vérifie que le joueur a bien saisi une des 4 lettres 's','n','e','o'
	-- vérifie que le joueur a saisi une distance correcte ( 1 pas par défaut)
	et qui renvoie la direction et la distance sous forme de tuple direction_distance = (direction, distance)"""

	direction_valide = False
	distance_valide = False
	while direction_valide == False or distance_valide == False:
		direction_distance = input("Direction (N)ord, (S)ud, (E)st, (O)uest + Distance ( par défaut 1 )\nexemple de saisie : S2 --> 2 pas vers le sud\n\nIndique ta direction et ta distance: ") 
		try:
			direction_distance[0]
		except IndexError: # Attention joueur sans initiative aucune
			print("\nAttention!!! Si on ne dit rien à Roboc, il ne fait rien.\n")
			direction_valide = False
			continue
		
		if direction_distance[0].upper() != "S" and direction_distance[0].upper() != "N" \
		and direction_distance[0].upper() != "E" and direction_distance[0].upper() != "O": # Attention joueur qui ne sait pas se servir d'une boussole
			print("\nAttention!!! La direction choisie n'est valide.\n ")
			direction_valide = False
		else:
			direction_valide =True

		distance = direction_distance[1:]
		if distance == "": # Attention joueur sans initiative, donc on choisit 1 pour lui
			distance = 1
			distance_valide = True
		else:
			try:
				distance = int(distance)
				assert int(distance) > 0
			except ValueError:# Attention joueur qui ne sait pas qu'un nombre de pas doit être un nombre 
				print("\nAttention!!! La distance n'est pas valide,  ça doit être un nombre.\n")
				distance_valide = False
			except AssertionError:# Attention joueur qui veut rester sur place ou reculer
				print("\nAttention!!! La distance ne peut être nulle ou négative.\n")
				distance_valide = False
			else:
				distance_valide = True

	direction = direction_distance[0].upper()
	distance = int(distance)
	direction_distance = (direction, distance)
	return direction_distance
