import streamlit as st
import pandas as pd
import plotly.express as px
st.header('University Data')
data=pd.read_csv('/workspaces/streamlit_dashboard/mentornow/timesData.csv')
with st.expander('Show Data'):
    st.write(data)
with st.sidebar:
    option =st.multiselect('options',['research','citations','income'])
# st.write("You selected:", option)
fig=px.line(data.head(100),x='world_rank',y=option)  
st.plotly_chart(fig)

    