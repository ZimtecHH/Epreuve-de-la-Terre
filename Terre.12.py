#Créez un programme qui transforme une
# heure affichée en format 12h
# en une heure affichée au format 24h.

heure = int(input("Rentrez l'heure sous format 12 heures : "))

minute = int(input("Rentrez les minutes : "))

matin_soir = input(" matin = AM   après midi = PM : ")

if heure > 12 :
    print("Ce n'est pas sous format 12 heures !! ")

if heure == 12 and matin_soir == "AM":
    heure = (heure-heure)
for i in range(12) :
    if heure == i < 12 and matin_soir == "PM":
        heure = (heure+12)

    if heure == i < 12 :
        matin_soir = "AM"
        heure = heure
for k in range(59) :
    if minute == k :
        print(str(heure) +":"+ str(minute))