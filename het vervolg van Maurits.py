import random
import os 

desktop_path = os.path.join(os.environ['USERPROFILE'], 'Desktop')
filename = 'output11.txt'
full_path = os.path.join(desktop_path, filename)

aantalKlanten = 2000
aantalpersoneel = int(input("aantal personeelsleden: "))

voornamen = ['Walter', 'Jan', 'Neo', 'Trinity', 'Morphius', 'Anne-lfeur', 'Peter', 'Pieter', 'Emma', 'Michael', 'Richard', 'Nebuchadnezzar', 'Elion', 'Jay', 'Maurits', 'Tygo', 'Simon', 'Flavius', 'Jesse', 'BSN', 'NAAMVANJEKIND']
achternamen = ['White', 'de Wit', 'de Vries', 'Janssen', 'van Babylon', 'Bozarius', 'Banana', 'Jimmy', 'Ozark', 'Breaking', 'Bad', 'Matrix']
straten = ['Kerkstraat', 'Schoolstraat', 'Molenstraat', 'Dorpsstraat', 'Brugstraat', 'Westeinde', 'Oosteinde', 'Heteinde']
woonplaatsen = ['Hengelo', 'Almelo', 'Enschede', 'Bornerbroek', 'Urk', 'Amsterdam', 'Daarlerveen', 'Vroomshoop', 'Zaanse Schans','Duivendrecht', 'Adorp', 'Vriezenveen']

def willekeurigIets(maxRandom, lijst):
    willekeurigGetal = random.randint(0,maxRandom)
    if lijst == False:
        return willekeurigGetal
    else:
        return lijst[willekeurigGetal]
def salaris():
    salaris1 = random.randint(1000,2000)
    salaris1 = float(salaris1/100)
    return salaris1

with open(full_path, 'w') as f: 
    f.write("CREATE TABLE 'klantgegevens' (KlantID, Voornaam, Achternaam, Adres, Woonplaats, Telefoonnummer);\n")
    f.write("CREATE TABLE 'bestellingen' (Bestelnr, KlantID, Tijd, Prijs, Bodem, Telefoonnummer);\n")
    f.write("CREATE TABLE 'BesteldePizza' (Pizzanr, Bodem, Saus, Topping, Grootte, Korst);\n")
    f.write("CREATE TABLE 'Personeel' (Medewerkernr, Voornaam, Achternaam, Adres, Woonplaats, Telefoonnummer, Salaris);\n")
    f.write('INSERT INTO klantgegevens (KlantID, Voornaam, Achternaam, Adres, Woonplaats, Telefoonnummer)\n')
    f.write('VALUES\n')

while aantalKlanten > 0:
    with open(full_path, 'a') as f:
        if aantalKlanten > 1:
            message = (f'({aantalKlanten}, \'{willekeurigIets(len(voornamen)-1, voornamen)}\', \'{willekeurigIets(len(achternamen)-1, achternamen)}\', \'{willekeurigIets(len(straten)-1, straten)} {willekeurigIets(350, False)}\', \'{willekeurigIets(len(woonplaatsen)-1, woonplaatsen)}\', 06{willekeurigIets(100000000, False)}),')
            f.write(message + '\n')
        if aantalKlanten == 1:
            message = (f'({aantalKlanten}, \'{willekeurigIets(len(voornamen)-1, voornamen)}\', \'{willekeurigIets(len(achternamen)-1, achternamen)}\', \'{willekeurigIets(len(straten)-1, straten)} {willekeurigIets(350, False)}\', \'{willekeurigIets(len(woonplaatsen)-1, woonplaatsen)}\', 06{willekeurigIets(100000000, False)});')
            f.write(message + '\n')
        aantalKlanten -= 1


with open(full_path, 'a') as f:
    f.write('INSERT INTO Personeel (Medewerkernr, Voornaam, Achternaam, Adres, Woonplaats, Telefoonnummer, Salaris) \n')
    f.write('VALUES\n')

while aantalpersoneel > 0:
    with open(full_path, 'a') as f:
        if aantalpersoneel > 1:
            message = (f'({aantalpersoneel}, \'{willekeurigIets(len(voornamen)-1, voornamen)}\', \'{willekeurigIets(len(achternamen)-1, achternamen)}\', \'{willekeurigIets(len(straten)-1, straten)} {willekeurigIets(350, False)}\', \'{willekeurigIets(len(woonplaatsen)-1, woonplaatsen)}\', 06{willekeurigIets(100000000, False)}, {salaris()}),')
            f.write(message + '\n')
        if aantalpersoneel == 1:
            message = (f'({aantalpersoneel}, \'{willekeurigIets(len(voornamen)-1, voornamen)}\', \'{willekeurigIets(len(achternamen)-1, achternamen)}\', \'{willekeurigIets(len(straten)-1, straten)} {willekeurigIets(350, False)}\', \'{willekeurigIets(len(woonplaatsen)-1, woonplaatsen)}\', 06{willekeurigIets(100000000, False)}, {salaris()});')
            f.write(message + '\n')
        aantalpersoneel -= 1