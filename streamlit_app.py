import streamlit
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

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

# usage d'une fonction
def get_fruityvice_data(fruit):
  '''retourne en dataframe le json obtenu en réponse de l'appel api'''
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
  return pd.json_normalize(fruityvice_response.json())

# Affichage d'un appel API
# Textbox pour determiner le fruit. Utilisation de variable dans appel api
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Veuillez selectionner un fruit pour avoir les infos")
  else :
    streamlit.write('Aliment selectionné', fruit_choice)
    # Appel API variabilisé, via fonction
    streamlit.text("Résultat de l'appel API")
    streamlit.dataframe(get_fruityvice_data(fruit_choice))
except URLError as e :
  streamlit.error()
streamlit.stop()

# Test de connexion à Snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

my_cur.execute("SELECT * FROM fruit_load_list")
fruits = my_cur.fetchall()
streamlit.header("Appel de la table fruit_load_list")
streamlit.dataframe(fruits)

# Ajout d'une 2e Textbox 
fruit_choice2 = streamlit.text_input('What fruit would you like to add ?','Banana')
streamlit.write('Merci d avoir ajouté : ', fruit_choice2)
