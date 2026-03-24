import sqlite3
import pandas as pd 

# ouverture de la pipeline pour établir la connexion
tuyau = sqlite3.connect('smart_city_velib.db')
# commande pandas pour lire la base comprenant deux paramètres : commande SQL + la pipeline de connexion
df_lecture = pd.read_sql('SELECT * FROM station_temps_reel', tuyau)
tuyau.close()
print(len(df_lecture))
print(df_lecture.tail())

