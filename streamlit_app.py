import streamlit
import pandas as pd
import requests

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
streamlit.dataframe(filtered_df)

streamlit.text('DataFrame stored on Dropbox')
df_dropbox = pd.read_csv("https://www.dropbox.com/s/vku7tldegl2w9em/CL2_daily.csv?dl=1", on_bad_lines='skip')
streamlit.dataframe(df_dropbox.head())

# Affichage d'un appel API
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.header("Fruityvice Fruit Advice!")
streamlit.text("Résultat d'un appel API")
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)
