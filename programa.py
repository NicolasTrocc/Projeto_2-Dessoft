from funcoes import *

cartela = {
    'regra_simples': {
        1: -1,
        2: -1,
        3: -1,
        4: -1,
        5: -1,
        6: -1
    },
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}
imprime_cartela(cartela)

regra_simples = ['1', '2', '3', '4', '5', '6']
regra_avançada = ['sem_combinacao', 'quadra', 'full_house','sequencia_baixa', 'sequencia_alta', 'cinco_iguais']

<<<<<<< HEAD
jogada = 0
while jogada < 12:
    dados_rolados = rolar_dados(5)
=======
jogada = 0 #começa a contar
while jogada < 12:
    dados_rolados = rolar_dados(5)  #primeira rolagem
>>>>>>> 3dc746109b6eeb1c2cc44b15bcd14de0b024ffd9
    dados_guardados = []
    rerrolagens = 0
    jogando = True

    while jogando:
        print(f'Dados rolados: {dados_rolados}')
        print(f'Dados guardados: {dados_guardados}')
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        acao = input()

        while acao not in ['0', '1', '2', '3', '4']:
            print("Opção inválida. Tente novamente.")
            acao = input()
        if acao == '1':
            print("Digite o índice do dado a ser guardado (0 a 4):")
            guardado = int(input())
            dados_rolados, dados_guardados = guardar_dado(dados_rolados, dados_guardados, guardado)
        elif acao == '2':
            print("Digite o índice do dado a ser removido (0 a 4):")
            removido = int(input())
            dados_rolados, dados_guardados = remover_dado(dados_rolados, dados_guardados, removido)
        elif acao == '3':
            if rerrolagens >= 2:
                print("Você já usou todas as rerrolagens.")
            else:
                dados_rolados = rolar_dados(len(dados_rolados))
                rerrolagens += 1
        elif acao == '4':
            imprime_cartela(cartela)
        elif acao == '0':
            dados_totais = dados_guardados + dados_rolados
            validacao = False
            print("Digite a combinação desejada:")
            while not validacao:
                combinacao = input()
                if combinacao in regra_simples:
                    combinacaoi = int(combinacao)
                    if cartela['regra_simples'][combinacaoi] == -1:
                        cartela = faz_jogada(dados_totais, combinacao, cartela)
                        validacao = True
                    else:
                        print("Essa combinação já foi utilizada.")
                elif combinacao in regra_avançada:
                    if cartela['regra_avancada'][combinacao] == -1:
                        cartela = faz_jogada(dados_totais, combinacao, cartela)
                        validacao = True
                    else:
                        print("Essa combinação já foi utilizada.")
                else:
                    print("Combinação inválida. Tente novamente.")
            jogando = False
    jogada += 1

imprime_cartela(cartela)
total_pontos = 0
bonus = 0

for pontos in cartela['regra_simples'].values():
    if pontos != -1:
        total_pontos += pontos
        bonus += pontos
for pontos in cartela['regra_avancada'].values():
    if pontos != -1:
        total_pontos += pontos
if bonus >= 63:
    total_pontos += 35

print(f"Pontuação total: {total_pontos}")