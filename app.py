import pandas as pd
import streamlit as st
from PIL import Image
import plotly.express as px
import csv
import plotly.graph_objects as go
from pathlib import Path

csv_path = Path(__file__).parents[0] /'gss2016.csv'


gss_data=pd.read_csv(csv_path)

# gss_data=pd.read_csv('gss2016.csv')


st.header("GSS dataset")
st.dataframe(gss_data)
st.title("Data Analytics Web App of General Social Survey")
gss_data_filtered=gss_data[['sex','race','age','degree','wrkstat','income','happy']]

st.dataframe(gss_data_filtered)

columns={'sex','race','age','degree','wrkstat','income','happy',''}

pick_columns=st.selectbox("Count by column :",list(columns))

gss_data_filtered["Count"]=0

gss_data_filtered_count=gss_data_filtered.groupby(pick_columns).count()

gss_data_filtered_count=gss_data_filtered_count[['sex']]
gss_data_filtered_count.columns=['Count']
gss_data_filtered_count["Percentages"]=(gss_data_filtered_count.Count/gss_data_filtered_count.Count.sum()) *100


st.dataframe(gss_data_filtered_count)


multi_select_column= st.multiselect("Multi-select columss or correlation", list(columns), default=["sex"])
multi_select_gss_data_filtered=gss_data_filtered[multi_select_column]
st.dataframe(multi_select_gss_data_filtered)
multi_select_column2 = st.multiselect("Multi-select colunns grouped by:",list(columns), default=["sex"])
multi_select_groupby=gss_data_filtered[multi_select_column2].groupby(multi_select_column2).size().reset_index(name='Count')
multi_select_groupby["Percentages"]=(multi_select_groupby.Count / multi_select_groupby.Count.sum()) *100
st.dataframe (multi_select_groupby)



pick_columns_visualized=st.selectbox("Visualize by Column",list(columns))
gss_data_filtered_count_visual=gss_data_filtered.groupby(pick_columns_visualized).count()
gss_data_filtered_count_visual['x-axis']=gss_data_filtered_count_visual.index
fig=go.Figure(data=[go.Pie(labels=gss_data_filtered_count_visual["x-axis"],values=gss_data_filtered_count_visual["Count"])])
st.plotly_chart(fig)
