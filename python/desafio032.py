from datetime import date
ano = int(input('digite o ano que voce quer analisar: . se quiser analisar o ano atual digite 0 '))
if ano ==0:
    ano=date.today().year
if ano%4==0 and ano%100 !=0 or ano%400==0:
    print('o ano {} é bissexto'.format(ano))
else:
    print('o ano {} nao é bissexto.'.format(ano))