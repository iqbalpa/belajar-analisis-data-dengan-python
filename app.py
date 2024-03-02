import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Hide PyplotGlobalUseWarning
st.set_option('deprecation.showPyplotGlobalUse', False)

data = pd.read_csv('main_data.csv')

st.title("The most popular day for group of users")

day_grouped = data.groupby('weekday')
casual_by_weekday = day_grouped['casual'].sum()
registered_by_weekday = day_grouped['registered'].sum()

selected_feature = st.selectbox('Select type of users', ['casual', 'registered'])

submit = st.button('Show')

if submit:
    plt.figure(figsize=(10, 6))
    if selected_feature == 'casual':
        plt.bar(casual_by_weekday.index, casual_by_weekday.values)
        plt.title('Casual users by weekday')
    else:
        plt.bar(registered_by_weekday.index, registered_by_weekday.values)
        plt.title('Registered users by weekday')
    st.pyplot()

