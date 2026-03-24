import sqlite3
import pandas as pd

pipeline = sqlite3.connect('smart_city_velib.db')
df_total = pd.read_sql('SELECT * FROM station_temps_reel', pipeline)
df_total.to_csv('donnees_powerbi.csv', index= False)
pipeline.close()