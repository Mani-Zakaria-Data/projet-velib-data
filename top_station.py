import sqlite3
import pandas as pd

pipeline = sqlite3.connect('smart_city_velib.db')
top_station = pd.read_sql('SELECT * FROM station_temps_reel ORDER BY numbikesavailable DESC LIMIT 1', pipeline)
print(top_station)
pipeline.close()