import streamlit
import pandas as pd
import requests
import snowflake.connector

streamlit.set_page_config(page_title="Bienvenue au PMU", layout="wide")
#streamlit.title('Bienvenue au PMU')

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
df_dropbox = pd.read_csv("https://www.dropbox.com/s/7tzhy9xe99740vo/Analyse_quotidienne_Daily_entries.csv?dl=1")
streamlit.dataframe(df_dropbox.tail(25), height=915)

# Affichage d'un appel API
# Textbox pour determiner le fruit. Utilisation de variable dans appel api
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('Aliment selectionné', fruit_choice)
# Appel API variabilisé
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
# Mise en forme du résultat dans la page
streamlit.header("Fruityvice Fruit Advice!")
streamlit.text("Résultat d'un appel API")
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)

# Test de connexion à Snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.header("Test de connexion Snowflake")
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
