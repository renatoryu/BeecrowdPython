val1 = int(input())
val2 = int(input())
maior = val1 if val1 > val2 else val2
menor = val2 if val2 < val1 else val1
menor+=1
soma = 0

while (maior > menor):
    if(menor % 2 != 0):
        soma = menor + soma
    menor = menor+1
print(soma)

#O programa deve imprimir um valor inteiro. Este valor é a soma dos valores ímpares que estão entre os valores fornecidos na entrada que deverá caber em um inteiro.





