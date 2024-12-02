# Écrivez votre code ici !
#Création du dictionnaire fruits
fruits={"pomme":"rouge","banane":"jaune","orange":"orange"}

#Ajout de la clé kiwi qui a pour valeur vert
fruits['kiwi']="vert"

couleur_banane=fruits['banane']

#modification de la couleur de pomme
fruits['pomme']="vert"

#suppression de la clé banane du dictionnaire fruits
del fruits("banane")

#Affichage
print(fruits)
