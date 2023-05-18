print('===================================')
print('Calculadora aluguel de carro')
dia = int(input('Quantos dias alugados? '))
km = float(input('Quantos KMs rodados? '))
custodiaria = 60
custokm = 0.15
valor = (dia * custodiaria) + (km * custokm)
print('O valor a pagar é R${}'.format(valor))