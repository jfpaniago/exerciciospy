a=int(input('qual o valor da casa?'))
b=int(input('qual é o seu salario?'))
c=int(input('em quantos anos voce vai pagar seu emprestimo?'))

if a/(c*12)>0.3*b:
    print('seu emprestimo foi negado.')
else:
    print('seu emprestimo foi aprovado. as parcelas serão de {} durante {} meses .'.format (a/(c*12),c*12))