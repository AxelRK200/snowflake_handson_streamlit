import streamlit
import pandas as pd

streamlit.title('Bienvenue au PMU')
streamlit.text('Prenez vos paris')

#streamlit.header('🐎 cote de Apollo Quick à 9 contre 1')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

streamlit.text('Alimentation du cheval')
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
