# Análise de Ocorrências Aeronáuticas

Uma aplicação de análise exploratória e visualização de ocorrências aeronáuticas do Brasil, construída como protótipo usando Python, Streamlit e Plotly. Os dados utilizados estão na pasta `data/` — são arquivos CSV derivados de bases públicas (CENIPA) e notebooks de análise estão em `notebooks/`.

## 🎯 Objetivo
Fornecer uma interface rápida para explorar ocorrências, filtrar por aeronave, tipo de ocorrência e fator contribuinte, e gerar visualizações interativas que ajudem na investigação e comunicação de resultados.

## Tecnologias
- Python 3.8+
- Streamlit (interface web)
- Pandas (manipulação de dados)
- Plotly (visualizações interativas)

## Pré-requisitos
- Git
- Python 3.8 ou superior
- Recomenda-se criar um ambiente virtual (venv ou conda)

## Instalação (rápida)
Abra um terminal na raiz do projeto e execute:

```bash
# criar e ativar ambiente virtual (venv)
python -m venv .venv
source .venv/bin/activate

# instalar dependências
pip install -r requirements.txt
```

## Como executar

Para rodar a aplicação Streamlit (recomendado):

```bash
streamlit run app.py
```



Para explorar os notebooks (análises e experimentos):

1. Abra `notebooks/embraer.ipynb` no Jupyter ou VS Code.

## Estrutura do projeto

- `app.py` — aplicação principal (Streamlit)
- `requirements.txt` — dependências do projeto
- `data/` — arquivos CSV usados nas análises
- `notebooks/` — notebooks com análises exploratórias (`embraer.ipynb`)

## Descrição dos dados (pasta `data/`)
- `aeronave.csv` — informações sobre aeronaves envolvidas nas ocorrências (ex.: modelo, prefixo)
- `fator_contribuinte.csv` — fatores que contribuíram para cada ocorrência (classificação do fator)
- `ocorrencia_tipo.csv` — tipos de ocorrência (categoria/descrição)
- `ocorrencia.csv` — tabela principal de ocorrências (datas, local, descrição resumida, links para registros)
- `recomendacao.csv` — recomendações associadas às ocorrências (quando presentes)

> Observação: os arquivos na pasta `data/` são CSVs locais incluídos no projeto para facilitar execução e testes. Verifique as colunas ao carregar os dados — nomes e formatos podem variar entre versões da base.

## Uso rápido / Exemplo

1. Inicie a aplicação com `streamlit run app.py`.
2. No painel lateral, selecione filtros (ano, modelo de aeronave, tipo de ocorrência).
3. Interaja com gráficos e tabelas para investigar padrões e exportar insights.

## Contribuindo

Contribuições são bem-vindas. Para contribuir:

1. Fork este repositório.
2. Crie uma branch com sua feature: `git checkout -b feature/minha-melhoria`
3. Implemente e adicione testes/suporte quando aplicável.
4. Abra um Pull Request descrevendo as mudanças.

Por favor, inclua descrições claras e, se alterar dados ou pipeline, explique como validar.

## Contato

Se quiser discutir melhorias ou reportar problemas, abra uma issue ou me envie uma mensagem através do repositório.

## Licença
Este repositório não possui uma licença explícita no momento. Se desejar tornar o projeto público com uso/redistribuição permitidos, adicione um arquivo `LICENSE` ou atualize este README com a licença desejada.

---


