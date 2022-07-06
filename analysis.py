import streamlit as st
import plotly_express as px
import pandas as pd

# import matplotlib.pyplot as plt

st.set_option('deprecation.showfileUploaderEncoding', False)
st.set_option('deprecation.showPyplotGlobalUse', False)

# title of the app
st.title("RETAIL MANAGEMENT SYSTEM")
st.subheader("Exploratory Data Analysis App")

# Add a sidebar
st.sidebar.subheader("Visualization Settings")

# Setup file upload
uploaded_file = st.sidebar.file_uploader(label="Upload your CSV file. (200MB max)", type=['csv'])

if uploaded_file is not None:
    @st.cache(allow_output_mutation=True)
    def load_csv():
        csv = pd.read_csv(uploaded_file, encoding='unicode_escape')
        return csv


    #    print(uploaded_file)
    #    print("hello")
    data = load_csv()
    data['sales'] = data['UnitPrice'] * data['Quantity']
    st.write(data)

    ch = data.columns
    column_select = st.sidebar.selectbox(
        label="Sort By Columns",
        options=ch)

    st.title('** Dataset Variables **')
    st.table(data.columns)

    st.title('** Data Cleaning **')

    # Stripping extra spaces in the description
    data['Description'] = data['Description'].str.strip()

    # Dropping the rows without any invoice number
    data.dropna(axis=0, subset=['InvoiceNo'], inplace=True)
    data['InvoiceNo'] = data['InvoiceNo'].astype('str')

    # Dropping all transactions which were done on credit
    data = data[~data['InvoiceNo'].str.contains('C')]

    st.title('** Glimpse of dataset **')
    st.table(data.head(5))

    st.title('** Dataset Details **')
    st.write(data.shape)

    st.title('** checking the different values for country in the dataset **')
    st.table(data['Country'].value_counts())

    st.title('** Variables Description **')
    st.table(data.describe())

    st.title('** Variables with Null Values **')
    st.table(data.isnull().sum())

    st.title("** Unique Values in the variables **")
    st.table(data.nunique())

    st.title('** Sort by columns **')
    st.write(data.sort_values(by=column_select))

    st.title("Data Visualization App")

    # add a select widget to the side bar
    chart_select = st.sidebar.selectbox(
        label="Select the chart type",
        options=["None", "Scatterplots", "Lineplots", "Histogram", "Boxplot", "area", "bar", "funnel", "pie",
                 "strip", "density_heatmap"])

    if chart_select == 'Scatterplots':
        st.sidebar.subheader("Scatterplot Settings")
        x_values = st.sidebar.selectbox('X axis', options=data.columns)
        y_values = st.sidebar.selectbox('Y axis', options=data.columns)
        color_value = st.sidebar.selectbox("Color", options=data.columns)
        plot = px.scatter(data_frame=data.head(200), x=x_values, y=y_values, color=color_value)
        st.plotly_chart(plot)

    elif chart_select == 'Lineplots':
        st.sidebar.subheader("Line Plot Settings")
        x_values = st.sidebar.selectbox('X axis', options=data.columns)
        y_values = st.sidebar.selectbox('Y axis', options=data.columns)
        color_value = st.sidebar.selectbox("Color", options=data.columns)
        plot = px.line(data_frame=data.head(200), x=x_values, y=y_values, color=color_value)
        st.plotly_chart(plot)

    elif chart_select == 'Histogram':
        st.sidebar.subheader("Histogram Settings")
        x = st.sidebar.selectbox('Feature', options=data.columns)
        bin_size = st.sidebar.slider("Number of Bins", min_value=10, max_value=100, value=40)
        color_value = st.sidebar.selectbox("Color", options=data.columns)
        plot = px.histogram(x=x, data_frame=data.head(200), color=color_value)
        st.plotly_chart(plot)

    elif chart_select == 'Boxplot':
        st.sidebar.subheader("Boxplot Settings")
        y = st.sidebar.selectbox("Y axis", options=data.columns)
        x = st.sidebar.selectbox("X axis", options=data.columns)
        color_value = st.sidebar.selectbox("Color", options=data.columns)
        plot = px.box(data_frame=data.head(200), y=y, x=x, color=color_value)
        st.plotly_chart(plot)

    elif chart_select == "area":
        st.subheader("Area Settings")
        y = st.sidebar.selectbox("Y axis", options=data.columns)
        x = st.sidebar.selectbox("X axis", options=data.columns)
        color_value = st.sidebar.selectbox("Color", options=data.columns)
        plot = px.area(data_frame=data.head(200), y=y, x=x, color=color_value)
        st.plotly_chart(plot)

    elif chart_select == "bar":
        st.subheader("Bar Chart Setting")
        y = st.sidebar.selectbox("Y axis", options=data.columns)
        x = st.sidebar.selectbox("X axis", options=data.columns)
        color_value = st.sidebar.selectbox("Color", options=data.columns)
        plot = px.bar(data_frame=data.head(200), y=y, x=x, color=color_value)
        st.plotly_chart(plot)

    elif chart_select == "funnel":
        st.subheader("Funnel Settings")
        y = st.sidebar.selectbox("Y axis", options=data.columns)
        x = st.sidebar.selectbox("X axis", options=data.columns)
        color_value = st.sidebar.selectbox("Color", options=data.columns)
        plot = px.funnel(data_frame=data.head(200), y=y, x=x, color=color_value)
        st.plotly_chart(plot)

    elif chart_select == "pie":
        st.subheader("Pie Chart Settings")
        y = st.sidebar.selectbox("values", options=data.columns)
        color_value = st.sidebar.selectbox("Color", options=data.columns)
        plot = px.pie(data_frame=data.head(200), values=y, names=color_value)
        st.plotly_chart(plot)

    elif chart_select == "strip":
        st.subheader("Strip Settings")
        y = st.sidebar.selectbox("Y axis", options=data.columns)
        x = st.sidebar.selectbox("X axis", options=data.columns)
        color_value = st.sidebar.selectbox("Color", options=data.columns)
        plot = px.strip(data_frame=data.head(200), y=y, x=x, color=color_value)
        st.plotly_chart(plot)


    elif chart_select == "density_heatmap":
        st.subheader("Density_Heatmap Settings")
        y = st.sidebar.selectbox("Y axis", options=data.columns)
        x = st.sidebar.selectbox("X axis", options=data.columns)
        color_value = st.sidebar.selectbox("Color", options=data.columns)
        plot = px.density_heatmap(data_frame=data.head(200), y=y, x=x, marginal_x="histogram", marginal_y="histogram")
        st.plotly_chart(plot)

    else:
        st.info('**PLEASE SELECT THE VISUALIZATION or UPLOAD A DATASET**')
else:
    st.info("**PLEASE UPLOAD A DATASET**")
