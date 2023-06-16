import streamlit
import pandas as pd

streamlit.title('Bienvenue au PMU')
streamlit.text('Prenez vos paris')

streamlit.header('🐎 cote de Apollo Quick à 9 contre 1')
streamlit.text('Alimentation du cheval')

# import du DataFrame depuis Bucket S3
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Création d'une liste à choix multiples sur la base d'une colonne
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Choisis ton fruit:", list(my_fruit_list.Fruit))

# Affichage du DataFrame sur la page
streamlit.dataframe(my_fruit_list)
