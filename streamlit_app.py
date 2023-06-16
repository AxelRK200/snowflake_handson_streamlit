import streamlit
import pandas

streamlit.title('Bienvenue au PMU')
streamlit.text('Prenez vos paris')

streamlit.header('🐎 cote de Apollo Quick à 9 contre 1')
streamlit.text('Alimentation du cheval')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
