# Faça um programa, com uma função que necessite de três argumentos
# e que forneça a soma desses três argumentos
def soma(numero1,numero2, numero3):
    soma = numero1 + numero2 + numero3
    return soma

numero1 = int(input('Digite um valor inteiro: '))
numero2 = int(input('Digite um valor inteiro: '))
numero3 = int(input('Digite um valor inteiro: '))

print(soma(numero1,numero2,numero3))