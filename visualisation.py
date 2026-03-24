import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Ouverture du pipeline
pipeline = sqlite3.connect("smart_city_velib.db")
# EXTRACTION ciblée + fermutre pour sécuriser le tuyau
df_station = pd.read_sql("SELECT * FROM station_temps_reel WHERE stationcode = 31003", pipeline)
pipeline.close()

# Affichage du nombre de lignes pour checker la cohérence du graphique
print(f"Nombre de lignes trouvées : {len(df_station)}")
print(df_station)

# Rendre l'axe X plus lisible car la donnée temporelle de pandas est trop précise
df_station['heure_lisible'] = pd.to_datetime(df_station['date_extraction']).dt.strftime('%H:%M:%S')

plt.title("Evolution des Vélib' - STATION EMILE ZOLA")
plt.xlabel("Heure de la journée")
plt.ylabel("Nombre de vélo disponible")

# Commande matplotlib pour tracer le visuel sur un graphique paramètre Axe X et Axe Y + markeur car 1 seule ligne présente dans ma base
plt.plot(df_station['heure_lisible'], df_station['numbikesavailable'], marker='o')
plt.show()

