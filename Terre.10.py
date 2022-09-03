#Créez un programme qui
# affiche si un nombre est premier ou pas.

Nombre = int(input(" Rentrez le nombre : "))

if Nombre == 0 or Nombre == 1:
    print("Erreur")
elif Nombre > 1:
    for i in range(2, int(Nombre/2)+1):
         if (Nombre % i) == 0:
            print("Ce n'est pas un nombre premier ")
            break
    else:
        print("C'est un nombre premier ")

else:
    print("Ce n'est pas un nombre premier ")



#LISTE DE NOMBRE PREMIER : 2, 3, 5, 7, 11, 13, 17, 19,