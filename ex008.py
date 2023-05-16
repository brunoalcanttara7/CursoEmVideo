"Antecessor e Sucessor"
n1 = int(input('Número: '))
nsu = 1
suce = n1 + nsu
ante = n1 - nsu
print('O sucessor é {} e o antecessor é {}, logo o número adicionado é {}'.format(suce, ante, n1))

"Dobro, triplo, raiz quadrada"
dobro = n1 * 2
print('O dobro é {}'.format(dobro))
triplo = n1 * 3
print('O triplo é {}'.format(triplo))
raiz = n1 ** (1/2)
print('A raiz quadrada é {:.3f}'.format(raiz))

print('===================================')
print('Agora vamos calcular média!')
"Média"
nota1 = int(input('Qual a primeira nota? '))
nota2 = int(input('Qual a segunda nota? '))
media = (nota1 + nota2) / 2
print('A média das notas é {}'.format(media))


print('===================================')
print('Calculadora de metros, centímetro e milímetro')
metro = int(input('Qual o valor em metros? '))
centimetro = metro * 100
milimetro = metro * 1000
print('A medida em metros é {}m, em centímetros é {}cm e em milímetros é {}mm'.format(metro, centimetro, milimetro))

print('===================================')
print('Tabuada')
n2 = int(input('Qual o número que deseja ver a tabuada? '))
tab1 = n2 * 1
tab2 = n2 * 2
tab3 = n2 * 3
tab4 = n2 * 4
tab5 = n2 * 5
tab6 = n2 * 6
tab7 = n2 * 7
tab8 = n2 * 8
tab9 = n2 * 9
tab10 = n2 * 10
print('A tabuada do número que foi inserido é: \n {} \n {} \n {} \n {} \n {} \n {} \n {} \n {} \n {} \n {}'.format(tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10))

print('===================================')
print('Calculadora de dolar')
carteira = int(input('Quanto vc tem na carteira em real? '))
dolar = carteira / 5
print('Na sua carteira, tem {} em dólar!'.format(dolar))


print('===================================')
print('Calculadora de area e tinta')
altura = int(input('Qual a altura da parede em metros? '))
largura = int(input('Qual a largura da parede em metros? '))
area = largura * altura
tintalitro = area / 2
print('A quantidade de tinta para pintar uma área de {} m² é de {} litros de tinta.'.format(area, tintalitro))

print('===================================')
print('Calculadora de desconto')
valor1 = int(input('Qual o valor do produto? '))
desconto = int(input('Qual o valor de desconto em %? '))
calcdesconto = (desconto/100) * valor1
valorcomdesconto = valor1 - calcdesconto
print('O valor com desconto é de {}.'.format(valorcomdesconto))

print('===================================')
print('Calculadora de Salário')
salario = int(input('Qual o valor do salário recebido? '))
calc = (15/100) * salario
salarioajustado = salario + calc
print('O valor do salário com acréscimo é de {}.'.format(salarioajustado))