import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Data Visualization with Time-Series")
data = pd.read_csv("C:/Users/Hello/Documents/data(1).csv", encoding='unicode_escape')
data['sales'] = data['UnitPrice'] * data['Quantity']

# checking how many quantity of products have been sold online from each country
plt.rcParams['figure.figsize'] = (12, 10)
a = data['sales'].groupby(data['Country']).agg('sum').sort_values(ascending=False)[1:]
sns.barplot(x=a.values, y=a.index, palette='inferno')
st.title('Sales of all the Countries Except UK')
st.pyplot()

# looking the stockcode for the dataset

color = plt.cm.copper(np.linspace(0, 1, 20))
data['StockCode'].value_counts().head(20).plot.bar(color=color, figsize=(18, 10))
plt.xlabel('StockCode')
st.title('Most Popular Stock codes')
st.pyplot()

color = plt.cm.viridis(np.linspace(0, 1, 20))
x_plt = plt.xlabel('Names of the Countries')
y_plt = plt.ylabel('Number of Items Sold')
data['Quantity'].groupby(data['Country']).agg('sum').sort_values(ascending=True).head(20).plot.bar(figsize=(15, 7),
                                                                                                   color=color,
                                                                                                   x=x_plt,
                                                                                                   y=y_plt)
st.title('20 Countries according to Quantity Sold Online')
st.pyplot()


# checking the different values for country in the dataset

plt.rcParams['figure.figsize'] = (12, 10)
a = data['Country'].value_counts().tail(20)
sns.barplot(x=a.values, y=a.index, palette='inferno')
st.title('Bottom 20 Countries having Online Retail Market')
plt.xlabel('Names of Countries')
plt.ylabel('Count')
st.pyplot()

# looking at the bottom 20 countries sales wise

data['sales'].groupby(data['Country']).agg('sum').sort_values(ascending=True).head(20).plot.bar(figsize=(15, 7),
                                                                                                color='pink')
st.title('Bottom 20 Countries Sales wise')
plt.xlabel('Names of Countries')
plt.ylabel('Sales')
st.pyplot()

# let's look at Sales vs Invoicedate (Time series Analysis)

plt.rcParams['figure.figsize'] = (15, 5)
data.plot(x='InvoiceDate', y='sales')
st.title("Time Series Analysis of Sales")
plt.xticks(rotation=90)
plt.xlabel('Date of Purchase')
plt.ylabel('Sales')
st.pyplot()

# time-series plot for netherlands
plt.rcParams['figure.figsize'] = (15, 5)
dataset = data[data['Country'] == 'Netherlands']
dataset.plot(x='InvoiceDate', y='sales')
st.title('Time-Series for Netherlands')
plt.xticks(rotation=90)
plt.xlabel('Date of Purchase')
plt.ylabel('Sales Amount')
st.pyplot()

# time-series plot for Australia
plt.rcParams['figure.figsize'] = (15, 5)
dataset = data[data['Country'] == 'Australia']
dataset.plot(x='InvoiceDate', y='sales')
st.title('Time-Series for Australia')
plt.xticks(rotation=90)
plt.xlabel('Date of Purchase')
plt.ylabel('Sales Amount')
st.pyplot()

# time-series plot for France
plt.rcParams['figure.figsize'] = (15, 5)
dataset = data[data['Country'] == 'France']
dataset.plot(x='InvoiceDate', y='sales')
st.title('Time-Series for France')
plt.xticks(rotation=90)
plt.xlabel('Date of Purchase')
plt.ylabel('Sales Amount')
st.pyplot()

# time-series plot for Germany
plt.rcParams['figure.figsize'] = (15, 5)
dataset = data[data['Country'] == 'Germany']
dataset.plot(x='InvoiceDate', y='sales')
st.title('Time-Series for Germany')
plt.xticks(rotation=90)
plt.xlabel('Date of Purchase')
plt.ylabel('Sales Amount')
st.pyplot()

# time-series plot for Switzerland
plt.rcParams['figure.figsize'] = (15, 5)
dataset = data[data['Country'] == 'Switzerland']
dataset.plot(x='InvoiceDate', y='sales')
st.title('Time-Series for Switzerland')
plt.xticks(rotation=90)
plt.xlabel('Date of Purchase')
plt.ylabel('Sales Amount')
st.pyplot()
