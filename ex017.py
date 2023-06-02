import random

#Chamada aleatória para apagar o quadro

aluno1 = input('Qual o nome do aluno 1? ')
aluno2 = input('Qual o nome do aluno 2? ')
aluno3 = input('Qual o nome do aluno 3? ')
aluno4 = input('Qual o nome do aluno 4? ')
lista = [aluno1, aluno2, aluno3, aluno4]
sorteio = random.choice(lista)
print('O aluno que irá apagar o quadro é {}'.format(sorteio))