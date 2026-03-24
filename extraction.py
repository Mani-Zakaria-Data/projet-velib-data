import requests
import pandas as pd
import sqlite3
import time


while True:
    # Reset 
    pagination = 0
    
    while True:
    # 1- EXTRACTION
        url_velib = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel/records"
        url_pagination = url_velib + "?limit=100&offset=" + str(pagination)
        print("Extraction des données en cours...")
        reponse = requests.get(url_pagination)
        dictionnaire_brut = reponse.json()

    # Récupération des données brutes
        donnees_stations = dictionnaire_brut['results']
        if len(donnees_stations) == 0:
            print("\n--- Traitement complet terminée. Prochain traitement dans 10 minutes ---")
            break

    # 2- TRANSFORMATION
        print("\n--- Tableau Nettoyé et GPS")
        df_velib = pd.DataFrame(donnees_stations)
        # Données imbriquées pour transformation en un tableau de 2 colonnes claires (lon, lat) 
        df_gps = df_velib['coordonnees_geo'].apply(pd.Series)
        
        # On assemble les deux tableaux
        df_velib = pd.concat([df_velib, df_gps], axis=1)

    # On filtre sur les colonnes qui nous interesse en ajoutant les données géographiques
        donnees_cles = ['stationcode', 'name', 'capacity', 'numdocksavailable', 'numbikesavailable', 'lat', 'lon']
        df_velib = df_velib[donnees_cles]
        df_velib['date_extraction'] = pd.Timestamp.now()

    # 3- VÉRIFICATION du résultat
        print("\n--- Tableau Nettoyé (Uniquement nos 5 colonnes) ---")
        print(df_velib.head())

    # 4- LOAD
        print("\nCréation de la base SQL...")
        pipeline = sqlite3.connect("smart_city_velib.db")

    # On charge le tableau dans la table 'station_temps_reel'
        df_velib.to_sql("station_temps_reel", pipeline, if_exists='append', index=False)
        pipeline.close()

        print("Données sauvegardées avec succès dans la base")
        pagination = pagination + 100
    time.sleep(30)