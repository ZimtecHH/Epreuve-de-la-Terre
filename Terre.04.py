#Créez un programme qui permet de déterminer
# si l’argument donné est un entier pair ou impair..

num = int(input("Entrer un nombre : "))
if (num % 2) == 0:
   print("{0} est Pair".format(num))
else:
   print("{0} est Impair".format(num))