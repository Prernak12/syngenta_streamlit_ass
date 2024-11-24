import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("CSV Data Visualization")
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.dataframe(data)

    chart_type = st.selectbox("Select Chart Type", ["Line Chart", "Bar Chart", "Histogram"])
    column = st.selectbox("Select Column for Visualization", data.columns)

    if chart_type == "Line Chart":
        st.line_chart(data[column])
    elif chart_type == "Bar Chart":
        st.bar_chart(data[column])
    elif chart_type == "Histogram":
        fig, ax = plt.subplots()
        ax.hist(data[column].dropna(), bins=20)
        st.pyplot(fig)
