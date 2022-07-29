from random import randint
from time import sleep
computador= randint(0,5)
print('vou sortear um número entre 0 e 5! Tente adivinhar qual é: ')
print('-=-'*20)
n = int(input('qual é o seu palpite? '))
print('Processando...')
sleep(2)
if n == computador:
    print('Parabéns, voce acertou!')
else:
    print('Eu pensei no número {} e não no número {}.'.format(computador,n))
    print ('Tente novamente.')