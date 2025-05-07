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
    lista = sorted(set(numeros))  # remove duplicatas e ordena
    max_seq = seq = 1

    for i in range(1, len(lista)):
        if lista[i] == lista[i-1] + 1:
            seq += 1
            max_seq = max(max_seq, seq)
        else:
            seq = 1

    return 15 if max_seq >= 4 else 0

def calcula_pontos_sequencia_alta(numeros):
    lista = sorted(set(numeros))
    max_seq = seq = 1

    for i in range(1, len(lista)):
        if lista[i] == lista[i-1] + 1:
            seq += 1
            max_seq = max(max_seq, seq)
        else:
            seq = 1

    return 30 if max_seq >= 5 else 0

def calcula_pontos_full_house(numeros):
    soma = 0
    dicio = {}
    for i in numeros:
        if i in dicio:
            dicio[i] += 1
        else:
            dicio[i] = 1
    if 3 in dicio.values() and 2 in dicio.values():
        for i in numeros:
            soma += i
    return soma

def calcula_pontos_quadra(numeros):
    soma = 0
    dicio = {}
    for i in numeros:
        if i in dicio:
            dicio[i] += 1
        else:
            dicio[i] = 1
    
    for a in dicio.values():
        if a >= 4:
            for l in numeros:
                soma += l
            break

    return soma

def calcula_pontos_quina(numeros):
    dicio = {}
    for i in numeros:
        if i in dicio:
            dicio[i] += 1
        else:
            dicio[i] = 1
    sim = 0
    for a in dicio.values():
        if a >= 5:
            sim = 50
    return sim

def calcula_pontos_regra_avancada(numeros):
    
    cinco_iguais = calcula_pontos_quina(numeros[:])
    full_house = calcula_pontos_full_house(numeros[:])
    quadra = calcula_pontos_quadra(numeros[:])
    sem_combinacao = calcula_pontos_soma(numeros[:])
    sequencia_baixa = calcula_pontos_sequencia_baixa(numeros[:])
    sequencia_alta = calcula_pontos_sequencia_alta(numeros[:])
    
    terminal = {
    'sem_combinacao': sem_combinacao,
    'quadra': quadra,
    'full_house': full_house,
    'sequencia_baixa': sequencia_baixa,
    'sequencia_alta': sequencia_alta,
    'cinco_iguais': cinco_iguais,
        }
    return terminal

def faz_jogada(dados, categoria, cartela):

    if categoria in ['1','2','3','4','5','6']:
        categoria = int(categoria)
        pontos_simples = calcula_pontos_regra_simples(dados)
        cartela["regra_simples"][categoria] = pontos_simples[categoria]
    else:
        pontos_avancados = calcula_pontos_regra_avancada(dados)
        cartela["regra_avancada"][categoria] = pontos_avancados[categoria]
        
    return cartela

def imprime_cartela(cartela):
    print("Cartela de Pontos:")
    print("-"*25)    
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_simples'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    for i in cartela['regra_avancada'].keys():
        filler = " " * (15 - len(str(i)))
        if cartela['regra_avancada'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_avancada'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    print("-"*25)


