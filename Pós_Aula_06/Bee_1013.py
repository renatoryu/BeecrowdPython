import math

entrada = input().split(" ")
A, B, C = entrada
maior = (int(A) + int(B) + abs(int(A) - int(B)))  / 2
resultado = (int(maior) + int(C) + abs(int(maior) - int(C)))/2
print('{:.0f} eh o maior'.format(resultado))

# Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".

