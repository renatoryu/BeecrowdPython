X = 1
Y = 2
while X != Y:
    X, Y = input().split()
    X = int(X)
    Y = int(Y)
    if X < Y:
        print('Crescente')
    elif X == Y:
        continue
    else:
        print('Decrescente')
    

