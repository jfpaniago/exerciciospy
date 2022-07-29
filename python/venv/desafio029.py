n = float(input('Velocidade:'))
x= (n-80)*7
if n > 80:
    print('Você ultrapassou o limite permitido de velocidade. Sua multa será de {}'.format(x))
else:
    print('sua velocidade é de {}km/h. Boa viagem!'.format(n))