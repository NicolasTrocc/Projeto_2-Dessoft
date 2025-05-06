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
regra_avancada = ['sem_combinacao', 'quadra', 'full_house', 'sequencia_baixa', 'sequencia_alta', 'cinco_iguais']

rodada = 0
while rodada < 12:
    rerrolagens = 0
    dados_rolados = rolar_dados(5)
    dados_guardados = []
    rodada_continua = True

    while rodada_continua:
        print(f'Dados rolados: {dados_rolados}')
        print(f'Dados guardados: {dados_guardados}')
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        acao = input()

        while acao not in ['0', '1', '2', '3', '4']:
            print('Opção inválida. Tente novamente.')
            acao = input()

        if acao == '1':
            print("Digite o índice do dado a ser guardado (0 a 4):")
            guardados = input()
            if guardados.strip().isnumeric():
                indice = int(guardados)
                if 0 <= indice < len(dados_rolados):
                    guardar = guardar_dado(dados_rolados, dados_guardados, indice)
                    dados_rolados = guardar[0]
                    dados_guardados = guardar[1]
                else:
                    print("Índice fora do intervalo.")
            else:
                print("Entrada inválida.")

        elif acao == '2':
            print("Digite o índice do dado a ser removido (0 a 4):")
            remover = input()
            if remover.strip().isnumeric():
                indice = int(remover)
                if 0 <= indice < len(dados_guardados):
                    pos_remover = remover_dado(dados_rolados, dados_guardados, indice)
                    dados_rolados = pos_remover[0]
                    dados_guardados = pos_remover[1]
                else:
                    print("Índice fora do intervalo.")
            else:
                print("Entrada inválida.")

        elif acao == '3':
            if rerrolagens >= 2:
                print("Você já usou todas as rerrolagens.")
            else:
                qtd = len(dados_rolados)
                dados_rolados = rolar_dados(qtd)
                rerrolagens += 1

        elif acao == '4':
            imprime_cartela(cartela)

        elif acao == '0':
            dados_totais = dados_guardados + dados_rolados
            categoria_valida = False
            print("Digite a combinação desejada:")

            while not categoria_valida:
                categoria = input()
                if categoria in regra_simples:
                    num = int(categoria)
                    if cartela['regra_simples'][num] == -1:
                        cartela = faz_jogada(dados_totais, num, cartela)
                        categoria_valida = True
                    else:
                        print("Essa combinação já foi utilizada.")
                elif categoria in regra_avancada:
                    if cartela['regra_avancada'][categoria] == -1:
                        cartela = faz_jogada(dados_totais, categoria, cartela)
                        categoria_valida = True
                    else:
                        print("Essa combinação já foi utilizada.")
                else:
                    print("Combinação inválida. Tente novamente.")

            rodada_continua = False

    rodada += 1

imprime_cartela(cartela)

total_pontos = sum(p for p in cartela['regra_simples'].values()) + sum(p for p in cartela['regra_avancada'].values())

pontos_simples = sum(p for p in cartela['regra_simples'].values())
if pontos_simples >= 63:
    total_pontos += 35

print(f"Pontuação total: {total_pontos}")