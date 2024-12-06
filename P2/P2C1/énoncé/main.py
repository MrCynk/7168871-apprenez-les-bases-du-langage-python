#fourniture des 2 nombres
nombre1=str(input("Entrez le 1er nombre : "))
nombre2=str(input("Entrez le 2ème nombre : "))

#vérification des nombres s'ils sont entier
if nombre1.isnumeric() and nombre2.isnumeric():
  nombre1=int(nombre1)
  nombre2=int(nombre2)
else:
  raise SystemExit("Fin du programme")

#creation de l'opération
operation=input("Saisir l'opérateur souhaitéé : ")
if (operation=="-"):
  resultat=nombre1-nombre2
elif (operation=="+"): 
  resultat=nombre1+nombre2
elif (operation=="*"):
  resultat=nombre1*nombre2
elif (operation=="/"):
  if(nombre2 != 0):
    resultat=nombre1/nombre2
  else:
    raise SystemExit("Impossible de diviser par 0")
else :
  raise SystemExit()
print(nombre1,operation,nombre2,"=",round(resultat,2))
