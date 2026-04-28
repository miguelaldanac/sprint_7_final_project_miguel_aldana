import pandas as pd
import plotly.express as px
import streamlit as st

# Título
st.header("Vehicle Data Dashboard")

# Cargar datos
car_data = pd.read_csv("vehicles_us.csv")

# Checkbox para histograma
build_hist = st.checkbox("Show Odometer Histogram")

if build_hist:
    st.write("Histogram of Odometer")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Checkbox para scatter
build_scatter = st.checkbox("Show Price vs Odometer")

if build_scatter:
    st.write("Scatter: Price vs Odometer")
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
