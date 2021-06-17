#igra pogodi broj game guess the number
#guess some number and give user to guess

import random

trazeni_broj = random.randint(0, 10)

while True:
    ucitani_broj = input("Unesite broj: "))
    if ucitani<-broj == trazeni_broj:
        print("Bravo pogodio si!")
        break

    elif ucitani_broj < trazeni_broj:
        print("Unio si manji broj! Pokušaj opet!")
    elif ucitani_broj > trazeni_broj:
        print("Unio si veći broj! Pokušaj opet!")

        broj_pokusaja += 1

        print