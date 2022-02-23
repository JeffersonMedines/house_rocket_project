import pandas    as pd
import streamlit as st
import numpy     as np
import plotly.express as px
st.set_page_config( layout='wide' )
pd.options.display.max_columns = None

@st.cache( allow_output_mutation=True )
def get_data( path ):
    data = pd.read_csv( path )

    return data

def transform_data( data ):
    pd.options.display.float_format = '{:.2f}'.format
    data['date'] = pd.to_datetime(data['date']).dt.strftime('%Y-%m-%d')
    data['yr_built'] = np.int64(data['yr_built'])
    data['year'] = pd.to_datetime(data['date']).dt.strftime('%Y')
    data['month'] = pd.to_datetime(data['date']).dt.strftime('%Y-%m')

    return data

def dataset_data( data ):
    st.title('Breve Visualização do Dataset')
    st.write(data.head())

    return None

def graph_hypotheses( data ):
    # =====================================
    # Gráficos das Hipóteses
    # =====================================

    st.title('Gráficos das Hipóteses de Negócio')
    c1, c2 = st.columns((1, 1))

    graph_1 = data[['price', 'waterfront']].groupby('waterfront').mean().reset_index()
    fig = px.bar(graph_1, x='waterfront', y='price')
    fig.update_layout(title_text='Preço Médio - Imóveis com Vista para a Água', title_x=0.5)
    c1.plotly_chart(fig)

    data['old'] = data['yr_built'].apply(lambda x: 'Yes' if x < 1955 else
    'No')

    graph_2 = data[['price', 'old']].groupby('old').mean().reset_index()
    fig = px.bar(graph_2, x='old', y='price')
    fig.update_layout(title_text='Preço Médio - Imóveis Antigos', title_x=0.5)
    c2.plotly_chart(fig)

    c1, c2 = st.columns((1, 1))
    data['basement'] = data['sqft_basement'].apply(lambda x: 'No' if x == 0 else
    'Yes')
    graph_3 = data[['basement', 'price']].groupby('basement').mean().reset_index()
    fig = px.bar(graph_3, x='basement', y='price')
    fig.update_layout(title_text='Preço Médio - Imóveis com Porão', title_x=0.5)
    c1.plotly_chart(fig)

    graph_4 = data[['price', 'year']].groupby('year').mean().reset_index()
    fig = px.bar(graph_4, x='year', y='price')
    fig.update_layout(title_text='Preço Médio - Crescimento YoY', title_x=0.5)
    c2.plotly_chart(fig)

    c1, c2 = st.columns((1, 1))
    data['reformed'] = data['yr_renovated'].apply(lambda x: 'No' if x == 0 else
    'Yes')
    graph_6 = data[['reformed', 'price']].groupby('reformed').mean().reset_index()
    fig = px.bar(graph_6, x='reformed', y='price')
    fig.update_layout(title_text='Preço Médio - Imóveis Reformados', title_x=0.5)
    c1.plotly_chart(fig)

    data['one_floor'] = data['floors'].apply(lambda x: 'Yes' if x == 1 else
    'No')
    graph_7 = data[['one_floor', 'price']].groupby('one_floor').mean().reset_index()
    fig = px.bar(graph_7, x='one_floor', y='price')
    fig.update_layout(title_text='Preço Médio - Imóveis com Apenas 1 Piso', title_x=0.5)
    c2.plotly_chart(fig)

    c1, c2 = st.columns((1, 1))
    graph_5 = data[data['bathrooms'] == 3][['price', 'month']].groupby('month').mean().reset_index()
    fig = px.line(graph_5, x='month', y='price')
    fig.update_layout(title_text='Preço Médio - Crescimento MoM de Imóveis com 3 Banheiros', title_x=0.5)
    c1.plotly_chart(fig)

    data['living_mean'] = data['sqft_living'].apply(lambda x: 'above' if x > data['sqft_living'].mean() else
    'Below')
    graph_8 = data[['living_mean', 'price']].groupby('living_mean').mean().reset_index()
    fig = px.bar(graph_8, x='living_mean', y='price')
    fig.update_layout(title_text='Preço Médio - Tamanho da Sala de Estar Acima da Média', title_x=0.5)
    c2.plotly_chart(fig)

    return None

def recommendation_table( data ):
    # =====================================
    # Tabela de Recomendação de Compra
    # =====================================
    # Criando as colunas que as tabelas irão ocupar
    st.title('Tabelas de Recomendação de Compra e Venda de Imóveis')
    c1, c2 = st.columns((1, 1))

    # Criando as colunas de preço mediano e imóvel em boas condições
    data['price_median'] = data['price'].apply(lambda x: 1 if x < data['price'].median() else
    0)
    data['good_condition'] = data['condition'].apply(lambda x: 1 if x > 2 else
    0)

    # Apply lambda para criar a coluna de recomendação de compra
    data['purchase'] = data[['price_median', 'good_condition']] \
        .apply(lambda x: 'Yes' if (x['price_median'] == 1) & (x['good_condition'] == 1) else
    'No', axis=1)

    # Selecionando as colunas da tabela
    df1 = data[['id', 'price', 'date', 'purchase']]
    df1['date'] = pd.to_datetime(df1['date']).dt.strftime('%Y-%m-%d')
    c1.dataframe(df1)

    # =====================================
    # Tabela de Recomendação de Venda
    # =====================================
    # FOR para criar a coluna com o preço de venda
    for i in range(len(data)):
        if data.loc[i, 'price'] > data.loc[data['zipcode'] == data.loc[i, 'zipcode'], 'price'].mean():
            data.loc[i, 'sale'] = data.loc[i, 'price'] * 1.1

        else:
            data.loc[i, 'sale'] = data.loc[i, 'price'] * 1.3

    # Selecionando as colunas filtrando pelas linhas onde
    # o imóvel foi comprado para criar a tabela
    df2 = data[data['purchase'] == 'Yes'][['id', 'price', 'date', 'sale']]
    df2['date'] = pd.to_datetime(df2['date']).dt.strftime('%Y-%m-%d')
    c2.dataframe(df2)

    return None

if __name__ == '__main__':
    # ETL
    # Data Extraction
    path = 'kc_house_data.csv'
    data = get_data( path )

    # Data Transformation
    transform_data( data )

    dataset_data( data )

    graph_hypotheses( data )

    recommendation_table( data )
    # Data Load







