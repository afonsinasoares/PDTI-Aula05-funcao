def avaliar_numero(numero:int):
    positivo = numero > 0
    if positivo:
        return 'Positivo'
    else:
        return 'Negativo'

valor = int(input('Digite um numero: '))

print(avaliar_numero(valor))