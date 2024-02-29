import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Hide PyplotGlobalUseWarning
st.set_option('deprecation.showPyplotGlobalUse', False)

data = pd.read_csv('concrete_data.csv')

st.title('Correlation between different features of Concrete Data and its impact on Strength')

st.write('This is a simple web app to view the correlation between different features of the Concrete Data and its impact on the Strength of the concrete. The data is taken from the UCI Machine Learning Repository.')

st.write('The data consists of 9 features and 1 target variable. The features are Cement, Blast Furnace Slag, Fly Ash, Water, Superplasticizer, Coarse Aggregate, Fine Aggregate, Age and the target variable is Strength.')

st.write('The correlation between feature and target will be shown as scatter plot, you can choose which feature you want to see the correlation with the target variable.')

features = data.columns.tolist()[:-1]
target = data.columns.tolist()[-1]

selected_feature = st.selectbox('Select the feature to see the correlation with the target variable', features)

submit = st.button('Show')

if submit:
    plt.figure(figsize=(10, 6))
    plt.title(f"Correlation between {selected_feature} and {target}")
    sns.scatterplot(x=selected_feature, y=target, data=data)
    sns.regplot(x=selected_feature, y=target, data=data, scatter=False, color='r')
    plt.xlabel(selected_feature)
    plt.ylabel(target)
    st.pyplot()

