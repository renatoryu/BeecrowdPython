cont = 0
pares = 0
impares = 0
negativo = 0
positivo = 0
for cont in range(1,6):
    valores = int(input())
    if valores % 2 == 0:
        pares = pares + 1
        cont = cont + 1
        
    if valores % 2 != 0:
        impares = impares + 1
        cont = cont + 1
        
    if valores > 0:
        positivo = positivo + 1
        cont = cont + 1  
        
    if valores < 0:
        negativo = negativo + 1
        cont = cont + 1  
        
print('{} valor(es) par(es)'.format(pares))
print('{} valor(es) impar(es)'.format(impares))
print('{} valor(es) positivo(s)'.format(positivo))
print('{} valor(es) negativo(s)'.format(negativo))

#Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares, quantos valores digitados foram positivos e quantos valores digitados foram negativos.



