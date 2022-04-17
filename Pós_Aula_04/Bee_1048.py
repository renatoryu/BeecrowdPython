sal = float(input())

if sal <= 400 and sal >= 0:
    reajuste = 0.15 * sal
    sal_novo = sal + reajuste
    print('Novo salario: {:.2f}'.format(sal_novo))
    print('Reajuste ganho: {:.2f}'.format(reajuste))
    print('Em percentual: 15 %')
elif sal <= 800 and sal > 400:
    reajuste = 0.12 * sal
    sal_novo = sal + reajuste
    print('Novo salario: {:.2f}'.format(sal_novo))
    print('Reajuste ganho: {:.2f}'.format(reajuste))
    print('Em percentual: 12 %')
elif sal <= 1200 and sal > 800:
    reajuste = 0.10 * sal
    sal_novo = sal + reajuste
    print('Novo salario: {:.2f}'.format(sal_novo))
    print('Reajuste ganho: {:.2f}'.format(reajuste))
    print('Em percentual: 10 %')
elif sal <= 2000 and sal >= 1200:
    reajuste = 0.07 * sal
    sal_novo = sal + reajuste
    print('Novo salario: {:.2f}'.format(sal_novo))
    print('Reajuste ganho: {:.2f}'.format(reajuste))
    print('Em percentual: 7 %')
else:
    reajuste = 0.04 * sal
    sal_novo = sal + reajuste
    print('Novo salario: {:.2f}'.format(sal_novo))
    print('Reajuste ganho: {:.2f}'.format(reajuste))
    print('Em percentual: 4 %')

#Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.