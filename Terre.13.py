#Créez un programme qui prend
# en paramètre trois entiers et
# affiche la valeur du milieu.

print("Le but de se programme est que pour trois entier rentré la valeur du milieu soit affiché")

premier_entier = int(input(" Premier Entier : "))

deuxième_entier = int(input(" Deuxième Entier : "))

troisième_entier = int(input(" Troisième Entier : "))

print(str(premier_entier)+" "+ str(deuxième_entier)+" "+ str(troisième_entier))

if premier_entier < deuxième_entier < troisième_entier :
    print("La valeur du milieu est donc :")
    print(str(deuxième_entier))

if troisième_entier < deuxième_entier < premier_entier :
    print("La valeur du milieu est donc :")
    print(str(deuxième_entier))

if deuxième_entier < premier_entier < troisième_entier :
    print("La valeur du milieu est donc :")
    print(str(premier_entier))

if troisième_entier < premier_entier < deuxième_entier :
    print("La valeur du milieu est donc :")
    print(str(premier_entier))

if premier_entier < troisième_entier < deuxième_entier :
    print("La valeur du milieu est donc :")
    print(str(troisième_entier))

if deuxième_entier < troisième_entier < premier_entier :
    print("La valeur du milieu est donc :")
    print(str(deuxième_entier))

