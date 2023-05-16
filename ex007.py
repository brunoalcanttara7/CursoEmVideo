"1==()"
"2==**"
"3==*///%"
"4==+-"

nome = input('Qual o seu nome? ')
print('Prazer em lhe conhecer {:=^20}!'.format(nome))

n1 = int(input('Valor 1:'))
n2 = int(input('Valor 2:'))
soma = n1 + n2
multi = n1 * n2
div = n1 / n1
sub = n1 - n2
di = n1 // n2
expo = n1 ** n2
print('A soma é {}; \nA multiplicação é {}; \nA divisão é {}'.format(soma, multi, div), end=' ')
print('A subitração é {}, a divisão por inteiro é {}, a exponencial é {}'.format(sub, di, expo))