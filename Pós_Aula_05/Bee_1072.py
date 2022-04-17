n1 = int(input())
dentroInt = 0
foraInt = 0
for cont in range(1,n1+1):
    X = int(input())
    if X >= 10 and X <= 20:
        dentroInt = 1 + dentroInt
    else:
        foraInt = 1 + foraInt
print('{} in'.format(dentroInt))
print('{} out'.format(foraInt))

#Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
#Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo, mostrando essas informações.