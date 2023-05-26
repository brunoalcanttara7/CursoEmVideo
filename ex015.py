import math

#Cálculo hipotenusa
catopo = float(input('Qual o valor do Cateto Oposto? '))
catadj = float(input('Qual o valor do Cateto Adjacente? '))
hipo = math.hypot(catadj, catopo)
print('A hipotenusa é {:.2f}'.format(hipo))