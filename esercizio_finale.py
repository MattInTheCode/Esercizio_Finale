import numpy as np
import pandas as pd
import matplotlib.pyplot as plt




numero_giorni = 305
date_range = pd.date_range(start="2023-01-01", periods=numero_giorni, freq='D')

# Generazione visitatori
media = 1200
std = 900
visitatori = np.random.normal(media, std, numero_giorni)

# trend crescente nel tempo
trend = np.linspace(0, 300, numero_giorni)
visitatori = visitatori + trend  

# con np maximum qualsiasi valore al di sotto di 0 sarà 0
visitatori = np.maximum(visitatori, 0)



# Generazione di una colonna casuale per la patologia 
patologie = ["ossa", "cuore", "testa"]
patologia = np.random.choice(patologie, numero_giorni)

# Creazione  del  DataFrame con le date come indice, il numero di visitatori e la patologia
df = pd.DataFrame({
    "Visitatori": visitatori.astype(int),
    "Patologia": patologia
}, index=date_range)

print("Le prime 5 righe:")
print(df.head())

