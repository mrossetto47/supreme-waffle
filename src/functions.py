#======================================================================================================================================================
# Nome do arquivo: functions.py
# Descrição: Este arquivo contém as funções necessárias para baixar o texto de uma página da web e extrair o texto limpo usando módulo trafilatura.
#=======================================================================================================================================================

# Importando as bibliotecas necessárias:
import requests
import trafilatura
import csv
import numpy as np
from unidecode import unidecode





#---------------------------------------------------------------------------------------------------------------
# Função baixar_texto(url) – retorna o texto bruto da página.
# Requisitos: Trate possíveis erros: URL inválida, falha de conexão, conteúdo não textual, etc.
#---------------------------------------------------------------------------------------------------------------
def baixar_texto(url=str):
    err_code = "OK" # Variável para armazenar o código de erro, inicializada como "OK" para indicar que não houve erros inicialmente
    try:
        # Verificar se a URL é válida
        if not url.startswith(('http://', 'https://')):
            raise ValueError("URL inválida. Certifique-se de incluir 'http://' ou 'https://' no início da URL.")
        
        # Fazer a requisição HTTP para obter o conteúdo da página
        texto = requests.get(url)
        texto.raise_for_status()  # Verificar se a requisição foi bem-sucedida
        return texto.text
    
    # Tratamento de erros:
    
    # Erros de conexão, como falha ao acessar a URL ou tempo limite de resposta:
    except requests.exceptions.RequestException as e:
        print("--------------------------------------------------------------------------------------\n"
            "\nUm erro ocorreu ao acessar a URL ou baixar o conteúdo textual:")
        print(f"Erro ao acessar a URL: {e}\n")
        print("--------------------------------------------------------------------------------------\n")
        err_code = "ERR1"  # Atribuir um código de erro específico para falha de conexão
        return err_code  # Retornar "ERR1" para indicar que houve um erro ao acessar a URL ou baixar o conteúdo textual   
    
    # Erros de valor, como URL inválida:
    except ValueError as ve:
        print("--------------------------------------------------------------------------------------\n"
            "\nUm erro ocorreu ao acessar a URL ou baixar o conteúdo textual:")        
        print(f"Erro de valor: {ve}\n")
        print("--------------------------------------------------------------------------------------\n")
        err_code = "ERR2"  # Atribuir um código de erro específico para erro de valor
        return err_code  # Retornar "ERR2" para indicar que houve um erro de valor

    # Outros erros inesperados: 
    except Exception as ex:
        print("--------------------------------------------------------------------------------------\n")
        print(f"Ocorreu um erro inesperado: {ex}\n")
        print("--------------------------------------------------------------------------------------\n") 
        err_code = "ERR3"  # Atribuir um código de erro específico para erro inesperado
        return err_code  # Retornar "ERR3" para indicar que houve um erro inesperado

#---------------------------------------------------------------------------------------------------------------





#---------------------------------------------------------------------------------------------------------------
# Função limpar_texto(texto) – remove tudo que não é letra, converte para minúsculas, remove acentos. 
# Requisitos: A limpeza deve ignorar números, pontuação, espaços e caracteres especiais. 
#---------------------------------------------------------------------------------------------------------------
def limpar_texto(texto=str):
    error_code = "OK"  # Variável para armazenar o código de erro, inicializada como "OK" para indicar que não houve erros inicialmente
    try:
        # Usar trafilatura para extrair o texto limpo da página, excluindo HTML, scripts, estilos e outros elementos não textuais.
        # Configurar trafilatura para extrair apenas o texto principal da página, ignorando elementos como anúncios, rodapés, comentários etc.
        texto_limpo = trafilatura.extract(texto, include_links=False, include_images=False)     
        
        # Verificar se o texto limpo foi extraído corretamente
        if texto_limpo is None:
            raise ValueError("Não foi possível extrair o texto limpo. Verifique o conteúdo da página.")
        
        # Converter o texto para minúsculas
        texto_limpo = texto_limpo.lower()

        # Remover acentos usando a biblioteca unidecode
        texto_limpo = unidecode(texto_limpo)

        return texto_limpo
    
    except Exception as ex:
        print("--------------------------------------------------------------------------------------\n")
        print(f"Ocorreu um erro ao limpar o texto: {ex}")
        print("--------------------------------------------------------------------------------------\n")
        return "ERR1"  # Retornar "ERR1" para indicar que houve um erro ao limpar o texto
    
