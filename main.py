import streamlit as st
import datetime as dt
import pandas_datareader.data as web
import matplotlib.pyplot as plt

# Warningの非表示
st.set_option('deprecation.showPyplotGlobalUse', False)

def get_data(start, end, id):
    df = web.DataReader(id, 'fred', start, end)
    return df

def plot_graph(start):
    end = dt.date.today()
    jpn = get_data(start, end, 'IRLTLT01JPM156N')
    usa = get_data(start, end, 'DGS10')
    
    ax_jpn = plt.subplot(211)
    ax_jpn.set_xlim(start,end)
    ax_jpn.plot(jpn.index, jpn, label='JPN')
    ax_jpn.legend()

    ax_usa = plt.subplot(212)
    ax_usa.set_xlim(start,end)
    ax_usa.plot(usa.index, usa, label='USA')
    ax_usa.legend()
    
    st.pyplot()

if st.button('plot'):
    start = dt.date(2012,1,1)
    plot_graph(start)

    
