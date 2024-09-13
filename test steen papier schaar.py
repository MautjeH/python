import random as r

import time

y = int(input('hoeveel potjes wil je spelen? '))

ss = 0
cs = 0
x = 0
score = f'computer score {cs}, uw score {ss}'
while x < y:

    speler = input('steen, papier of schaar ')

    time.sleep(4)

    pc = r.randint(0,2)

    if speler == 'steen':
        speler = 0
    elif speler == 'papier':
        speler = 1
    elif speler == 'schaar':
        speler = 2

    if pc == 0:
        print('steen')
    if pc == 1:
        print('papier')
    if pc == 2:
        print('schaar')

    if speler == pc:
        print('gelijkspel')
        print(f'computer score {cs}, uw score {ss}')
    elif speler == 0:
        if pc == 1:
            cs = cs + 1
            print("computer wint")
            print(f'computer score {cs}, uw score {ss}')
        elif pc == 2:
            ss = ss + 1
            print("jij wint")
            print(f'computer score {cs}, uw score {ss}')
    elif speler == 1:
        if pc == 0:
            ss = ss + 1
            print('jij wint')
            print(f'computer score {cs}, uw score {ss}')
        elif pc == 2:
            cs = cs + 1
            print('computer wint')
            print(f'computer score {cs}, uw score {ss}')
    elif speler == 2:
        if pc == 0:
            cs = cs + 1
            print('computer wint')
            print(f'computer score {cs}, uw score {ss}')
        elif pc == 1:
            ss = ss + 1
            print('jij wint')
            print(f'computer score {cs}, uw score {ss}')
    x = x + 1