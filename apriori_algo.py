import pandas as pd
import streamlit as st
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from pathlib import Path

st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Apriori Algorithm")
data = pd.read_csv("C:/Users/Hello/Documents/data(1).csv", encoding='unicode_escape')
data['sales'] = data['UnitPrice'] * data['Quantity']

# Splitting the data according to the region of transaction

# Transactions done in France
basket_France = (data[data['Country'] == "France"]
                 .groupby(['InvoiceNo', 'Description'])['Quantity']
                 .sum().unstack().reset_index().fillna(0)
                 .set_index('InvoiceNo'))

st.write(basket_France)


def hot_encode(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1


# Encoding the datasets
basket_encoded = basket_France.applymap(hot_encode)
basket_encoded.drop('POSTAGE', inplace=True, axis=1)
basket_France = basket_encoded

# Building the model

st.header("**Building the models and analyzing the results**")
st.subheader("France")
frq_items = apriori(basket_France, min_support=0.05, use_colnames=True)

# Collecting the inferred rules in a dataframe
rules = association_rules(frq_items, metric="lift", min_threshold=1)
rules = rules.sort_values(['confidence', 'lift'], ascending=[False, False])
st.write(rules)

rules[(rules['lift'] >= 6) & (rules['confidence'] >= 0.8)]



st.title("Association Rule Mining")
st.header("**Using Apriori Rule**")
st.write("")
st.subheader("It uses Four Parameters")


def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()


intro_markdown = read_markdown_file("rule.md")
st.markdown(intro_markdown, unsafe_allow_html=True)


