import json
import random

def loadJSON():
    global database
    file = (open('database.txt', 'r')).read()
    database = json.loads(file)

def writeJSON():
    global database
    text = json.dumps(database)
    with open('database.txt', 'w') as file:
        file.write(text)

def randomID():
    global database
    number = ''
    for loop in range(1):
        number += str(random.randrange(0,9))
    if number in database:
        return randomID()
    else:
        return number

def register():
    global database
    loadJSON()
    ID = randomID()
    firstNane = input('Wat is je voornaam: ')
    lastName = input('Wat is je achternaam: ')
    name = firstNane + ' ' + lastName
    database[ID] = {'name' : name, 'present' : False}
    writeJSON()

register()
