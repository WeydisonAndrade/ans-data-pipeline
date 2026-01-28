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


┌──────────────────────────┐
│      API Pública ANS     │
│  (Dados Abertos - ZIPs)  │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│        fase 1             │
│ Ingestão e Download      │
│ - Identifica trimestres  │
│ - Baixa arquivos         │
│ - Descompacta dados      │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│        fase 2             │
│ Processamento            │
│ - Leitura incremental    │
│ - Identifica sinistros   │
│ - Normaliza colunas      │
│ - Trata inconsistências  │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│        fase 3             │
│ Consolidação Final       │
│ - Unifica trimestres     │
│ - Resolve conflitos      │
│ - Gera CSV final         │
│ - Compacta em ZIP        │
└──────────────────────────┘

