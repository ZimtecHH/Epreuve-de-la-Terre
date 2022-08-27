#Créez un programme qui affiche les arguments qu’il reçoit ligne par ligne, peu importe le nombre d’arguments.
argument1 = input("Entrez nombre d'argument voulu : ")

primes = argument1

for prime in primes:
    coupeur = prime.split("\n")
    print(coupeur)
