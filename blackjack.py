import time as t
import random as r

sk = 500 #totale kapitaal
print(f'uw startkapitaal is {sk}')
t.sleep(0.2)
print('minimale inzet is 10')
t.sleep(0.5)
print('de dealer zal stoppen op 18')
t.sleep(0.5)
p = 'ja' #bepaalt of je nog een potje doet

while p == 'ja':
    st = 0 #totale kaartwaarde speler
    ct = 0 #totale kaartwaarde computer
    print('\n')


    y = 'wrong'
    while y == 'wrong':
        inzet = int(input('wat zet u in '))
        if inzet < 10:
            print('invalid bet')
        elif inzet > sk:
            print('invalid bet')
        elif inzet >= 10:
            y = 'ok'

    sk = sk - inzet
    kl = sk - inzet


    harten = [
                    'aas','2','3','4','5', '6','7','8','9','10','boer','vrouw','heer',   
                ]
    schoppen = [
                    'aas','2','3','4','5', '6','7','8','9','10','boer','vrouw','heer',   
                ]
    ruiten = [
                    'aas','2','3','4','5', '6','7','8','9','10','boer','vrouw','heer',   
                ]
    klaver = [
                    'aas','2','3','4','5', '6','7','8','9','10','boer','vrouw','heer',   
                ]
    d = 0 #totaal aantal gedeelde kaarten in een potje
    aas = 0 #hoeveel asen de computer in zijn hand heeft
    aass = 0 #hoeveel asen de speler in zijn hand heeft
    m = 0 #zorgt ervoor dat het kaarten delen in een loop zit
    H = 12 #aantal harten kaarten
    S = 12 #aantal schoppen kaarten
    R = 12 #aantal ruiten kaarten
    K = 12 #aantal klaver kaarten
    a = 0 #zorgt ervoor dat de eerste kaart van de dealer onbekend is
    h = 0 #zorgt ervoor dat de eerste kaart van de dealer open word gelegd
    x = 0 #zorgt ervoor dat de kaarten worden uitgedeeld
    b = 1 #om te kijken voor een mogelijkheid op double down of splitten
    doubledown = 0
    t.sleep(0.5)


    while m < 1:

        while x < 4:
            if d == 0:
                print('dealers kaart')
            elif d == 2:
                print('uw kaarten')
            s = r.randint(0,3) #bepaalt welke soort kaart er word uitgedeeld
            #de variabele nummer bepaalt de waarde van de uitgedeelde kaart
            
            t.sleep(0.5)
            
            if s == 0:
                
                nummer = r.randint(0,H)
                
                kaart = harten[nummer]
                harten.pop(nummer)
                if a == 1:
                    print('harten', kaart)
                H = H - 1
                
                
            elif s == 1:
                
                nummer = r.randint(0,S)
                
                kaart = schoppen[nummer]
                schoppen.pop(nummer)
                if a == 1:
                    print('schoppen', kaart)
                S = S - 1
                
            elif s == 2:
                
                nummer = r.randint(0,R)
                
                kaart = ruiten[nummer]
                ruiten.pop(nummer)
                if a == 1:
                    print('ruiten', kaart)
                R = R - 1
                
            elif s == 3:
                
                nummer = r.randint(0,K)
                
                kaart = klaver[nummer]
                klaver.pop(nummer)
                if a == 1:
                    print('klaver', kaart)
                K = K - 1
            if a == 0:
                hg = kaart
                #waardes geven aan de kaarten van de dealer
            if x <= 1:
                if kaart == 'aas':
                    ct = ct + 11
                    aas = aas + 1
                elif kaart == '2':
                    ct = ct + 2
                elif kaart == '3':
                    ct = ct + 3
                elif kaart == '4':
                    ct = ct + 4
                elif kaart == '5':
                    ct = ct + 5
                elif kaart == '6':
                    ct = ct + 6
                elif kaart == '7':
                    ct = ct + 7
                elif kaart == '8':
                    ct = ct + 8
                elif kaart == '9':
                    ct = ct + 9
                elif kaart == '10':
                    ct = ct + 10
                elif kaart == 'boer':
                    ct = ct + 10
                elif kaart == 'vrouw':
                    ct = ct + 10
                elif kaart == 'heer':
                    ct = ct + 10
                if ct > 21:
                        if aas > 0:
                            ct = ct - 10
                            aas = aas - 1
                a = 1
                #waardes geven aam de kaarten van de speler
            elif x > 1:
                if kaart == 'aas':
                    st = st + 11
                    aass = aass + 1
                elif kaart == '2':
                    st = st + 2
                elif kaart == '3':
                    st = st + 3
                elif kaart == '4':
                    st = st + 4
                elif kaart == '5':
                    st = st + 5
                elif kaart == '6':
                    st = st + 6
                elif kaart == '7':
                    st = st + 7
                elif kaart == '8':
                    st = st + 8
                elif kaart == '9':
                    st = st + 9
                elif kaart == '10':
                    st = st + 10
                elif kaart == 'boer':
                    st = st + 10
                elif kaart == 'vrouw':
                    st = st + 10
                elif kaart == 'heer':
                    st = st + 10
                if st > 21:
                        if aass > 0:

                            st = st - 10
                            aass = aass - 1
            

            if x == 2:
                split = kaart
            d = d + 1
            x = x + 1
        print(f'uw totaal score {st}')
        t.sleep(1)
        if st < 21 and ct < 21:
            if doubledown == 0:
                if b == 1 and split == kaart and kl >= 0:
                    hitorstand = input('hit, stand, double down or split ')
                    b = 2
                elif b == 1 and kl >= 0:
                    hitorstand = input('hit, stand or double down ')
                    b = 2
                else:
                    hitorstand = input('hit or stand ')

            if hitorstand == 'hit':
                x = x - 1
            elif hitorstand == 'stand':
                m = 1
                print(f'de kaart die eerder aan de dealer is gegeven {hg}')
                while ct < 18:
                    s = r.randint(0,3)
                    if h == 0:
                        
                        h = 1
                    t.sleep(1)
                    if s == 0:
                        nummer = r.randint(0,H)
                        
                        kaart = harten[nummer]
                        harten.pop(nummer)
                        print('harten', kaart)
                        H = H - 1
                        
                    elif s == 1:
                        
                        nummer = r.randint(0,S)
                        
                        kaart = schoppen[nummer]
                        schoppen.pop(nummer)
                        print('schoppen', kaart)
                        S = S - 1
                        
                    elif s == 2:
                        
                        nummer = r.randint(0,R)
                        
                        kaart = ruiten[nummer]
                        ruiten.pop(nummer)
                        print('ruiten', kaart)
                        R = R - 1
                        
                    elif s == 3:
                        
                        nummer = r.randint(0,K)
                        
                        kaart = klaver[nummer]
                        klaver.pop(nummer)
                        print('klaver', kaart)
                        K = K - 1
                    #waardes geven aan de kaarten van de dealer
                    if kaart == 'aas':
                        ct = ct + 11
                        aas = aas + 1
                    elif kaart == '2':
                        ct = ct + 2
                    elif kaart == '3':
                        ct = ct + 3
                    elif kaart == '4':
                        ct = ct + 4
                    elif kaart == '5':
                        ct = ct + 5
                    elif kaart == '6':
                        ct = ct + 6
                    elif kaart == '7':
                        ct = ct + 7
                    elif kaart == '8':
                        ct = ct + 8
                    elif kaart == '9':
                        ct = ct + 9
                    elif kaart == '10':
                        ct = ct + 10
                    elif kaart == 'boer':
                        ct = ct + 10
                    elif kaart == 'vrouw':
                        ct = ct + 10
                    elif kaart == 'heer':
                        ct = ct + 10
                    if ct > 21:
                            if aas > 0:
                                ct = ct - 10
                                aas = aas - 1
                    t.sleep(0.5)
                t.sleep(0.3)   
                print(f'dealer score {ct}')
                if ct > 21:
                    print('u wint')
                    inzet = inzet * 2
                elif st < ct:
                    print('u verliest')
                    inzet = 0
                elif st == ct:
                    print('het is gelijkspel')
                elif st > ct:
                    print('u wint')
                    inzet = inzet * 2
            elif hitorstand == 'double down':
                sk = sk - inzet
                inzet = inzet * 2
                x = x - 1
                doubledown = 1
                hitorstand = 'stand'
        elif ct == st:
            print('het is gelijkspel')
            m = 1
        elif ct == 21:
            print(f'de kaart die eerder aan de dealer is gegeven {hg}')
            t.sleep(0.5)
            print('de dealer heeft blackjack')
            t.sleep(0.5)
            print('u verliest')
            inzet = 0
            m = 1
        elif st == 21:
            m = 1
            print('u heeft blackjack')
            inzet = inzet * 2
        elif st > 21:
            m = 1
            print('u verliest')
            inzet = 0

    sk = sk + inzet

    print(f'uw totale kapitaal {sk}')
    t.sleep(0.2)
    if sk > 10:
        hoi = 'wrong'
        while hoi == 'wrong':
            p = input('wilt u nog een potje doen? ')
            if p == 'ja' or p == 'nee':
                hoi = 'ok'
            else:
                print('geen correct antwoord op de vraag')
    else:
        print('u heeft niet genoeg geld om mee te doen')
        p = 'niet genoeg geld'

if sk > 0:
    t.sleep(1)
    print('het spijt mij te zeggen dat u niet met echt geld speelt')
    t.sleep(1)
    print('er is dus ook geen cash out, nog een hele fijne dag verder.')
else:
    print('een hele fijne dag verder.')
    