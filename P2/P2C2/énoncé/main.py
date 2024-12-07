nombres=str(input("Entrez une liste de nombre séparé par des virgules : "))

#Transformation de la chaine de caractères nombres en liste
liste=nombres.split(",")

#Transformation de la liste en liste d'entiers
liste_entiers=[]
for nombre in liste:
    nombre_entier=int(nombre)
    liste_entiers.append(nombre_entier)
print("La liste finale d'entiers est :",liste_entiers)

#Calcul de la somme des éléments de la liste
somme=0
for i in range(0,len(liste_entiers)):
    somme=somme+liste_entiers[i]
print("La Somme des éléments de la liste est: ",somme)

#Calcul de la moyenne des éléments de la liste
moyenne=somme/len(liste_entiers)
print("La moyenne des éléments de la liste finale est : ",moyenne)

liste_superieure=[]
for nbre in liste_entiers:
    if (nbre>moyenne):
        liste_superieure.append(nbre)
print("La liste de nombres supérieure à la moyenne est: ",liste_superieure)
print("Le nombre d'élément superieure à la moyenne est: ",len(liste_superieure))
