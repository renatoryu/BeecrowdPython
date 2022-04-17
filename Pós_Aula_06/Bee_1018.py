valor= int (input())
cem=0
cinquenta=0
vinte=0
dez=0
cinco=0
dois=0
um=0 

print (valor) 

cem= valor // 100
valor = valor - (cem*100)
print(f"{cem} nota(s) de R$ 100,00")

cinquenta= valor // 50 
valor = valor - (cinquenta*50) 
print(f"{cinquenta} nota(s) de R$ 50,00")

vinte= valor // 20
valor = valor - (vinte*20) 
print(f"{vinte} nota(s) de R$ 20,00")

dez= valor // 10
valor = valor - (dez*10) 
print(f"{dez} nota(s) de R$ 10,00")

cinco= valor // 5
valor = valor - (cinco*5) 
print(f"{cinco} nota(s) de R$ 5,00")

dois= valor // 2
valor = valor - (dois*2) 
print(f"{dois} nota(s) de R$ 2,00")

um= valor // 1
valor = valor - (um*1) 
print(f"{um} nota(s) de R$ 1,00")

#Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.