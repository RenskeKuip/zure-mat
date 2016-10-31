import csv
import random

#dit is de layout van de code van het menu pas op de cijfers staan niet op volgorde
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
        register()#Roept de functie aan die
    elif keuze == 1:
        info()
    elif keuze == 2:
        stall()
    elif keuze == 3:
        fetch()


# functies die nu erin staan:
