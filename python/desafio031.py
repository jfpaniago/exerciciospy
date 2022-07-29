x = float(input('qual a distancia da sua viagem?'))
if x <= 200:
    y= x*0.5
    print('sua passagem custa {}'.format(y))
else:
    z= x*0.45
    print('sua passagem custa {}'.format (z))