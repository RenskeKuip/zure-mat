import csv
import random

#De functies:
#Het openen en lezen van het bestand en als die nog niet bestaat, aanmaken.
def csvToList():
    global bikeList
    bikeList = []
    try:
        file = open('fietsen.csv', 'r')
    except FileNotFoundError:
        open('fietsen.csv', 'w')
        file = open('fietsen.csv', 'r')
    CSVFile = csv.reader(file)
    for line in CSVFile:
        bikeList.append(line)

#Het schrijven van de lijst met gegevens naar het CSV bestand.
def listToCSV():
    global bikeList
    file = open('fietsen.csv', 'w', newline= '')
    CSVFile = csv.writer(file)
    for bike in bikeList:
        CSVFile.writerow(bike)

def randomNumber():
    number = ''
    for i in range(10):
        number += str(random.randrange(0, 9))
    return number

def registrerBike():
    global bikeList
    if bikeList == []:
        bikeList = [[ovNummer,randomNumber()]]
    else:
        temp = ovNummer,randomNumber()
        bikeList.append(temp)

ovNummer = 12345
csvToList()
registrerBike()
listToCSV()