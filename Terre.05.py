#Créez un programme qui affiche le résultat
# et le reste d’une division entre deux nombres.
def modulo_two_numbers(a, b):
    return a % b

argument1 = float(input("Rentrez le premier argument : "))

argument2 = float(input("Rentrez le deuxième argument : "))

Resolve = modulo_two_numbers(argument1,argument2)


print("Le reste de cette division est %f" %Resolve)