#---------------------------------------------------------------------------------------------------------------





#---------------------------------------------------------------------------------------------------------------
# Função calcular_frequencia(texto_limpo) – retorna um dicionário {letra: percentual}.
# Requisitos: O percentual deve ser calculado com base no total de letras (ignorando espaços, pontuação, números e caracteres especiais).
#---------------------------------------------------------------------------------------------------------------
def calcular_frequencia(texto_limpo=str):
    error_code = "OK"  # Variável para armazenar o código de erro, inicializada como "OK" para indicar que não houve erros inicialmente
    try:
        # Criar um dicionário para armazenar a contagem de cada letra
        frequencia = {}
        total_letras = 0
        
        # Contar a frequência de cada letra no texto limpo
        for char in texto_limpo:
            if char.isalpha():  # Verificar se o caractere é uma letra
                total_letras += 1
                if char in frequencia:
                    frequencia[char] += 1
                else:
                    frequencia[char] = 1
        
        # Calcular o percentual de cada letra com base no total de letras
        percentual_frequencia = {letra: (contagem / total_letras) * 100 for letra, contagem in frequencia.items()}

        # Verificar se o total de letras é maior que zero para evitar divisão por zero
        if total_letras == 0:
            raise ValueError("O texto limpo não contém letras para calcular a frequência.")
        
        # Ordenar o dicionário de frequência em ordem alfabética
        percentual_frequencia = dict(sorted(percentual_frequencia.items()))

        # Deixar o percentual com três casas decimais para melhor visualização
        percentual_frequencia = {letra: round(percentual, 3) for letra, percentual in percentual_frequencia.items()}

        # Retornar o dicionário com o percentual de frequência de cada letra em formato {letra: percentual}      
        return percentual_frequencia

    except Exception as ex:
        print("--------------------------------------------------------------------------------------\n")
        print(f"Ocorreu um erro ao calcular a frequência: {ex}")
        print("--------------------------------------------------------------------------------------\n")
        return "ERR1"  # Retornar "ERR1" para indicar que houve um erro ao calcular a frequência
#---------------------------------------------------------------------------------------------------------------




#---------------------------------------------------------------------------------------------------------------
# Função Função carregar_perfis() – carrega os perfis de referência (do arquivo de dados data/perfis.csv).
# Requisitos: 
#   A função deve ler o arquivo CSV e retornar dicionários para cada idioma e sua respectiva frequência de letras.
#   Depois, os dicionários serão usados para comparar com o perfil de frequência do texto analisado e determinar a língua mais provável.
#   No arquivo CSV, cada coluna representa um idioma e cada linha representa a frequência de uma letra específica
#   A primeira linha é o cabeçalho com os nomes dos idiomas e a primeira coluna é a letra correspondente
# Observação:
#   Caso deseje utilizar perfis personalizados, edite o arquivo CSV (data/perfis.csv) para incluir os perfis de frequência de letras para os idiomas desejados.
#    No momento, a biblioteca vai importar os perfis para português, alemão e francês.
#---------------------------------------------------------------------------------------------------------------

