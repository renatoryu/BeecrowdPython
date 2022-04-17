cont = 0
positivo = 0
for cont in range(1,7):
    valores = float(input())
    if valores > 0:
        positivo = positivo + 1
        
print('{} valores positivos'.format(positivo))

#Imprima uma mensagem dizendo quantos valores positivos foram lidos.

