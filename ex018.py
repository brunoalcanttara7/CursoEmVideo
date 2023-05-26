import random

#Ordem de apresentações na sala

aluno1 = input('Qual o aluno 1? ')
aluno2 = input('Qual o aluno 2? ')
aluno3 = input('Qual o aluno 3? ')
aluno4 = input('Qual o aluno 4? ')
lista = [aluno1, aluno2, aluno3, aluno4]
ordem = random.uniform(lista)
print(ordem)