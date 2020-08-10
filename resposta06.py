# Faça um programa com uma função chamada somaImposto. A função
# possui dois parâmetros formais: taxaImposto, que é a quantia de imposto
# sobre vendas expressa em porcentagem e custo, que é o custo de um
# item antes do imposto. A função “altera” o valor de custo para incluir o
# imposto sobre vendas.

def converter(hora,minuto):
    if hora >= 12 and minuto>0:
        return str(hora - 12) + ':'+str(minuto)+' PM'
    else:
        return str(hora)+':'+str(minuto)+' AM'

hora = int(input('Digite a hora: '))
while hora > 24 or hora < 0:
    hora = int(input('Digite a hora: '))

minuto = int(input('Digite os minutos: '))
while minuto > 60 or hora < 0:
    minuto = int(input('Digite os minutos: '))

print(converter(hora,minuto))