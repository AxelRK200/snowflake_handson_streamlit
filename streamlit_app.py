import streamlit
import pandas as pd

streamlit.title('Bienvenue au PMU')
streamlit.text('Prenez vos paris')

streamlit.header('🐎 cote de Apollo Quick à 9 contre 1')
streamlit.text('Alimentation du cheval')

# import du DataFrame depuis Bucket S3
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Création d'une liste à choix multiples sur la base d'une colonne
liste_a_afficher = streamlit.multiselect("Choisis ton fruit:", list(my_fruit_list.Fruit), ['Avocado','Strawberries'])
filtered_df = my_fruit_list[my_fruit_list['Fruit'].isin(liste_a_afficher)]

# Affichage du DataFrame sur la page
streamlit.dataframe(my_fruit_list)
