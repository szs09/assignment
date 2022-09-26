# Importing 
import streamlit as st
import pandas as pd 
import plotly.express as px 
# Adding a Title 
st.title('Freelancers in the Middle East')
# Adding a Markdown
st.markdown('By: Stephany Said - 202371921')
# A dataset of freelancers in the Middle East 
df= pd.read_csv(r'Freelancers.csv')
df
# Line graph of the Price per Hour as a function of Country 
st.header("Location of the Freelancers and the Price they Charge per Hour")
line= px.line(df,x="location", y="price_per_hour", color="location", title="This graph represents the price freelancers charge and their locations")
line
# Scatterplot showing Location as a function of User Score
st.header("Location of the Freelancers and their Scores")
scatter= px.scatter(df, x="user_score", y="location", color="location",
           hover_name="location", log_x=True, size_max=60, title= "This graph represents the variation of the freelancers' locations as a function of their scores").update_xaxes(categoryorder="total descending")
scatter
# Strip Chart that shows verified users per their location
st.header("Verified Freelancers as per Location")
strip= px.strip(df, x="location", hover_name="verified_user", color="verified_user", title="This graph represents the verified freelancers as per Location")
strip
# Bar Chart of the User Score as a function of Price per Hour
st.header("Freelancers' Scores and the Price they Charge per Hour")
bar= px.bar(df, x="price_per_hour", y="user_score", color="user_score", title="This graph represents the relationship between the user score as a function of price per hour",labels={
                     "x": "User Score",
                     "y": "Price per Hour",
                 }).update_xaxes(categoryorder="total descending")
bar
# Pie Chart that represents the Recommended and Verified Users Percentage
st.header("Percentage of Recommended and Verified Users in the Dataset")
pie= px.pie(df, values="recommended", names="verified_user", title= "This graph represents the percentage of recommended and verified users in the dataset")
pie 
# Price per Hour Based on User Score & Country     
st.header("The Price Freelancers Charge per Hour, their Scores and Countries")
clist = df['location'].unique()
country = st.sidebar.selectbox("Select a country:",clist)
st.header("Price per hour based on score")
fig = px.line(df, x = "user_score", y = "price_per_hour" )

st.plotly_chart(fig)
                 
# Slider on how informative the dataset was
st.header("Level of Information Gained from this Dataset")
st.select_slider('How informative was this dataset?', ['Very Informative', 'Informative', 'A Little', 'Not Informative'])
