num=int(input('digite um numero'))
print('[1]binário\n[2]octal\n[3]hexadecimal')
opcao=int(input('voce gostaria de converter este numero para qual linguagem?'))
if opcao==1:
    print('{} convertido para binário é igual a {}'.format(num,bin(num)[2:]))
elif opcao==2:
    print('{} convertido para octal é igual a {}'.format(num,oct(num)[2:]))
elif opcao==3:
    print('{} convertido para hexadecimal é igual a {}'.format(num,hex(num)[2:]))
else:
    print('opção invalida')

