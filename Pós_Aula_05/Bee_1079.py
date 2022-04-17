vezes = int(input())
n1 = 0
n2 = 0
n3 = 0
for cont in range(0,vezes):
    n1,n2,n3 = input().split(" ")
    n1 = float(n1)
    n2 = float(n2)
    n3 = float(n3)
    media = (n1*2 + n2*3 + n3*5) / 10
    print('{:.1f}'.format(media))
    vezes = vezes+1

#Leia 1 valor inteiro N, que representa o número de casos de teste que vem a seguir. Cada caso de teste consiste de 3 valores reais, cada um deles com uma casa decimal. Apresente a média ponderada para cada um destes conjuntos de 3 valores, sendo que o primeiro valor tem peso 2, o segundo valor tem peso 3 e o terceiro valor tem peso 5.


    
    
