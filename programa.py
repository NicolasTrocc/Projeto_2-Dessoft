from funcoes import *
cartela = {
    'regra_simples': {
        1: -1,
        2: -1,
        3: -1,
        4: -1,
        5: -1,
        6: -1   },
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1   }
        }               
imprime_cartela(cartela)


regra_simples = ['1', '2', '3', '4', '5', '6']
regra_avancada = ['sem_combinacao', 'quadra', 'full_house', 'sequencia_baixa', 'sequencia_alta', 'cinco_iguais']
comandos = ['0', '1', '2', '3', '4']

jogada = 0 #começa a contar
while jogada < 12:
    dados_rolados = rolar_dados(5)  #primeira rolagem
    dados_guardados = []
    rerroladas = 0

    continua = True
    while continua:
        print(f'Dados rolados: {dados_rolados}')
        print(f'Dados guardados: {dados_guardados}')
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        acao = input()
        while acao not in comandos:
            print('Opção inválida. Tente novamente.')
            acao = input()
        else:
            if acao == '1':                    
                print("Digite o índice do dado a ser guardado (0 a 4):")
                vai_guardar = input()
                guardar = guardar_dado(dados_rolados, dados_guardados, int(vai_guardar))
                dados_rolados = guardar[0]
                dados_guardados = guardar[1]
            elif acao =='2':             
                print("Digite o índice do dado a ser removido (0 a 4):")
                vai_remover = input()
                remover = remover_dado(dados_rolados, dados_guardados, int(vai_remover))
                dados_rolados = remover[0]
                dados_guardados = remover[1]
            elif acao == '3':             
                if rerroladas >= 2:
                    print("Você já usou todas as rerrolagens.")
                else: 
                    quantidade = len(dados_rolados)
                    dados_rolados = rolar_dados(quantidade) 
                    rerroladas += 1
            elif acao == '4':             
                imprime_cartela(cartela)
            elif acao == '0': 
                todos = dados_guardados + dados_rolados
                categoria_valida = False
                print("Digite a combinação desejada:")
                while not categoria_valida:
                    categoria = input()
                    if categoria in regra_simples:
                        opcao = int(categoria)
                        if cartela['regra_simples'][opcao] == -1:
                            cartela = faz_jogada(todos, opcao, cartela)
                            categoria_valida = True
                        else:
                            print("Essa combinação já foi utilizada.")
                    elif categoria in regra_avancada:
                        if cartela['regra_avancada'][categoria] == -1:
                            cartela = faz_jogada(todos, categoria, cartela)
                            categoria_valida = True
                        else:
                            print("Essa combinação já foi utilizada.")
                    else:
                        print("Combinação inválida. Tente novamente.")


                continua = False
    jogada += 1  
   
        

imprime_cartela(cartela)

total_pontos = sum(ponto for ponto in cartela['regra_simples'].values()) + sum(ponto for ponto in cartela['regra_avancada'].values())

pontos_simples = sum(ponto for ponto in cartela['regra_simples'].values())
if pontos_simples >= 63:
    total_pontos += 35

print(f"Pontuação total: {total_pontos}")