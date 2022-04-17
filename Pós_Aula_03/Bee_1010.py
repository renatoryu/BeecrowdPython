linha1 = input().split(" ")
linha2 = input().split(" ")
cod1, qtde1, valor1 = linha1
cod2, qtde2, valor2 = linha2
total = (int(qtde1) * float(valor1)) + (int(qtde2) * float(valor2))
print('VALOR A PAGAR: R$ {:.2f}'.format(total))

#A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando de deixar um espaço após os dois pontos e um espaço após o "R$". O valor deverá ser apresentado com 2 casas após o ponto.