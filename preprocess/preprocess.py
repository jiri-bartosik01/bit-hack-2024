import pandas as pd

# Načtení CSV souboru
df = pd.read_csv("../data-raw/data.csv", sep=';')

# Přejmenování sloupců podle zadaného formátu
df.columns = ['place', 'year', 'month', 'day', 'hour', 'verejnost', 'abonenti', 'total']


# Odstranění sloupců "verejnost" a "abonenti"
df = df.drop(columns=['verejnost', 'abonenti'])

df['total'] = pd.to_numeric(df['total'], errors='coerce').fillna(0).astype(int)

# Přiřazení čísel originálním názvům v prvním sloupci pomocí "enumerate"
unique_places = {name: i for i, name in enumerate(df['place'].unique())}
df['place'] = df['place'].map(unique_places)

# Uložení upraveného souboru
df.to_csv("data_zpracovane_nove_nazvy.csv", index=False, sep=';')
