nomes = ['josé', 'pedro','calros','simaão','josue']

def minha_funcao(caractere, lista):
    resultado = []
    for item in lista:
        if item.startswith(caractere):
            resultado.append(item)
    return resultado

# minha_funcao(letra, lista)
filtro = minha_funcao('j', nomes)

print(filtro)