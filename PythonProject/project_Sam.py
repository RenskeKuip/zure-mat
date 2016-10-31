import csv
import random

keuze = int

while keuze != 5:
    print('1: Ik wil een Fiets registreren')
    print('2: Ik wil mijn fiets stallen')
    print('3: Ik wil informatie opvragen')
    print('4: Ik wil mijn fiets ophalen')
    print('')
    try:
        keuze = int(input('voer hier uw keuze in dit moet een getal zijn:'))
    except ValueError:
        print('U heeft geen geldig nummer ingevoerd')
    if keuze == 4:
        aantal_kluizen_vrij()
    elif keuze == 1:
        nieuwe_kluis()
    elif keuze == 2:
        kluis_openen()
    elif keuze == 3: #does nothing
        print('This is not a requirement for the assignment')
