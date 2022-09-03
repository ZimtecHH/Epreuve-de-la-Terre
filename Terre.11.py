#Créez un programme qui transforme une heure
# affichée en format 24h
# en une heure affichée en format 12h.

heure = int(input("Rentrez l'heure sous format 12 heures : "))

minute = int(input("Rentrez les minutes : "))

# matin_soir : après midi = PM  matin = AM
matin_soir = ""

if heure > 24 :
    print("Tu connais des horloge qui affiche ce genre d'heure ?? ")

if heure == 24:
    heure = (heure-heure)
for i in range(24) :
    if heure == i > 12 :
        matin_soir = "PM"
        heure = (heure-12)
else :
    if heure == i < 12 :
        matin_soir = "AM"
        heure = heure
for k in range(59) :
    if minute == k :
        print(str(heure) +":"+ str(minute)+" "+ matin_soir)