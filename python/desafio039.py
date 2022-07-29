a=int(input('que ano voce nasceu?'))
if a > 2003:
    print('fique atento! você deve se alistar daqui {} anos'.format(a-2003))
elif a<2003:
    print('voce deveria ter se alistado a {} anos atras'.format(2003-a))
else:
    print('voce deve se alistar esse ano')