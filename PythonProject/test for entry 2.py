from tkinter import *
import json
import random
import datetime
from tkinter.messagebox import showinfo
import sys

chipkaartnummer = ""
name = ""
counter = 0

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
    window = Toplevel(root)
    global database
    number = ''
    for loop in range(10):
        number += str(random.randrange(0,9))
    if number in database:
        return randomID()
    else:
        return number
#
# def return_entry():
#     """Gets and prints the content of the entry"""
#     content = entry.get()
#     print(content)


entryb1 = StringVar

def register():
    global database
    loadJSON()

    if counter 
    global counter
    counter += 1
    chipscan()
    ID = randomID()

    def nameAsk():
        window = Toplevel(root)
        Label(window, text="Wat is uw volledige naam? ").pack(ipady=5, ipadx=5, padx=2, pady=2)
        entry1 = Entry(window, textvariable=entryb1)
        entry1.pack(ipady=5, ipadx=5, padx=2, pady=2)
    # Connect the entry with the return button
    # entry.bind('<Return>', entry.get())

        def callback():
            print(entry1.get())
            global name
            name = entry1.get()

        b1 = Button(window, text="continue", command= lambda: callback())
        b1.pack()

    def fietsCode():
        database[ID] = {'naam' : name, 'aanwezig' : False, 'ovchip' : ovChip}
        showinfo(message='Het unieke nummer van jouw fiets is: ' + str(ID))
        if input('Wil je je fiets gelijk stallen? (Y/N): ') == 'Y':
            database[ID]['aanwezig'] = True
            database[ID]['sinds'] = str(datetime.datetime.now())
        writeJSON()


ID = ""
def store():
    global database
    loadJSON()
    global counter

    # window = Toplevel(root)
    # Label(window, text="Geef het 10 cijferig nummer van jouw de fiets: ").pack()
    # entry1 = Entry(window, textvariable=entryb1)
    # entry1.pack()
    #
    # def callback():
    #     print(entry1.get())
    #     global ID
    #     ID = entry1.get()
    #
    # b1 = Button(window, text="continue", command=callback())
    # b1.pack()
    ID = input('Geef het 10 cijferig nummer van jouw de fiets: ')
    if ID not in database:
        showinfo(message='Deze fiets is niet bij ons bekend')
    elif database[ID]['aanwezig'] is True:
        showinfo(message='Deze fiets staat al in de stalling...')
    else:
        database[ID]['aanwezig'] = True
        database[ID]['sinds'] = str(datetime.datetime.now())
        writeJSON()

def pickup():
    global database
    loadJSON()
    ID = input('Geef het 10 cijferig nummer van de fiets die je wilt ophalen: ')
    if ID not in database:
        showinfo(message='Deze fiets is niet bij ons bekend')
    elif database[ID]['aanwezig'] is False:
        showinfo(message='Deze fiets staat niet in de stalling')
    else:
        ovChip = chipscan()
        if database[ID]['ovchip'] != ovChip:
            showinfo(message='Jij bent niet de eigenaar van deze fiets')
        else:
            database[ID]['aanwezig'] = False
            del database[ID]['sinds']
            showinfo(message='Je hebt je fiets opgehaald')
            writeJSON()

def count():
    global database
    loadJSON()
    count = 0
    for fiets in database:
        if database[fiets]['aanwezig'] is True:
            count += 1
    if count == 1:
        showinfo(message='Er staat op dit moment 1 fiets in de stalling')
    else:
       showinfo(message='Er staan op dit moment ' + str(count) + ' fietsen in de stalling')
    showinfo(message='Er zijn nog ' + str(500 - count) + ' plekken beschikbaar')


def chipscan():
    window = Toplevel(root)
    Label(window, text="Dit leest de ov-chipkaart scanner? (voer hier een het getal van je ov chipkaart in zonder de spaties): ").pack(ipady=5, ipadx=5, padx=2, pady=2)
    entry = Entry(window)
    entry.pack()

    def callback1():
        print(entry.get())
        global chipkaartnummer
        chipkaartnummer = entry.get()

    b1 = Button(window, text="submit", command=lambda: callback1())
    b1.pack()


    chipkaartnummer = str(1234123412341234)
    if len(chipkaartnummer) == 16:
        try:
            chipkaartnummer = int(chipkaartnummer)
            return chipkaartnummer
            register()
        except:
            showinfo(message='U heeft geen getal ingevoerd')
            chipscan()
    else:
        showinfo(message='De code was niet 16 tekens lang ')
        chipscan()

root = Tk()

label = Label(master=root,
              text='Fietsenstalling',
              font =("Italic",50),
              width=15,
              height=5)
label.pack()

button = Button(master=root,
                text="Fiets registreren",
                command=register)
button.pack(ipady=5, ipadx=5, padx=2, pady=2)

button2 = Button(master=root,
                 text="Fiets stallen",
                command=store)
button2.pack(ipady=5, ipadx=5, padx=2, pady=2)

button3 = Button(master=root,
                 text="Fiets ophalen",
                command=pickup)
button3.pack(ipady=5, ipadx=5, padx=2, pady=2)

button4 =  Button(master=root,
                  text="Informatie opvragen",
                  command=count)
button4.pack(ipady=5, ipadx=5, padx=2, pady=2)

root.mainloop()
