# Exemplo de execução 1 : Website em idioma não disponível no programa

## Instruções:

1. Siga todo o passo-a-passo apresentado no arquivo README.md

2. Execute o programa e forneça a ele a URL:
    
    https://www.haaretz.co.il/


## Resultado esperado:

Este site está em Hebreu, um idioma não suportado pelo programa.

Assim, o resultado retornado é:

*O texto está provavelmente em Inglês com grau de similaridade de 55.444%.*

O programa tenta buscar na lista de perfis mais prováveis o idioma com maior similaridade, ainda que ela seja baixa.

Neste caso, ele encontrou o idioma **Inglês**.

Por padrão, quando a similaridade calculada fica inferior a **70%**, o programa dá um aviso:

*ATENÇÃO: O grau de similaridade é baixo, o que pode indicar uma identificação imprecisa do idioma.*
*Considere analisar outra URL ou verificar o conteúdo da página para obter melhores resultados.*
*Dica: Utilize o comando 'lang' para ver os idiomas disponíveis para análise.*

Porém, **CUIDADO:** 

Pode ser que nem sempre a similaridade fique baixa, mesmo o idioma não sendo um dos disponíveis no programa.

Nesses casos, principalmente quando os idiomas são correlatos ou muito próximos, a mensagem pode não ser exibida.

É preciso sempre analisar os resultados com cautela!