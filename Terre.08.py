#Créez un programme qui affiche le résultat d’une puissance.
#L’exposant ne pourra pas être négatif.
def puissance_two_numbers(a, b):
    return a ** b


Nombre = int(input("Rentrez le nombre : "))

Exposant = int(input("Maintenant rentrez l'exposant qui doit être positif : "))

puissance = puissance_two_numbers(Nombre,Exposant)

if Exposant < 0:
   print("Exposant négatif erreur ")

else:
   print(puissance)
