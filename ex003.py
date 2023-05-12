numero1 = int(input('Qual o primeiro número? '))
numero2 = int(input('Qual o segundo número? '))
soma = numero1 + numero2
numero3 = float(input('Qual o terceiro número? '))
numero4 = float(input('Qual o quarto número? '))
soma2 = numero3 + numero4
soma3 = soma + soma2
print('A Soma do primeiro e segundo número é {}!'.format(soma))
print('A soma do terceiro e do quarto número é {}!'.format(soma2))
print('E a soma das duas somas é {}.'.format(soma3))