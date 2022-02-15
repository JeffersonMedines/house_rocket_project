import pandas    as pd
import geopandas
import streamlit as st
import numpy     as np
import folium
import plotly.express as px

from datetime import datetime
from streamlit_folium import folium_static
from folium.plugins   import MarkerCluster

st.set_page_config( layout='wide' )

# Functions
@st.cache( allow_output_mutation=True )
def get_data( path ):
    data = pd.read_csv( path )

    return data

@st.cache( allow_output_mutation=True )
def get_geofile( url ):
    geofile = geopandas.read_file( url )

    return geofile

def set_feature( data ):
    # add new features
    data['price_m2'] = data['price'] / data['sqft_lot']

    return data

def overview_data( data ):
    f_attributes = st.sidebar.multiselect('Enter Columns', data.columns)
    f_zipcode = st.sidebar.multiselect(
        'Enter Zipcode',
        data['zipcode'].unique())

    st.title('Data Overview')

    if (f_zipcode != []) & (f_attributes != []):
        data = data.loc[data['zipcode'].isin(f_zipcode), f_attributes]

    elif (f_zipcode != []) & (f_attributes == []):
        data = data.loc[data['zipcode'].isin(f_zipcode), :]

    elif (f_zipcode == []) & (f_attributes != []):
        data = data.loc[:, f_attributes]

    else:
        data = data.copy()

    st.dataframe(data)

    c1, c2 = st.columns((1, 1))

    # Average metrics
    df1 = data[['id', 'zipcode']].groupby('zipcode').count().reset_index()
    df2 = data[['price', 'zipcode']].groupby('zipcode').mean().reset_index()
    df3 = data[['sqft_living', 'zipcode']].groupby('zipcode').mean().reset_index()
    df4 = data[['price_m2', 'zipcode']].groupby('zipcode').mean().reset_index()

    # merge
    m1 = pd.merge(df1, df2, on='zipcode', how='inner')
    m2 = pd.merge(m1, df3, on='zipcode', how='inner')
    df = pd.merge(m2, df4, on='zipcode', how='inner')

    df.columns = ['ZIPCODE', 'TOTAL HOUSES', 'PRICE', 'SQFT LIVING',
                  'PRICE/M2']

    c1.header('Average Metrics')
    c1.dataframe(df, height=630)

    # Statistics Descriptive
    num_attributes = data.select_dtypes(include=['int64', 'float64'])
    media = pd.DataFrame(num_attributes.apply(np.mean))
    mediana = pd.DataFrame(num_attributes.apply(np.median))
    std = pd.DataFrame(num_attributes.apply(np.std))

    max_ = pd.DataFrame(num_attributes.apply(np.max))
    min_ = pd.DataFrame(num_attributes.apply(np.min))

    # Merge
    df1 = pd.concat([max_, min_, media, mediana, std], axis=1).reset_index()
    df1.columns = ['attributes', 'max', 'min', 'media', 'mediana', 'std']

    c2.header('Statistics Descriptive')
    c2.dataframe(df1, height=640)

    st.write(f_attributes)
    st.write(f_zipcode)

    return None

def portfolio_density( data, geofile ):
    st.title('Region Overview')

    c1, c2 = st.columns((1, 1))
    c1.header('Portfolio Density')

    df = data.sample(10)

    # Base Map - Folium
    density_map = folium.Map(location=[data['lat'].mean(),
                                       data['long'].mean()],
                             default_zoom_start=15)

    marker_cluster = MarkerCluster().add_to(density_map)
    for name, row in df.iterrows():
        folium.Marker([row['lat'], row['long']],
                      popup='Sold R${0} on: {1}. Features: {2} sqft,'
                            ' {3} bedrooms, year built: {5}'.format(
                          row['price'],
                          row['date'],
                          row['sqft_living'],
                          row['bedrooms'],
                          row['bathrooms'],
                          row['yr_built']
                      )).add_to(marker_cluster)

    with c1:
        folium_static(density_map)

    # Region Price Map
    c2.header( 'Price Density' )

    df = data[['price', 'zipcode']].groupby( 'zipcode' ).mean().reset_index()
    df.columns = ['ZIP', 'PRICE']

    df = df.sample( 10 )

    geofile = geofile[geofile['ZIP'].isin( df['ZIP'].tolist() )]

    region_price_map = folium.Map(location=[data['lat'].mean(),
                                  data['long'].mean()],
                                  default_zoom_start=15)

    region_price_map.choropleth( data = df,
                                 geo_data = geofile,
                                 columns=['ZIP', 'PRICE'],
                                 key_on='feature.properties.ZIP',
                                 fill_color='YlOrRd',
                                 fill_opacity = 0.7,
                                 line_opacity = 0.2,
                                 legend_name='AVG PRICE' )

    with c2:
       folium_static( region_price_map )

    return None

