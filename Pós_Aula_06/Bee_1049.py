tipo = input().lower()
especie = input().lower()
alimentacao = input().lower()

if tipo == 'vertebrado':
    if especie =='ave':
        if alimentacao == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    else:
        if alimentacao == 'onivoro':
            print('homem')
        else:
            print('vaca')
else:
    if especie =='inseto':
        if alimentacao == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    else:
        if alimentacao == 'hematofago':
            print('sanguessuga')
        else:
            print('minhoca')
        
# Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda para a direita.  Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.