# ans-data-pipeline
## Processo de itegração com API pública ANS

Neste processo foi feito a:

*Downloado dos arquivos de demonstrações contábeis dos últimos tês trimestres, utilizando IED Google Colab e a linguagem de programação Python

*Extração dos arquivos através de linguagem Python

*Identificação e processamento de arquivos que continham dados de Despesas com Eventos/Sinistros, utilizando linguagem de programação Python e a biblioteca Pandas

*Identificação automática e estruturação e normalização dos dados, com linguagem Python

*TRADE OFF técnico: Optou-se pelo processamento incremental dos arquivos ao invés da leitura completa em memória.
Essa decisão foi tomada considerando:

•	o grande volume potencial de dados trimestrais

•	limitações de memória em ambientes como Google Colab

•	maior escalabilidade e robustez do pipeline

#TRASNFORMAÇÃO E VALIDAÇÃO DOS DADOS

#### Validação de CNPJ

### Contexto
Durante a análise do dataset, verificou-se que **não existe coluna de CNPJ**
nem coluna de Razão Social na base disponibilizada.

### Decisão Técnica
Optou-se por **não criar artificialmente** colunas de CNPJ ou Razão Social,
evitando a introdução de dados inexistentes ou inferidos.

A pipeline foi construída de forma defensiva, aplicando validações
apenas quando as colunas relevantes estiverem presentes no dataset.

### Justificativa
Criar ou inferir CNPJs poderia comprometer a integridade, rastreabilidade
e confiabilidade das análises, especialmente em contextos financeiros
ou regulatórios.

### Prós
- Mantém fidelidade absoluta aos dados de origem
- Evita dados artificiais ou inferidos
- Pipeline resiliente e reutilizável
- Alinhado a boas práticas de engenharia de dados

### Contras
- Não é possível realizar análises por entidade jurídica
- Limita validações cadastrais enquanto o dado não existir

### Observação
Caso futuras versões do dataset incluam CNPJ ou Razão Social,
as validações já estão prontas para serem aplicadas automaticamente.


#IMPORTANDO ARQUIVOS DE DADOS CADASTRAIS DE OPERADORAS ATIVAS

## Limitações Estruturais dos Dados

Durante o processo de análise e transformação dos dados, foi identificada
uma limitação estrutural que impacta diretamente a possibilidade de integração
entre os conjuntos de dados disponíveis.

### Estrutura dos datasets analisados

- **consolidado_despesas.csv**
  - Colunas: `Trimestre`, `Ano`, `ValorDespesas`
  - Dados financeiros agregados em nível temporal
  - Não possui identificadores de operadoras (CNPJ, Razão Social ou UF)

- **Relatorio_cadop.csv**
  - Contém informações cadastrais das operadoras
  - Inclui campos como CNPJ, Razão Social e UF
  - Dados em nível granular por operadora

### Limitação identificada

Não existe uma chave comum confiável que permita a realização de um JOIN
relacional entre o dataset de despesas consolidadas e o dataset cadastral.
Em especial, o arquivo de despesas não contém CNPJ ou qualquer identificador
institucional que permita associar os valores financeiros a operadoras
específicas.

### Decisão técnica adotada

Optou-se por **não realizar integração relacional entre os datasets**, tratando-os
como fontes analíticas independentes, porém complementares:

- O consolidado de despesas é utilizado para análises macroeconômicas
  e temporais.
- O relatório cadastral (CADOP) é utilizado para análises institucionais
  e geográficas, como agrupamentos por Razão Social e UF.

Essa decisão preserva a integridade dos dados e evita associações incorretas
ou inferências estatísticas inválidas.

### Impactos da limitação

**Prós**
- Mantém consistência e confiabilidade dos dados
- Evita cruzamentos artificiais ou incorretos
- Segue boas práticas de modelagem e governança de dados

**Contras**
- Impede análises financeiras por operadora
- Limita o enriquecimento direto dos dados consolidados

A superação dessa limitação exigiria uma fonte adicional que relacionasse
valores financeiros a identificadores institucionais (ex.: CNPJ).


## Limitação no cálculo de despesas por operadora/UF

Apesar de existir um dataset cadastral contendo operadoras e suas respectivas
Unidades Federativas (UF), o dataset de despesas analisado apresenta valores
apenas em nível agregado por período (ano e trimestre).

Não há informação que relacione diretamente valores de despesas a CNPJs,
operadoras ou UFs. Dessa forma, não foi possível calcular o total de despesas
por operadora ou por UF sem introduzir suposições artificiais.

Qualquer tentativa de rateio ou distribuição proporcional dos valores
configuraria uma inferência estatística inválida. Assim, optou-se por não
realizar esse cálculo, preservando a integridade e confiabilidade da análise.


## Limitação no cálculo de médias por operadora e UF

O cálculo da média de despesas por trimestre para cada operadora ou Unidade
Federativa (UF) não pôde ser realizado, pois o dataset de despesas apresenta
valores apenas em nível agregado por período, sem identificação de operadoras.

Não existe relacionamento direto entre os valores financeiros e os dados
cadastrais disponíveis. Qualquer tentativa de distribuição das despesas por
operadora ou UF exigiria suposições artificiais, o que comprometeria a validade
estatística da análise.

Dessa forma, optou-se por calcular médias apenas em nível temporal (ano e
trimestre), preservando a integridade dos resultados.


## Limitação na identificação de operadoras com alta variabilidade de despesas

Foi avaliada a possibilidade de calcular o desvio padrão das despesas por
operadora, com o objetivo de identificar entidades com valores altamente
variáveis ao longo do tempo.

Entretanto, o dataset de despesas disponível apresenta valores apenas em nível
agregado por período (ano e trimestre), sem identificação de operadoras ou UFs.
Dessa forma, não é possível associar a variabilidade das despesas a operadoras
específicas.

Optou-se por calcular o desvio padrão apenas em nível temporal, permitindo a
análise da volatilidade global das despesas, sem comprometer a integridade dos
dados.

