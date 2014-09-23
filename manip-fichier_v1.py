import re
def verif(a_verif,regexp=r"^0[0-9]([ .-]?[0-9]{2}){4}$", msg="rentré un numero de telephone valide"):
	if a_verif:
		while re.search(regexp, a_verif) is None :
			test = input(msg)
	return (a_verif)

selection_fichier = "e"

if selection_fichier  not in ["p", "o",]:
	selection_fichier = input ("ajouter un adresse pro ou autre ? (p/o) ")
	selection_fichier = verif(selection_fichier,r"[po]","p or o ")
if selection_fichier =="p":
	with open("repertoire_pro.txt", "a") as fichier :

		nb_contacts = input("combien de contact : ")
		nb_contacts = verif(nb_contacts, r"[0-9]", "entré un nombre ")
		if nb_contacts == "" :
			nb_contacts = 0
		nb_contacts = int(nb_contacts)
		for i in range(nb_contacts):
			nom = input("nom du contact : ")
			nom = nom.upper()
			prenom = input("prenom du contact : ")
			prenom = prenom.capitalize()
			tel_f = input("telephone fixe du contact : ")
			tel_f = verif(tel_f)
			tel_p = input("portable du contact : ")
			tel_p = verif(tel_p)
			mail = input("adresse mail du contact : ")
			mail = verif(mail, r"^[A-Za-z1-9]+@[a-z]+[.][a-z]+$", "entré un adresse email valide")
			ad_skype = input("skype du contact : ")
			adresse = input("adresse postale du contact : ")
			adresse = verif(adresse, r"[0-9]*[A-Za-z -]*[0-9]*[A-Za-z]$","entré un adresse postale valide")

			fichier.write("*\n")
			fichier.write(nom + " " + prenom + "\n")
			fichier.write("fixe : " + tel_f + "\n")
			fichier.write("portable : " + tel_p + "\n")
			fichier.write("adresse e-mail : " + mail + "\n")
			fichier.write("skype : " + ad_skype + "\n")
			fichier.write("adresse : " + adresse + "\n")

elif selection_fichier == o:
	with open("repertoire_autre.txt", "a") as fichier :
		nb_contacts = input("combien de contact : ")
		nb_contacts = verif(nb_contacts, r"[0-9]")
		if nb_contacts == "" :
			nb_contacts = 0
		nb_contacts = int(nb_contacts)
		for i in range(nb_contacts):
			nom = input("nom du contact : ")
			nom = nom.capitalize()
			prenom = input("prenom(ou pseudo) du contact : ")
			prenom = prenom.capitalize()
			tel_f = input("telephone fixe du contact : ")
			tel_f = verif(tel_f)
			tel_p = input("portable du contact : ")
			tel_p = verif(tel_p)
			mail = input("adresse mail du contact : ")
			mail = verif(mail, r"^[A-Za-z1-9]+@[a-z]+[.][a-z]+$", "entré un adresse email valide")
			ad_skype = input("skype du contact : ")
			adresse = input("adresse postale du contact : ")

			fichier.write("\n")
			fichier.write(nom + " " + prenom + "\n")
			fichier.write("fixe : " + tel_f + "\n")
			fichier.write("portable : " + tel_p + "\n")
			fichier.write("adresse e-mail : " + mail + "\n")
			fichier.write("skype : " + ad_skype + "\n")
			fichier.write("adresse : " + adresse + "\n")