def carregar_perfis():

    error_code = "OK"  # Variável para armazenar o código de erro, inicializada como "OK" para indicar que não houve erros inicialmente
    
    # Deve existir um dicionário para cada idioma, onde a chave é a letra e o valor é o percentual de frequência dessa letra no idioma correspondente.
    # Criar um dicionário para armazenar os perfis de cada idioma atualmente suportado:
    perfil_portugues = {}
    perfil_alemao = {}
    perfil_frances = {}
    perfil_ingles = {}

    # Lembrete: os nomes no arquivo estão em inglês (Letter, Portuguese, German, French, etc.)
    # Vamos criar um dicionário para converter os nomes dos idiomas do arquivo CSV para os nomes em português:
    idiomas_csv = {
        'Portuguese': 'Português',
        'German': 'Alemão',
        'French': 'Francês',
        'English': 'Inglês'
    }

    try:

        # Abrir o arquivo CSV com o módulo csv em modo leitura:
        with open('data/perfis.csv', mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')  # Usar o delimitador ';' para ler o arquivo corretamente

            # Verificar se o arquivo CSV foi lido corretamente
            if reader.fieldnames is None:
                raise ValueError("O arquivo CSV não contém um cabeçalho válido. Verifique o formato do arquivo 'data/perfis.csv'.")
            # Verificar se os idiomas esperados estão presentes no cabeçalho do CSV
            for idioma in idiomas_csv.keys():
                if idioma not in reader.fieldnames:
                    raise ValueError(f"O idioma '{idioma}' não foi encontrado no cabeçalho do arquivo CSV. Verifique o formato do arquivo 'data/perfis.csv'.")
        
            # Ler cada linha do arquivo CSV e preencher os dicionários de perfis de cada idioma.
            # A primeira coluna é a letra correspondente, e as colunas seguintes são os percentuais de frequência para cada idioma.
            # Ignorar a primeira linha (cabeçalho) e processar as linhas seguintes para preencher os dicionários de perfis de cada idioma.
            # Ler apenas até a letra 'z' para garantir que estamos processando apenas as letras do alfabeto, sem incluir caracteres especiais ou acentos.
            for row in reader:
                letra = row['Letter'].lower()  # Obter a letra da primeira coluna e converter para minúscula

                # Preencher os dicionários de perfis de cada idioma com a letra e seu respectivo percentual de frequência
                for idioma_csv, idioma_busca in idiomas_csv.items():
                    if letra.isalpha() and letra <= 'z':  # Verificar se a letra é uma letra do alfabeto (a-z)
                        percentual = float(row[idioma_csv].replace('%', '').strip())  # Remover o símbolo '%' e converter para float
                        if idioma_busca == 'Português':
                            perfil_portugues[letra] = percentual
                        elif idioma_busca == 'Alemão':
                            perfil_alemao[letra] = percentual
                        elif idioma_busca == 'Francês':
                            perfil_frances[letra] = percentual
                        elif idioma_busca == 'Inglês':
                            perfil_ingles[letra] = percentual
        # Retornar os dicionários de perfis de cada idioma:
        return {
            'Português': perfil_portugues,
            'Alemão': perfil_alemao,
            'Francês': perfil_frances,
            'Inglês': perfil_ingles
        }
             
    # Tratamento de erros:
    except FileNotFoundError:
        print("--------------------------------------------------------------------------------------\n")
        print("O arquivo 'data/perfis.csv' não foi encontrado. Verifique se o arquivo existe no caminho especificado.")
        print("--------------------------------------------------------------------------------------\n")
        return "ERR1"  # Retornar "ERR1" para indicar que houve um erro ao encontrar o arquivo CSV
    
    except ValueError as ve:
        print("--------------------------------------------------------------------------------------\n")
        print(ve)
        print("--------------------------------------------------------------------------------------\n")
        return "ERR2"  # Retornar "ERR2" para indicar que houve um erro de valor ao processar o arquivo CSV
    
    except Exception as ex:
        print("--------------------------------------------------------------------------------------\n")
        print(f"Ocorreu um erro ao carregar os perfis: {ex}")
        print("--------------------------------------------------------------------------------------\n")
        return "ERR3"  # Retornar "ERR3" para indicar que houve um erro inesperado ao carregar os perfis
#---------------------------------------------------------------------------------------------------------------



#---------------------------------------------------------------------------------------------------------------
# Função comparar_perfis(percentual_frequencia, perfis) – calcula a distância/similaridade e retorna o idioma mais próximo.
# Requisitos: A função vai calcular a similaridade por distância de cosseno utilizando numpy.
#   Ela vai receber o texto analisado da função calcular_frequencia()
#   e os perfis de referência da função carregar_perfis() para comparar e determinar a língua mais provável do texto analisado.
#   A função deve retornar o idioma mais próximo utilizando distância de cosseno.
#---------------------------------------------------------------------------------------------------------------
def comparar_perfis(percentual_frequencia, perfis):

    error_code = "OK"  # Variável para armazenar o código de erro, inicializada como "OK" para indicar que não houve erros inicialmente
    
    # Criar um dicionário para armazenar a similaridade de cada idioma com o perfil do texto analisado
    similaridade_idiomas = {}

    try:
        
        # Receber o dicionário de texto analisado da função calcular_frequencia() - Já vem em ordem alfabética
        # Transformar em vetor no numpy para calcular a distância de cosseno:
        letras = sorted(percentual_frequencia.keys())  # Obter as letras em ordem
        vetor_texto = np.array([percentual_frequencia[letra] for letra in letras])  # Criar o vetor do texto analisado

        # Receber os perfis de referência da função carregar_perfis() - Já vem em ordem alfabética
        # Criar um vetor para cada idioma no numpy para calcular a distância de cosseno:
        for idioma, perfil in perfis.items():
            vetor_perfil = np.array([perfil.get(letra, 0) for letra in letras])  # Criar o vetor do perfil do idioma (usar 0 para letras ausentes)

            # Calcular a distância de cosseno entre o vetor do texto analisado e o vetor do perfil do idioma
            # A distância de cosseno é calculada como:
            #    1 - (produto escalar dos vetores / (norma do vetor do texto analisado * norma do vetor do perfil do idioma))

            # Calcular o produto escalar dos vetores:
            produto_escalar = np.dot(vetor_texto, vetor_perfil)

            # Calcular a norma do vetor do texto analisado e do vetor do perfil do idioma:
            norma_texto = np.linalg.norm(vetor_texto)
            norma_perfil = np.linalg.norm(vetor_perfil)

            # Verificar se as normas são maiores que zero para evitar divisão por zero
            if norma_texto > 0 and norma_perfil > 0:
                distancia_cosseno = 1 - (produto_escalar / (norma_texto * norma_perfil))
            else:
                distancia_cosseno = 1  # Se uma das normas for zero, a distância de cosseno é máxima (1)

            # Armazenar a similaridade (distância de cosseno) do idioma com o perfil do texto analisado
            similaridade_idiomas[idioma] = distancia_cosseno

        # Determinar o idioma mais próximo com base na menor distância de cossseno e exceçáo se houver empate
        # Por isso, vamos utilizar loop e não a função min()
        idioma_mais_proximo = None
        menor_distancia = float('inf')  # Inicializar com infinito para encontrar a menor distância
        for idioma, distancia in similaridade_idiomas.items():
            if distancia < menor_distancia:
                menor_distancia = distancia
                idioma_mais_proximo = idioma
            elif distancia == menor_distancia:
                raise ValueError("Houve um empate na comparação de perfis. Dois ou mais idiomas apresentaram a mesma distância de cosseno mínima com o perfil do texto analisado.") 
            
     

        # Retornar o idioma mais próximo
        # Retornar o percentual de similaridade do idioma mais próximo para o texto analisado (opcional, pode ser útil para análise posterior)
        # percentual_similaridade = (1 - menor_distancia) * 100  # Converter a distância de cosseno para percentual de similaridade
        return idioma_mais_proximo, round((1 - menor_distancia) * 100, 3)  # Retornar o idioma mais próximo e o percentual de similaridade com três casas decimais

    # Tratamento de erros:

    # A função carregar_perfis() não foi executada, portanto os perfis de referência não estão disponíveis para comparação.
    except KeyError:
        print("--------------------------------------------------------------------------------------\n")
        print("Os perfis de referência não estão disponíveis. Certifique-se de executar a função 'carregar_perfis()' antes de comparar os perfis.")
        print("--------------------------------------------------------------------------------------\n")
        return "ERR1", "ERR1"  # Retornar "ERR1" para indicar que houve um erro de chave ao acessar os perfis de referência

    # Erros de valor, como divisão por zero ou empate na comparação de perfis:
    except ValueError as ve:
        print("--------------------------------------------------------------------------------------\n")
        print(ve)
        print("--------------------------------------------------------------------------------------\n")
        return "ERR2", "ERR2"  # Retornar "ERR2" para indicar que houve um erro de valor ao comparar os perfis

    # Outros erros inesperados:
    except Exception as ex:
        print("--------------------------------------------------------------------------------------\n")
        print(f"Ocorreu um erro ao comparar os perfis: {ex}")
        print("--------------------------------------------------------------------------------------\n")
        return "ERR3", "ERR3"  # Retornar "ERR3" para indicar que houve um erro inesperado ao comparar os perfis
    
#---------------------------------------------------------------------------------------------------------------

