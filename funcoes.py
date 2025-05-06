
import funcoes 
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
        'cinco_iguais': -1   }         }               #cria uma cartela vazia
funcoes.imprime_cartela(cartela)


cats_regra_simples = ['1', '2', '3', '4', '5', '6']
cats_regra_avan = ['sem_combinacao', 'quadra', 'full_house', 'sequencia_baixa', 'sequencia_alta', 'cinco_iguais']


rodada = 0                  # inicia a contagem de rodadas 
while rodada < 12:
    ja_rerrolou = 0
    dados_rolados = funcoes.rolar_dados(5)          #rolagem inicial 
    dados_guardados = []
    rodada_continua = True
    while rodada_continua:
        print(f'Dados rolados: {dados_rolados}')
        print(f'Dados guardados: {dados_guardados}')
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        opcao = input()
        while opcao not in ['0', '1', '2', '3', '4']:
            print('Opção inválida. Tente novamente.')
            opcao = input()
        else:
            if opcao == '1':                    #programa para guardar o dado
                print("Digite o índice do dado a ser guardado (0 a 4):")
                dado_guardar = input()
                lista_pos_guardar = funcoes.guardar_dado(dados_rolados, dados_guardados, int(dado_guardar))
                dados_rolados = lista_pos_guardar[0]
                dados_guardados = lista_pos_guardar[1]
            elif opcao =='2':             #programa para remover o dado 
                print("Digite o índice do dado a ser removido (0 a 4):")
                dado_remover = input()
                lista_pos_remover = funcoes.remover_dado(dados_rolados, dados_guardados, int(dado_remover))
                dados_rolados = lista_pos_remover[0]
                dados_guardados = lista_pos_remover[1]
            elif opcao == '3':              #programa para rolar de novo (o ja_rerrolou é zerado a cada rodada)
                if ja_rerrolou >= 2:
                    print("Você já usou todas as rerrolagens.")
                else: 
                    qtd = len(dados_rolados)
                    dados_rolados = funcoes.rolar_dados(qtd) 
                    ja_rerrolou += 1
            elif opcao == '4':             #imprime a cartela
                funcoes.imprime_cartela(cartela)
            elif opcao == '0': 
                dados_totais = dados_guardados + dados_rolados
                cat_valida = False
                print("Digite a combinação desejada:")
                while not cat_valida:
                    cat = input()
                    if cat in cats_regra_simples:
                        num = int(cat)
                        if cartela['regra_simples'][num] == -1:
                            cartela = funcoes.faz_jogada(dados_totais, cat, cartela)
                            cat_valida = True
                        else:
                            print("Essa combinação já foi utilizada.")
                    elif cat in cats_regra_avan:
                        if cartela['regra_avancada'][cat] == -1:
                            cartela = funcoes.faz_jogada(dados_totais, cat, cartela)
                            cat_valida = True
                        else:
                            print("Essa combinação já foi utilizada.")
                    else:
                        print("Combinação inválida. Tente novamente.")


                rodada_continua = False
    rodada += 1  
   
        

funcoes.imprime_cartela(cartela)

total_pontos = sum(p for p in cartela['regra_simples'].values()) + sum(p for p in cartela['regra_avancada'].values())

pontos_simples = sum(p for p in cartela['regra_simples'].values())
if pontos_simples >= 63:
    total_pontos += 35

print(f"Pontuação total: {total_pontos}")