import math

#Cáculo de Seno, Cosseno e Tângente

angulo = int(input('Qual o ângulo? '))
seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O Seno, Cosseno e Tangente de {:.2f} em Radianos é: \nSeno = {:.2f} \nCosseno = {:.2f} \nTangente = {:.2f}'.format(angulo, seno, coseno, tangente) )