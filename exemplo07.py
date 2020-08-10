# crie um algoritmo que informe se o número é primo ou não
def eh_primo(numero):
    parada = numero + 1
    contador = 0
    for n in range(1, parada):
        if numero % n == 0:
            contador += 1
        if contador == 3:
            break
    # if contador == 1 or contador > 2:
    #     return False
    # else:
    #     return True
    return contador == 2
numero = input('Informe um número: ')
numero = int(numero)

if eh_primo(numero):
    print('O número é primo')
else:
    print('O número não é primo')