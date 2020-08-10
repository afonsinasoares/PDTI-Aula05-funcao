# função para imprimir os valores
def escada(numero):
    parada_i = numero + 1
    resposta = ''
    for i in range(1, parada_i):
        parada_j = i + 1
        for j in range(1, parada_j):
            resposta += str(j) + ' '
        resposta += '\n'
    return resposta

## Inicio do algoritmo
numero = int(input('Digite um número: '))

print(escada(numero))
