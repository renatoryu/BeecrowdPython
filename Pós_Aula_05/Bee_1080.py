maior = 0
vez = 0
x = 0

for cont in range(0,5): # conta os primeiros 5 números
    n1 = int(input())
    if n1 > x:
        maior = n1 # se o número for maior que o anterior, vai ficar armazenado em maior
        x = n1 # definir a comparação entre um número anterior e o seguinte
        posicao = cont + 1 # saber a posição do número
print(maior) # o maior número é
print(posicao) # a posição do maior número é

#Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.

