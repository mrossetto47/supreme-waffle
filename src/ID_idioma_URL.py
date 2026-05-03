import functions  # Importar o módulo functions, que contém as funções necessárias para o programa

# Mensagem de boas-vindas
print("Bem-vindo ao identificador de idioma por URL!\n"
        "Este programa irá analisar o conteúdo textual de uma página web e identificar o idioma predominante com base na frequência das letras.\n"
        "\nPressione a tecla 'Enter' para continuar...")
input()  # Aguardar o usuário pressionar 'Enter'



# Carregar os perfis de frequência dos idiomas pré‑carregados
print("Carregando perfis de frequência dos idiomas...\n")
perfis = functions.carregar_perfis()  # Carregar os perfis de frequência dos idiomas pré‑carregados

# Limpar a tela do terminal
print("\033c", end="") # Limpar a tela do terminal

# Criar um loop para permitir que o usuário analise múltiplas URLs, saia do programa ou consulte mais comandos digitando 'options'
while True:
# Solicitar ao usuário que insira uma URL ou um comando
    usr_input = input("Digite uma URL para analisar, 'options' para ver os comandos disponíveis ou 'exit' para sair do programa:\n").strip()  # Solicitar ao usuário que insira uma URL ou um comando, e remover espaços em branco extras  

    if usr_input.lower() == 'exit':  # Verificar se o usuário deseja sair do programa
        print("Saindo do programa. Até mais!")
        break  # Sair 



    elif usr_input.lower() == 'options':  # Verificar se o usuário deseja ver os comandos disponíveis

        #Comandos disponíveis para o usuário:
        # 1. Digite uma URL para analisar o idioma predominante do conteúdo textual da página web.
        # 2. Digite 'options' para ver esta mensagem de ajuda novamente.
        # 3. Digite 'lang' para ver os idiomas disponíveis para análise.
        # 4. Digite 'clear' para limpar a tela do terminal.
        # 5. Digite 'exit' para sair do programa.   
            
        print("\nComandos disponíveis:\n"
            "1. Digite uma URL para analisar o idioma predominante do conteúdo textual da página web.\n"
            "2. Digite 'options' para ver esta mensagem de ajuda novamente.\n"
            "3. Digite 'lang' para ver os idiomas disponíveis para análise.\n"
            "4. Digite 'clear' para limpar a tela do terminal.\n"
            "5. Digite 'exit' para sair do programa.\n")
        
    
    elif usr_input.lower() == 'lang':  # Verificar se o usuário deseja ver os idiomas disponíveis para análise
        print("\nIdiomas disponíveis para análise:\n")
        for idioma in perfis.keys():  # Iterar sobre os idiomas disponíveis nos perfis carregados
            print(f"- {idioma}")  # Exibir cada idioma disponível para análise
        print()  # Adicionar uma linha em branco para melhor formatação da saída


    elif usr_input.lower() == 'clear':  # Verificar se o usuário deseja limpar a tela do terminal
        print("\033c", end="") # Limpar a tela do terminal  




    #Verificar se a entrada do usuário é uma URL válida (começa com "http://" ou "https://")
    elif usr_input.startswith("http") or usr_input.startswith("https"):
        print(f"Analisando a URL... {usr_input}")

        # Tentar  acessar a URL com a função baixar texto
        print("Tentando acessar a URL e baixar o conteúdo textual...\n")
        texto_bruto = functions.baixar_texto(usr_input)
        # Verificar se ocorreu um erro e voltar para o início
        if texto_bruto == "ERR1" or texto_bruto == "ERR2" or texto_bruto == "ERR3" or texto_bruto is None:  
            continue

        # Limpar o texto baixado usando a função limpar texto
        print("URL acessada com sucesso! \nLimpando o texto baixado...\n")  
        texto_limpo = functions.limpar_texto(texto_bruto)
        # Verificar se ocorreu um erro e voltar para o início
        if texto_limpo == "ERR1" or texto_limpo == "ERR2" or texto_limpo == "ERR3" or texto_limpo is None:  
            continue


        # Calcular a frequência relativa das letras usando a função calcular frequência
        print("Calculando a frequência relativa das letras no texto limpo...")
        frequencia_relativa = functions.calcular_frequencia(texto_limpo)
        # Verificar se ocorreu um erro e voltar para o início
        if frequencia_relativa == "ERR1" or frequencia_relativa == "ERR2" or frequencia_relativa == "ERR3" or frequencia_relativa is None:  
            continue

        # Identificar o idioma mais provável usando a função identificar idioma
        print("Identificando o idioma mais provável com base na frequência relativa das letras...")
        idioma_identificado, percentual_similaridade = functions. comparar_perfis(frequencia_relativa,perfis)   
        # Verificar se ocorreu um erro e voltar para o início
        if idioma_identificado == "ERR1" or percentual_similaridade == "ERR2":  
            continue
        
        # Exibir o resultado para o usuário
        print("------------------------------------------------------------------------------")
        print(f"\nO texto está provavelmente em {idioma_identificado} com grau de similaridade de {percentual_similaridade}%.\n")
        print("------------------------------------------------------------------------------")

        # Verificar se o grau de similaridade é baixo (abaixo de 70%) e alertar o usuário sobre a possibilidade de identificação imprecisa
        if percentual_similaridade < 70:
            print("ATENÇÃO: O grau de similaridade é baixo, o que pode indicar uma identificação imprecisa do idioma.\n"
            "Considere analisar outra URL ou verificar o conteúdo da página para obter melhores resultados.\n"
            "Dica: Utilize o comando 'lang' para ver os idiomas disponíveis para análise.\n")




    # Comandos não reconhecidos:
    else:
        print("Comando não reconhecido. Por favor, digite uma URL válida, 'options' para ver os comandos disponíveis ou 'exit' para sair do programa.\n")

 