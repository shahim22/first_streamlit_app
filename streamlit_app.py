from urllib.error import URLError
import snowflake.connector
import requests
import streamlit
import pandas
streamlit.title("All good here..")
streamlit.title("A Healthy Breakfast is the one which you like.")
streamlit.title('And of course eat healthy.')
streamlit.header("🍌🥭 Build Your Own Fruit Smoothie 🥝🍇")
#import pandas

#create repeatable code block (called a function)
def get_fruityvice_data(this_fruit_choice):
     fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
     fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
     return fruityvice_normalized    

def get_fruit_load_list():
    my_cur = my_cnx.cursor()
    #my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
    my_cur.execute("SELECT * from fruit_load_list")
    return my_cur.fetchall() 




my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Lemon'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
streamlit.dataframe(fruits_to_show)



streamlit.header("Fruityvice Fruit Advice!")
try:
     fruit_choice = streamlit.text_input('What fruit would you like information about?')
     if not fruit_choice:
           streamlit.error("Please select a fruit to get information.")
     else:   
           back_from_function = get_fruityvice_data(fruit_choice)
           streamlit.dataframe(back_from_function)

except URLError as e:
     streamlit.error()
            
#import requests

#streamlit.text(fruityvice_response.json())

# take the json version of fresponse and normalize it

# output the data in tablular form.


#import snowflake.connector
#dont run anything from here
# streamlit.stop()

#Add a button to load the fruit
if streamlit.button('Get the fruit Load list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list() 
    streamlit.dataframe(my_data_rows)


streamlit.header("The Fruit load list contains:")


fruit_add_choice = streamlit.text_input('What fruit would you like to add?','Litchi')
streamlit.write('Thanks for adding ', fruit_add_choice)

my_cur.execute("insert into fruit_load_list values('from streamlit')")
