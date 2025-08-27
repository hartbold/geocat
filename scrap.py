import pandas as pd
import requests
import numpy as np

def get_coords(poblacio):
    """
    Aquesta funció rep un nom de població i retorna les coordenades de la població.
    Si no troba la població, simplifica el nom de la població i torna a cercar.
    Si no troba la població simplificada, retorna un array de dos elements buits.
    """
    
    url = f"https://eines.icgc.cat/geocodificador/autocompletar?text={poblacio}&size=1&layers=tops"
    response = requests.get(url)
    data = response.json()
    
    if data["features"] and data["features"][0]["geometry"]["coordinates"]:
        coord = data["features"][0]["geometry"]["coordinates"]
        
    else:
        print(f"No s'ha trobat la població: {poblacio}")
        
        # fem una nova cerca amb el nom de la població simplificat a veure si troba alguna cosa.
        # li treiem  els dos darrers valors separats per un espai del nom de la poblacio:
        poblacio_simplificada = " ".join(poblacio.split(" ")[:-2])
        if len(poblacio_simplificada) > 3:
            coord = get_coords(poblacio_simplificada)
        else:
            coord = ['', '']
        
    return coord

poblacions = pd.read_csv("./t15903.csv", sep=";", encoding="utf-8")
# poblacions = poblacions.sample(10)

coords = []
for poblacio in poblacions["Municipi"]:
    coords.append(get_coords(poblacio))

poblacions["longitud"] = [coord[0] for coord in coords]
poblacions["latitud"] = [coord[1] for coord in coords]

print(poblacions.head())

# ho desem de nou
poblacions.to_csv("./poblacions_coords.csv", index=False)