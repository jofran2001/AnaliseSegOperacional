"""
Dashboard interativo para análise de ocorrências aeronáuticas no Brasil.

Este módulo carrega dados do CENIPA, os processa e exibe visualizações
interativas usando Streamlit e Plotly, como parte de um projeto de iniciativa
para a dinâmica de grupo da Embraer.
"""
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide", page_title="Análise de Ocorrências Aeronáuticas")

st.title('Análise de Ocorrências Aeronáuticas no Brasil')
st.markdown(
    """
    Esta aplicação web apresenta uma análise interativa dos dados de ocorrências
    aeronáuticas reportadas pelo CENIPA. A ideia surgiu como iniciativa para a
    dinâmica de grupo da Embraer, demonstrando a aplicação prática de análise de dados.
    """
)

@st.cache_data
def carregar_dados():
    """
    Carrega, limpa e une os datasets de ocorrências e aeronaves do CENIPA.

    Returns:
        pandas.DataFrame: Um DataFrame completo com os dados prontos para análise.
    """
    valores_nulos = ['***', 'NULL', '****', '*****']
    df_ocorrencias = pd.read_csv(
        'data/ocorrencia.csv', sep=';', encoding='latin-1', na_values=valores_nulos
    )
    df_aeronaves = pd.read_csv(
        'data/aeronave.csv', sep=';', encoding='latin-1', na_values=valores_nulos
    )

    df_ocorrencias['ocorrencia_dia'] = pd.to_datetime(
        df_ocorrencias['ocorrencia_dia'], format='%d/%m/%Y', errors='coerce'
    )
    df_ocorrencias.dropna(subset=['ocorrencia_dia'], inplace=True)
    df_ocorrencias['ano'] = df_ocorrencias['ocorrencia_dia'].dt.year

    df_processado = pd.merge(
        df_ocorrencias, df_aeronaves,
        left_on='codigo_ocorrencia', right_on='codigo_ocorrencia2', how='left'
    )

    df_processado['aeronave_fabricante_limpo'] = (
        df_processado['aeronave_fabricante'].str.upper().str.strip()
    )
    df_processado['aeronave_fabricante_limpo'].replace('EMBRAER S A', 'EMBRAER', inplace=True)
    df_processado['aeronave_fabricante_limpo'].replace('CESSNA AIRCRAFT', 'CESSNA', inplace=True)
    df_processado['aeronave_fabricante_limpo'].replace('PIPER AIRCRAFT', 'PIPER', inplace=True)

    return df_processado

df_analise = carregar_dados()

st.sidebar.header("Filtros Interativos")
lista_anos = sorted(df_analise['ano'].unique(), reverse=True)
ano_selecionado = st.sidebar.selectbox('Selecione um Ano:', options=lista_anos)
df_filtrado = df_analise[df_analise['ano'] == ano_selecionado]

st.header(f"Dashboard para o ano de {ano_selecionado}")

st.sidebar.header("Opções de Gráfico")
tipo_grafico = st.sidebar.radio(
    "Selecione o tipo de visualização:",
    ('Barras', 'Pizza', 'Treemap')
)

col1, col2 = st.columns(2)

with col1:
    st.subheader('Classificação das Ocorrências')
    ocorrencias_classificacao = df_filtrado['ocorrencia_classificacao'].value_counts()
    
    if tipo_grafico == 'Barras':
        fig = px.bar(
            ocorrencias_classificacao, x=ocorrencias_classificacao.values,
            y=ocorrencias_classificacao.index, orientation='h',
            labels={'x': 'Contagem', 'y': 'Classificação'}, template='plotly_dark'
        )
    elif tipo_grafico == 'Pizza':
        fig = px.pie(
            ocorrencias_classificacao, names=ocorrencias_classificacao.index,
            values=ocorrencias_classificacao.values,
            template='plotly_dark'
        )
    elif tipo_grafico == 'Treemap':
        fig = px.treemap(
            ocorrencias_classificacao, path=[ocorrencias_classificacao.index],
            values=ocorrencias_classificacao.values,
            template='plotly_dark'
        )
    st.plotly_chart(fig, use_container_width=True)


with col2:
    st.subheader('Top 10 Estados (UF) com mais ocorrências')
    ocorrencias_uf = df_filtrado['ocorrencia_uf'].value_counts().nlargest(10)

    if tipo_grafico == 'Barras':
        fig = px.bar(
            ocorrencias_uf, x=ocorrencias_uf.values, y=ocorrencias_uf.index,
            orientation='h', labels={'x': 'Contagem', 'y': 'Estado'},
            template='plotly_dark'
        )
    elif tipo_grafico == 'Pizza':
        fig = px.pie(
            ocorrencias_uf, names=ocorrencias_uf.index, values=ocorrencias_uf.values,
            template='plotly_dark'
        )
    elif tipo_grafico == 'Treemap':
        fig = px.treemap(
            ocorrencias_uf, path=[ocorrencias_uf.index], values=ocorrencias_uf.values,
            template='plotly_dark'
        )
    st.plotly_chart(fig, use_container_width=True)

st.subheader('Top 20 Fabricantes por Número de Ocorrências')
top_fabricantes_filtrado = df_filtrado['aeronave_fabricante_limpo'].value_counts().nlargest(20)

if tipo_grafico == 'Barras':
    fig_fabricantes = px.bar(
        top_fabricantes_filtrado, x=top_fabricantes_filtrado.values,
        y=top_fabricantes_filtrado.index, orientation='h',
        title=f'Top 20 Fabricantes em {ano_selecionado}',
        labels={'x': 'Número de Ocorrências', 'y': 'Fabricante'},
        template='plotly_dark'
    )
elif tipo_grafico == 'Pizza':
    fig_fabricantes = px.pie(
        top_fabricantes_filtrado, names=top_fabricantes_filtrado.index,
        values=top_fabricantes_filtrado.values,
        title=f'Top 20 Fabricantes em {ano_selecionado}',
        template='plotly_dark'
    )
elif tipo_grafico == 'Treemap':
    fig_fabricantes = px.treemap(
        top_fabricantes_filtrado, path=[top_fabricantes_filtrado.index],
        values=top_fabricantes_filtrado.values,
        title=f'Top 20 Fabricantes em {ano_selecionado}',
        template='plotly_dark'
    )
st.plotly_chart(fig_fabricantes, use_container_width=True)

if st.checkbox('Mostrar dados brutos do ano selecionado'):
    st.subheader('Dados Brutos')
    st.write(df_filtrado)
