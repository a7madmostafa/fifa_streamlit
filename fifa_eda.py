import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

fifa = pd.read_csv('fifa_eda.csv')

st.title("FIFA Exploratory Data Analysis")
st.write(""" this app performs simple EDA on fifa 2019 data 
            * **Python libraries:** pandas, streamlit, numpy, matplotlib, seaborn
       * **Data source:** [Kaggle](https://www.kaggle.com/karangadiya/fifa19)""")

st.image('players.jpg', width=500)
st.subheader("Top 5 Valued Players")
top5 =fifa.nlargest(5, 'Value')[['Name', 'Value']]
# st.write(top5)
top_players_dict = top5.set_index('Name').to_dict()

col1, col2 = st.columns(2)
with col1:
    for name, value in top_players_dict['Value'].items():
        st.markdown(f"+ {name}: {value}")

with col2:
    fig = px.bar(top5, x='Name', y='Value', title='Top 5 Valued Players')
    st.plotly_chart(fig)

#players_avg_values = fifa.groupby('Nationality').mean()['Value']
nationality = fifa.Nationality.unique().tolist()
country_choice = st.selectbox('Choose Country', nationality)
st.write(fifa[fifa.Nationality == country_choice]['Value'].mean())


num_cols = fifa.select_dtypes(include=['int64', 'float64']).columns.tolist()

col1, col2 = st.columns(2)
with col1:
    num_feat_choice = st.selectbox('Choose Numerical Feature', num_cols)
with col2:
    plot_type = st.selectbox('Choose Plot Type', ['Histogram', 'Box Plot', 'Violin Plot'])
if plot_type == 'Histogram':
    st.plotly_chart(px.histogram(fifa, x=num_feat_choice, title=num_feat_choice))
elif plot_type == 'Box Plot':
    st.plotly_chart(px.box(fifa, x=num_feat_choice, title=num_feat_choice))
else:
    st.plotly_chart(px.violin(fifa, x=num_feat_choice, title=num_feat_choice))
