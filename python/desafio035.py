print('ANALISADOR DE TRIANGULOS')
print('-==-'*20)
x=float(input('digite o tamanho do primeiro segmento'))
y=float(input('digite o tamanho do segundo segmento'))
z=float(input('digite o tamanho do terceiro segmento'))
if z<y+x and y<x+z and x<z+y:
    print('os segmentos podem formar um triangulo.')
else:
    print('os segmentos nao podem formar um triangulo.')
