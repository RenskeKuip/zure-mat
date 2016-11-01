import xmltodict
import random



#open()
#dit is het invoeren van de ov chipkaart
chipkaartnummer =  input('dit leest de ov-chipkaart scanner? (voer hier een het getal van je ov chipkaart in zonder de spaties):')#deze code simuleert het scannen vaeen OV chip
if len(chipkaartnummer)==16:
    try:
        int(chipkaartnummer)
    except:
        print('U heeft geen getal ingevoerd')
    chipkaartnummer =  input('dit leest de ov-chipkaart scanner:')
else:
    print('de code was niet 16 tekens lang ')
    chipkaartnummer =  input('dit leest de ov-chipkaart scanner? (voer hier een het getal van je ov chipkaart in zonder de spaties):')
print(chipkaartnummer)



#if chipkaartnummer:
    #chipkaartnummer.strip(' ')
#print(chipkaartnummer)

#dit is de layout van de code van het menu pas op de cijfers staan niet op volgorde
# keuze = int
# while keuze != 5:
#     print('1: Ik wil informatie opvragen')
#     print('2: Ik wil mijn fiets plaatsen')
#     print('3: Ik wil mijn fiets ophalen')
#     print('4: Ik wil mijn fiets registreren')
#     try:
#         keuze = int(input('voer hier uw keuze in dit moet een getal zijn:'))
#     except ValueError:
#         print('U heeft geen geldig nummer ingevoerd')
#     if keuze == 4:
#         register()#Roept de functie aan die de fiets in het systeem zet
#     elif keuze == 1:
#         info()#roept de functie die alle informatie laat zien
#     elif keuze == 2:
#         stall()#roept de functie aan die je een fiets laat plaatsen
#     elif keuze == 3:
#         fetch()#haalt een fiets op uit de stalling
