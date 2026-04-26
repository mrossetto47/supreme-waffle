#======================================================================================================================================================
# Nome do arquivo: functions.py
# Descrição: Este arquivo contém as funções necessárias para baixar o texto de uma página da web e extrair o texto limpo usando módulo trafilatura.
#=======================================================================================================================================================

# Importando as bibliotecas necessárias:
import requests
from bs4 import BeautifulSoup
import trafilatura

#---------------------------------------------------------------------------------------------------------------
# Função baixar_texto(url) – retorna o texto bruto da página.
# Requisitos: Trate possíveis erros: URL inválida, falha de conexão, conteúdo não textual, etc.
#---------------------------------------------------------------------------------------------------------------
def baixar_texto(url=str):
    try:
        # Verificar se a URL é válida
        if not url.startswith(('http://', 'https://')):
            raise ValueError("URL inválida. Certifique-se de incluir 'http://' ou 'https://' no início da URL.")
        
        # Fazer a requisição HTTP para obter o conteúdo da página
        texto = requests.get(url)
        texto.raise_for_status()  # Verificar se a requisição foi bem-sucedida
        return texto.text
    
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a URL: {e}")
    except ValueError as ve:
        print(ve)
    except Exception as ex:
        print(f"Ocorreu um erro inesperado: {ex}") 
#---------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------
# Função limpar_texto(texto) – remove tudo que não é letra, converte para minúsculas, remove acentos. 
# Requisitos: A limpeza deve ignorar números, pontuação, espaços e caracteres especiais. 
#---------------------------------------------------------------------------------------------------------------
def limpar_texto(texto=str):
    try:
        # Usar trafilatura para extrair o texto limpo da página
        texto_limpo = trafilatura.extract(texto)     
        return texto_limpo
    
    except Exception as ex:
        print(f"Ocorreu um erro ao limpar o texto: {ex}")
#---------------------------------------------------------------------------------------------------------------


a = baixar_texto("https://www.letras.mus.br/avenged-sevenfold/hail-to-the-king/") 

b = limpar_texto(a)

print(b)
