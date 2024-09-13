print('hoeveel verdien je bruto per maand? ')
inkomen = input('ik verdien per maand bruto: ')
print('heb je een dertiende maand? j/n')
dertiende = input('j/n ')
inkomen = float(inkomen)

grens = 73.031
if inkomen < grens:
    belastingp = 0.3693
elif inkomen > grens:
    belastingp = 0.4950
x = 1 - belastingp

def maandloon():
    netto = (inkomen * x)
    print(f'uw maandloon is €{netto}')
def jaarloon():
    netto = (inkomen * x)
    if dertiende == ('j'):
        nettojaar = (netto * 13)
    elif dertiende == ('n'):
        nettojaar = (netto * 12)
    print(f'uw jaarloon is €{nettojaar}')

def belastingbox():
    belasting = (inkomen * belastingp)
    print(f'uw maandbelasting is €{belasting}')



jaarloon()
maandloon()
belastingbox()
