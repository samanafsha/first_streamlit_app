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


# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page