def commercial_distribution( data ):
    st.title('Commercial Attributes')
    st.sidebar.title('Commercial Options')

    # ---------Average Price per Year

    # Filter

    min_year_built = int(data['yr_built'].min())
    max_year_built = int(data['yr_built'].max())

    st.sidebar.subheader('Select Max Year Built')
    f_year_built = st.sidebar.slider('Year Built',
                                     min_year_built,
                                     max_year_built,
                                     max_year_built)

    st.header('Average Price per Year Built')

    # Data Selection
    df = data.loc[data['yr_built'] < f_year_built]
    df = df[['yr_built', 'price']].groupby('yr_built').mean().reset_index()

    # Plot
    fig = px.line(df, x='yr_built', y='price')

    st.plotly_chart(fig, use_container_width=True)

    # ----------Average Price per Day
    st.header('Average Price per Day')
    st.sidebar.subheader('Select Max Date')

    # Filters
    min_date = datetime.strptime(data['date'].min(), '%Y-%m-%d')
    max_date = datetime.strptime(data['date'].max(), '%Y-%m-%d')

    f_date = st.sidebar.slider('Date', min_date,
                               max_date,
                               max_date)
    data['date'] = pd.to_datetime(data['date'])
    df = data.loc[data['date'] < f_date, :]
    df = df[['date', 'price']].groupby('date').mean().reset_index()

    fig = px.line(df, x='date', y='price')

    st.plotly_chart(fig, use_container_width=True)

    # -------------- Histogram
    st.header('Price Distribution')
    st.sidebar.subheader('Select Max Price')

    # Filter
    min_price = int(data['price'].min())
    max_price = int(data['price'].max())
    avg_price = int(data['price'].mean())

    # Data Filtering
    f_price = st.sidebar.slider('Price', min_price,
                                max_price,
                                avg_price)

    df = data.loc[data['price'] < f_price, :]

    # Plot
    fig = px.histogram(df, x='price', nbins=50)
    st.plotly_chart(fig, use_container_width=True)

    return None

def attributes_distribution( data ):
    st.sidebar.title('Attributes Options')
    st.title('House Attributes')

    # Filters
    f_bedrooms = st.sidebar.selectbox('Max number of bedrooms', sorted(set(data['bedrooms'].unique())))
    df = data[data['bedrooms'] < f_bedrooms]

    f_bathrooms = st.sidebar.selectbox('Max number of bathrooms', sorted(set(data['bathrooms'].unique())))
    df = data[data['bathrooms'] < f_bathrooms]

    f_floors = st.sidebar.selectbox('Max number of floors', sorted(set(data['floors'].unique())))
    df = data[data['floors'] < f_floors]

    c1, c2 = st.columns((2))
    c1.header('House per bedrooms')
    c2.header('House per bathrooms')

    # House per bedrooms
    fig = px.histogram(data, x='bedrooms', nbins=19)
    c1.plotly_chart(fig, use_container_width=True)

    # House per bathrooms
    fig = px.histogram(data, x='bathrooms', nbins=19)
    c2.plotly_chart(fig, use_container_width=True)

    c1, c2 = st.columns((1, 1))
    c1.header('House per floors')
    c2.header('House per water view')

    # House per floors
    fig = px.histogram(data, x='floors', nbins=10)
    c1.plotly_chart(fig, use_container_width=True)

    # House per water view

    f_water = st.sidebar.checkbox('View to water')
    if f_water:
        df = data[data['waterfront'] == 1]

    else:
        df = data.copy()

    fig = px.histogram(df, x='waterfront', nbins=3)
    c2.plotly_chart(fig, use_container_width=True)

    return None


if __name__ == '__main__':
    # ETL
    # Data Extraction
    path = 'kc_house_data.csv'
    url = 'https://opendata.arcgis.com/datasets/83fc2e72903343aabff6de8cb445b81c_2.geojson'

    data = get_data( path )

    geofile = get_geofile( url )

    # Data transformation
    data['date'] = pd.to_datetime( data['date'] ).dt.strftime( '%Y-%m-%d' )

    data = set_feature( data )

    overview_data( data )

    portfolio_density( data, geofile )

    commercial_distribution( data )

    attributes_distribution( data )
    # Data Load










































