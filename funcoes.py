
def rolar_dados(n):
    import random
    dados = n*[0]
    for v in range(n):
        numero = random.randint(1,6)
        dados[v] = (numero)
    return dados