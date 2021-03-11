import streamlit as st

import array
import numpy as np
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


st.title('A app about yield data' )

st.sidebar.title('Selectors')

'''
##  Subtitle: Wheat in the UK

'''
st.write('Some data')

DATA_URL = ('../All_Cultivars_Spreadsheets/all_cultivars.csv')


@st.cache(persist=True)
def load_dt():
    data = pd.read_csv(DATA_URL)
    # data['Sow Month'] = pd.to_datetime(data['Sow Month'])
    data['lat'] = data['Lat']
    data['lon'] = data['Long']
    return data[data.Cultivar.str.startswith('A')]

data = load_dt()

chart_data = data['Yield']

st.write(data)

def make_cultivar_dt():
    vals = {}
    for cultivar in data.Cultivar.values:
        cultivar_df = data[data.Cultivar == cultivar]
        vals[cultivar] = cultivar_df.Yield
    return vals

st.line_chart(make_cultivar_dt())

if st.checkbox('Show Map'):
    st.map(data[['Yield', 'lat', 'lon']])
    year = st.slider('Year', 2012, 2017)

# text = [elem.encode('hex') for cult in data.Cultivar]
 # text = array.array(data.Cultivar)
text = data['Cultivar']

wordcloud = WordCloud().generate(text)

plt.imshow(wordcloud)
plt.axis('off')
plt.show()
st.pyplot()
 #.ddtype
#as stg

