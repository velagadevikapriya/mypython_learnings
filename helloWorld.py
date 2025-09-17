Weight = int(input('what is your weight? '))
unit = input('(K)g or (L)bs? ')
if unit.upper() == 'K':
    converted = Weight / 0.45
    print('weight in Lbs: ' + str(converted))