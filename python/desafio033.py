x=int(input('digite um numero'))
y=int(input('digite outro numero'))
z=int(input('digite mais outro numero'))
if x<y<z:
    print (' menor numero é {} e o maior numero é {}'.format (x,z))
if y<x<z:
    print('o menor numero é {} e o maior numero é {}'.format (y,z))
if z<x<y:
    print('o menor numero é {} e o maior numero é {}'.format (z,y))
if x<z<y:
    print('o menor numero é {} e o maior numero é {}'.format (x,y))
if y<z<x:
    print('o menor numero é {} e o maior numero é {}'.format(y,x))
if z<y<x:
    print('o menor numero é {} e o maior numero é {}'.format(z,x))