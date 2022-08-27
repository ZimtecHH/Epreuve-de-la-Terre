#Créez un programme qui affiche les arguments qu’il reçoit ligne par ligne, peu importe le nombre d’arguments.

argument1 = [input("Entrez nombre d'argument voulu : ")]

primes = argument1

for number in argument1:
    if number == 'avion':
        break

    if number == 'auhkhukh':
        continue

    number = number.split(" ")

    primes = number
    for prime in primes:
        print(prime)
