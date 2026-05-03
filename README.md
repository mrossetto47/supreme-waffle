# Projeto: Identificador de Idioma por Frequência de Letras

## Funcionamento:

 Este projeto utiliza o módulo *requests* para fazer uma requisição HTTP em uma URL fornecida pelo usuário.

 O texto principal da página é baixado e limpo utilizando o módulo *trafilatura*.

 O programa então organiza e conta a frequência de ocorrência de cada letra no texto.

 Essa frequência é utilizada para comparar o texto com perfis pré-existentes de alguns idiomas, vetorizando as variáveis e utilizando o módulo *numpy* para calcular a distância de cosseno entre o perfil padrão e o da URL.

 Dessa forma é possível estimar o idioma mais semelhante com o texto da página e o grau de similaridade percentual.

 ## Instruções:

 1. Verifique se você possui o Python instalado. Caso tenha dúvidas, siga as instruções na documentação oficial ou no site:

    https://realpython-com.translate.goog/installing-python/?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt&_x_tr_pto=tc
 
 2. Descompacte todos os arquivos do .zip para uma pasta em seu computador.

 3. Utilizando o terminal, navegue até a pasta na qual o projeto foi salvo e execute o comando:
    
    **pip install -r requirements.txt**

    Isso garantirá que todos os pacotes necessários para o funcionamento estejam instalados no seu computador.

4. Execute o script principal navegando até a pasta raiz via terminal e executando o comando:

   **python3 src/ID_idioma_URL.py**

5. Siga as instruções apresentadas no terminal.

## Observações:

- O arquivo perfis.csv possui as informações sobre os perfis de frequência de letra para cada idioma.

- A pasta exemplos possui alguns exemplos de execução do programa e URLs sugeridas para teste.

- Atualmente, o programa suporta apenas os idiomas: **Português, Inglês, Francês e Alemão**. Mais idiomas podem ser adicionados modificando o arquivo functions.py e perfis,csv.
