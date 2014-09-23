a_trouver = input("nom/prenon : ")

while a_trouver not in ["nom", "prenom"]:
	a_trouver = input("nom/prenom : ")
if a_trouver == "nom" :
	personne = input("rentré le nom du contact a chercher : ")
	personne = personne.upper()
if a_trouver == "prenom" :
	personne = input("rentré le prenom du contact a chercher : ")
	personne = personne.capitalize()

section = 0

with open("repertoire_pro.txt", "r") as fichier :
	liste = fichier.readlines()
	for element in liste :
		if "*" in element :
			section = section + 1
		if personne in element :
			ind_element = liste.index(element)
			derniere = liste.index(element)+6
			print("\n", personne, "a été trouvé section", section, "\n")
			with open("test.docx", "w") as test :
				for element in liste[ind_element:derniere] :
					print(element)
					test.write(element)