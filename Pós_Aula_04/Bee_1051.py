sal = float(input())

if sal > 0 and sal <= 2000:
    print('Isento')
elif sal > 2000 and sal <= 3000:
    sal_novo = ((sal-2000) * 8) / 100
    print('R$ {:.2f}'.format(sal_novo))
elif sal <= 4500 and sal > 3000:
    sal_novo = (((sal - 3000) * 18) / 100) + (1000*0.08)
    print('R$ {:.2f}'.format(sal_novo))
else:
    sal_novo = (((sal - 4500) * 28) / 100) + (1000*0.08) + (1500 * 0.18)
    print('R$ {:.2f}'.format(sal_novo))

#Imprima o texto "R$" seguido de um espaço e do valor total devido de Imposto de Renda, com duas casas após o ponto. Se o valor de entrada for menor ou igual a 2000, deverá ser impressa a mensagem "Isento".