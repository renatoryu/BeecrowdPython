cont = 0
positivo = 0
media = 0
total = 0

for cont in range(1,7):
    valores = float(input())
    if valores > 0:
        positivo = positivo + 1
        total = total + valores
        cont = cont + 1  
       
print('{} valores positivos'.format(positivo))
print('{:.1f}'.format(total/positivo))

#Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos. Na próxima linha, deve-se mostrar a média de todos os valores positivos digitados, com um dígito após o ponto decimal.

