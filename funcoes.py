
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