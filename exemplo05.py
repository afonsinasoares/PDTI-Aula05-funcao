def somar(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    return resultado

teste = somar(1, 10,100, 1000)

print("A soma é", teste)