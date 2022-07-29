a=float(input('digite sua nota na p1'))
b=float(input('digite sua nota na p2'))
c=(a+b)/2
print(c)
if c<5:
    print('reprovado')
elif 5<=c<7:
    print('recuperação')
else:
    print('aprovado')