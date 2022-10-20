import streamlit

streamlit.title('My new healthy diner')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

streamlit.header('Breakfast Menu')
streamlit.text('Omeg 3 and blueberry oatmeal')
streamlit.text('Kale, Spinach and Rocket Smoothie')
streamlit.text('Hard-Bolied Free-Range Egg')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
