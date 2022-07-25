import streamlit
import pandas
streamlit.title('All good here..')
streamlit.title('A Healthy Breakfast is the one which you like.')
streamlit.title('And of course eat healthy.')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
