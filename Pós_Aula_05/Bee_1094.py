qntd_casos = int(input()) # quantidade de casos que serão digitados
c = 0 # coelho
r = 0 # rato
s = 0 # sapo

for cont in range(0, qntd_casos):  # vai pedir os testes até atingir o limite de casos especificados
    teste = input().split() # quantidade de casos + letra do animal -> Ex: 14 C | 14 Coelhos
    quantia, animal = teste # divide a variável teste para duas, do nome e da quantidade de animais
    if animal == 'C': # se a letra do animal for C de Coelho
        c = c + int(quantia) # variável c vai receber a quantidade mais o valor de c
    if animal == 'R': # se a letra do animal for R de Rato
        r = r + int(quantia) # variável r vai receber a quantidade mais o valor de r
    if animal == 'S':# se a letra do animal for S de Sapo
        s = s + int(quantia) # variável s vai receber a quantidade mais o valor de s

total = c + r + s # soma todos os experimentos com todos os animais

#porcentagem dos animais
porc_coelho = (c / total) * 100
porc_rato = (r / total) * 100
porc_sapo = (s / total) * 100

#mensagem
print('Total: {} cobaias'.format(total))
print('Total de coelhos: {}'.format(c))
print('Total de ratos: {}'.format(r))
print('Total de sapos: {}'.format(s))
print('Percentual de coelhos: {:.2f} %'.format(porc_coelho))
print('Percentual de ratos: {:.2f} %'.format(porc_rato))
print('Percentual de sapos: {:.2f} %'.format(porc_sapo))

#Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada e o percentual de cada uma em relação ao total de cobaias utilizadas, sendo que o percentual deve ser apresentado com dois dígitos após o ponto.