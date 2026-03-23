import sqlite3
import pandas as pd 

tuyau = sqlite3.connect('smart_city_velib.db')
df_lecture = pd.read_sql('SELECT * FROM station_temps_reel', tuyau)
tuyau.close()
print(len(df_lecture))
print(df_lecture.tail())

