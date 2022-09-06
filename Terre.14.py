#Créez un programme qui détermine
# si une liste d’entiers est triée ou pas.

print("Rentre tes entiers :")

entiers = [int(s) for s in input().split()]

print(entiers)

Trier = sorted(entiers)

if entiers != Trier :
    print("Pas Triée")
else :
    print("Trié")