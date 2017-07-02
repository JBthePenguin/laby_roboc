class Carte():
	"""docstring for Carte : classe qui produit
	des cartes de labyrinthe qui s'affiche
	sous forme de chaine de caractères """
	def __init__(self, nom_du_fichier):
		with open("cartes/{}".format(nom_du_fichier), "r") as labyrinthe_file:
			laby = labyrinthe_file.read()

		self.affichage = laby.strip()

		list_ligne_partie_en_cours = self.affichage.split("\n")
		self.nbre_ligne = len(list_ligne_partie_en_cours)

		nbre_caractere = len(self.affichage) + 1
		self.nbre_caractere_par_ligne = nbre_caractere // self.nbre_ligne

	
	def __str__(self):
		""" la fonction d'affichage pour print"""
		return "\n{}\n".format(self.affichage)


	def deplacer_roboc(self, caractere_a_ajouter, partie_gagnee, direction_distance):
		"""Fonction qui vérifie si roboc ne sort pas des limites, qui affiche le déplacement de roboc pas à pas 
		et qui renvoie , la partie en cours après le déplacement, le caractère à ajouter à la place de roboc
		lors du déplacement suivant et une variable "booléen" partie_gagnee"""
		list_chaine_avant_apres_x = self.affichage.split("X")	# on trouve roboc...
		chaine_avant_x = list_chaine_avant_apres_x[0]
		chaine_apres_x = list_chaine_avant_apres_x[1]
		position_x = (len(chaine_avant_x) + 1) % (self.nbre_caractere_par_ligne) # ...et on lui donne...
		position_y = (len(chaine_avant_x) + 1) // (self.nbre_caractere_par_ligne) + 1 #... une position xy

		if direction_distance[0] == "S": # on trouve la future position...
			nvelle_position = (position_x, position_y + direction_distance[1])
		elif direction_distance[0] == "N": #...après le déplacement...
			nvelle_position = (position_x, position_y - direction_distance[1])
		elif direction_distance[0] == "O": #...pour chacune des directions
			nvelle_position = (position_x - direction_distance[1], position_y)
		elif direction_distance[0] == "E":
			nvelle_position = (position_x + direction_distance[1], position_y)
		
		if nvelle_position[0] <= 0 or nvelle_position[0] >= self.nbre_caractere_par_ligne or nvelle_position[1] <= 0 or nvelle_position[1] > self.nbre_ligne: # Attention joueur sans limite, sûrement un rebel
			print("\nAttention!!! avec une telle distance dans cette direction, Roboc sort des limites de jeu.\n")
			print(self, "\n")
			return (self, caractere_a_ajouter, partie_gagnee)
		else:
			caractere_a_ajouter_debut = caractere_a_ajouter
			i = 1
			deplacement_affichage = self.affichage	
			while i <= direction_distance[1]:
				if direction_distance[0] == "E": # déplacement vers la droite
					caractere_a_remplacer = chaine_apres_x[0]
					chaine_avant_x = chaine_avant_x + caractere_a_ajouter
					chaine_apres_x = chaine_apres_x[1:]	
				elif direction_distance[0] == "O": # déplacement vers la gauche
					caractere_a_remplacer = chaine_avant_x[-1]
					chaine_avant_x = chaine_avant_x[0:-1]
					chaine_apres_x = caractere_a_ajouter + chaine_apres_x	
				elif direction_distance[0] == "S": # déplacement vers le bas
					caractere_a_remplacer = chaine_apres_x[self.nbre_caractere_par_ligne-1]
					chaine_avant_x = chaine_avant_x + caractere_a_ajouter + chaine_apres_x[0:self.nbre_caractere_par_ligne-1]
					chaine_apres_x = chaine_apres_x[self.nbre_caractere_par_ligne:]	
				elif direction_distance[0] == "N": # déplacement vers le haut
					caractere_a_remplacer = chaine_avant_x[-self.nbre_caractere_par_ligne]
					chaine_apres_x = chaine_avant_x[(len(chaine_avant_x)-self.nbre_caractere_par_ligne)+1:] + caractere_a_ajouter + chaine_apres_x
					chaine_avant_x = chaine_avant_x[:-self.nbre_caractere_par_ligne]	

				if caractere_a_remplacer == "O": # Attention joueur qui croit pouvoir passer à travers les murs
					print("\nAttention!!! Roboc n'est pas un fantôme mais un robot, il ne traverse pas les murs.\nRetour au point de départ!!!\n")
					print(self)
					return (self, caractere_a_ajouter_debut, partie_gagnee)
				elif caractere_a_remplacer == "U":
					if i == direction_distance[1]: # Enfin un joueur digne de ce superbe jeu
						deplacement_affichage = chaine_avant_x + "X" + chaine_apres_x
						print("\n")
						print(deplacement_affichage)
						print("\n!!! GAGNE !!!".center(30))
						partie_gagnee = True
						self.affichage = deplacement_affichage
						return (self, caractere_a_ajouter, partie_gagnee)
					else: # Attention joueur aveugle qui passe devant la sortie sans s'arrêter
						deplacement_affichage = chaine_avant_x + "X" + chaine_apres_x
						print("\n")
						print(deplacement_affichage)
						caractere_a_ajouter = "U"
						i += 1	
				elif caractere_a_remplacer == ".": # Attention que le joueur n'embarque pas la porte
					deplacement_affichage = chaine_avant_x + "X" + chaine_apres_x
					print("\n")
					print(deplacement_affichage)
					caractere_a_ajouter = "."
					i += 1
				else: # La voie est libre				
					deplacement_affichage = chaine_avant_x + "X" + chaine_apres_x
					print("\n")
					print(deplacement_affichage)
					caractere_a_ajouter = " "
					i += 1 	

			self.affichage = deplacement_affichage
			return (self, caractere_a_ajouter, partie_gagnee)
