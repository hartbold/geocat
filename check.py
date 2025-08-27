"""
Comprovem que les dades recollides al scrap.py y desades en el csv poblacions_coords.csv tenen sentit.
"""

import pandas as pd

poblacions = pd.read_csv("./poblacions_coords.csv")

# poblacions sense coordenades
print(poblacions[poblacions['longitud'].isna() | poblacions['latitud'].isna()])
