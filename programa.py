from funcoes import *

cartela = {
    "regra_simples": {
        1: -1,
        2: -1,
        3: -1,
        4: -1,
        5: -1,
        6: -1
    },
    "regra_avancada": {
        "sem_combinacao":-1,
        "quadra":-1,
        "full_house":-1,
        "sequencia_baixa":-1,
        "sequencia_alta":-1, 
        "cinco_iguais":-1, 
    }
}

jogadas = 1

categorias_numero = ['1','2','3','4','5','6']

while jogadas <= 12:
    n = 5
    dados_rolados = rolar_dados(n)
    guardados = []
    rerrolagens = 0
    imprime_cartela(cartela)
    
    print(f'Dados rolados: {dados_rolados}')
    print(f'Dados guardados: {guardados}')
    
    acao = int(input('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação: '))
    
    while acao != 0: 
        if acao == 1: 
            indice = int(input("Digite o índice do dado a ser guardado (0 a 4): "))
            dado_guardado = dados_rolados.pop(indice)
            guardados.append(dado_guardado)
    
        elif acao == 2:
            indice = int(input("Digite o índice do dado a ser removido (0 a 4): "))
            dado_removido = guardados.pop(indice)
            dados_rolados.append(dado_removido)
    
        elif acao == 3:
            if rerrolagens < 2:
                rerrolagens += 1
                dados_rolados = rolar_dados(5 - len(guardados))
                            
            else:
                print("Você já usou todas as rerrolagens.")

        elif acao == 4:
            imprime_cartela(cartela)
        
        else:
            print("Opção inválida. Tente novamente.")

        print(dados_rolados)
        print(guardados)

        acao = int(input('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação: '))

    if acao == 0:
        categoria = input("Digite a combinação desejada: ")
        print(cartela['regra_simples'])
        if categoria in categorias_numero:
            categoria = int(categoria)
            cartela = faz_jogada(guardados, categoria, cartela)
        elif categoria in cartela['regra_avancada']:
            cartela = faz_jogada(guardados, categoria, cartela)
        else:
            print("Combinação inválida. Tente novamente.")
        jogadas += 1
