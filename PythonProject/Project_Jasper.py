import json
import random
import datetime

def loadJSON():
    global database
    file = (open('database.txt', 'r')).read()
    database = json.loads(file)

def writeJSON():
    global database
    text = json.dumps(database, sort_keys=True, indent=4)
    with open('database.txt', 'w') as file:
        file.write(text)

def randomID():
    global database
    number = ''
    for loop in range(10):
        number += str(random.randrange(0,9))
    if number in database:
        return randomID()
    else:
        return number

def register():
    global database
    loadJSON()
    ID = randomID()
    name = input('Wat is je voledige naam: ')
    ovChip = chipscan()
    database[ID] = {'naam' : name, 'aanwezig' : False, 'ovchip' : ovChip}
    print('Het unieke nummer van jouw fiets is: ' + str(ID))
    if input('Wil je je fiets gelijk stallen? (Y/N): ') == 'Y':
        database[ID]['aanwezig'] = True
        database[ID]['sinds'] = str(datetime.datetime.now())
    writeJSON()

def store():
    global database
    loadJSON()
    ID = input('Geef het 10 cijferig nummer van jouw de fiets: ')
    if ID not in database:
        print('Deze fiets is niet bij ons bekend')
    elif database[ID]['aanwezig'] is True:
        print('Deze fiets staat al in de stalling...')
    else:
        database[ID]['aanwezig'] = True
        database[ID]['sinds'] = str(datetime.datetime.now())
        writeJSON()

def pickup():
    global database
    loadJSON()
    ID = input('Geef het 10 cijferig nummer van de fiets die je wilt ophalen: ')
    if ID not in database:
        print('Deze fiets is niet bij ons bekend')
    elif database[ID]['aanwezig'] is False:
        print('Deze fiets staat niet in de stalling')
    else:
        ovChip = chipscan()
        if database[ID]['ovchip'] != ovChip:
            print('Jij bent niet de eigenaar van deze fiets')
        else:
            database[ID]['aanwezig'] = False
            del database[ID]['sinds']
            print('Je hebt je fiets opgehaald')
            writeJSON()

def count():
    global database
    loadJSON()
    count = 0
    for fiets in database:
        if database[fiets]['aanwezig'] is True:
            count += 1
    if count == 1:
        print('Er staat op dit moment 1 fiets in de stalling')
    else:
       print('Er staan op dit moment ' + str(count) + ' fietsen in de stalling')
    print('Er zijn nog ' + str(500 - count) + ' plekken beschikbaar')


def chipscan():
    chipkaartnummer =  input('Dit leest de ov-chipkaart scanner? (voer hier een het getal van je ov chipkaart in zonder de spaties): ')#deze code simuleert het scannen va. een OV chip
    if len(chipkaartnummer) == 16:
        try:
            chipkaartnummer = int(chipkaartnummer)
            return chipkaartnummer
        except:
            print('U heeft geen getal ingevoerd')
            chipscan()
    else:
        print('De code was niet 16 tekens lang ')
        chipscan()



while True:
    print('----------------------')
    print('1: Ik wil een fiets registreren')
    print('2: Ik wil mijn fiets parkeren')
    print('3: Ik wil mijn fiets ophalen')
    print('4: Ik wil weten hoeveel plekken er vrij zijn')
    print('5: Ik wil stoppen')
    try:
        menuChoice = int(input(''))
    except ValueError:
        print('Geef een geldig nummer op.')
        continue
    if menuChoice < 1 or menuChoice > 5:
        print('Geef een geldig nummer op.')
        continue
    elif menuChoice == 1:
        register()
    elif menuChoice == 2:
        store()
    elif menuChoice == 3:
        pickup()
    elif menuChoice == 4:
        count()
    elif menuChoice == 5:
        print('Bedankt en tot ziens!')
        break
