import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

map_day = {
    0: 'Sunday',
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday'
}

# Hide PyplotGlobalUseWarning
st.set_option('deprecation.showPyplotGlobalUse', False)

# read data
data = pd.read_csv('main_data.csv')

# dashboard title
st.title("The most popular day for group of users")

# group the data
day_grouped = data.groupby('weekday')
casual_by_weekday = day_grouped['casual'].sum()
registered_by_weekday = day_grouped['registered'].sum()

# max day for casual users
max_casual = casual_by_weekday.idxmax()

# max day for registered users
max_registered = registered_by_weekday.idxmax()

# select the type of users
selected_feature = st.selectbox('Select type of users', ['casual', 'registered'])

plt.figure(figsize=(10, 6))
if selected_feature == 'casual':
    plt.title('Casual users by weekday')
    plt.bar(casual_by_weekday.index, casual_by_weekday.values)
    st.write("The most popular day for casual users is", map_day[max_casual])
    
else:
    plt.bar(registered_by_weekday.index, registered_by_weekday.values)
    plt.title('Registered users by weekday')
    st.write("The most popular day for registered users is", map_day[max_registered])
st.pyplot()
