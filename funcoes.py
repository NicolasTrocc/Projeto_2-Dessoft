
def rolar_dados(n):
    import random
    dados = n*[0]
    for v in range(n):
        numero = random.randint(1,6)
        dados[v] = (numero)
    return dados

def guardar_dado(dados_rolados, dados_guardados, vai_guardar):
    dados_novos = []
    for i in range(len(dados_guardados)):
        dados_novos.append(dados_guardados[i])
    dados_novos.append(dados_rolados[vai_guardar])
    del dados_rolados[vai_guardar]
    lista = [dados_rolados, dados_novos]
    return lista

def remover_dado(dados_rolados,dados_guardados, vai_sair):
    lista = []
    dados_rolados.append(dados_guardados[vai_sair])
    del dados_guardados[vai_sair]
    lista = [dados_rolados, dados_guardados]
    return lista

def calcula_pontos_regra_simples(numeros):
    dicio = {}
    #monta o dicio
    for i in range(6):
        dicio[i+1] = 0
    #adiciona valores ao dicio
    
    for p in range(len(numeros)):
        dicio[numeros[p]] += numeros[p]

    return dicio

def calcula_pontos_soma(numeros):
    soma = 0
    for i in range(len(numeros)):
        soma += numeros[i]

    return soma

def calcula_pontos_sequencia_baixa(numeros):
    pontos = 0
    #Deixa a lista crescente
    lista = []
    maxi = 0
    for i in range(len(numeros)):
        if numeros[i]>maxi:
            maxi = numeros[i]
    for i in range(len(numeros)):
        menor = maxi
        for p in range(len(numeros)):
            if numeros[p]<=menor:
                menor = numeros[p]
                indice = p
        del numeros[indice]
        if menor not in lista:
            lista.append(menor)
    #verifica se tem sequencia
    sequencia = 1
    for v in range(len(lista)-1):
        if lista[v+1] == lista[v]+1:
            sequencia += 1
        else:
            break
    if sequencia >= 4:
        pontos = 15
    return pontos

def calcula_pontos_sequencia_alta(numeros):
    pontos = 0
    #Deixa a lista crescente
    lista = []
    maxi = 0
    for i in range(len(numeros)):
        if numeros[i]>maxi:
            maxi = numeros[i]
    for i in range(len(numeros)):
        menor = maxi
        for p in range(len(numeros)):
            if numeros[p]<=menor:
                menor = numeros[p]
                indice = p
        del numeros[indice]
        if menor not in lista:
            lista.append(menor)
    #verifica se tem sequencia
    sequencia = 1
    for v in range(len(lista)-1):
        if lista[v+1] == lista[v]+1:
            sequencia += 1
        else:
            break
    if sequencia >= 5:
        pontos = 30
    return pontos