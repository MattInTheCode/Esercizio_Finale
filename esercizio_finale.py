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

print("Prime 5 righe:")
print(df.head())




# Media e deviazione standard dei visitatori per mese
df_mensile = df.resample('M').agg({'Visitatori': ['mean', 'std']})
df_mensile[('Visitatori', 'mean')] = df_mensile[('Visitatori', 'mean')].astype(int)
#qui ho cercato come evitare il nan e  utilizzo il fillna
df_mensile[('Visitatori', 'std')] = df_mensile[('Visitatori', 'std')].fillna(0)

print("\nStatistiche mensili dei visitatori:")
print(df_mensile)


# Determino la patologia più e meno frequente
patologia_counts = df["Patologia"].value_counts()
patologia_piu_frequente = patologia_counts.idxmax()
patologia_meno_frequente = patologia_counts.idxmin()

print("\nPatologia più frequente:", patologia_piu_frequente)
print("Patologia meno frequente:", patologia_meno_frequente)