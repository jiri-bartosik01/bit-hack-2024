import pandas as pd

# Načtení CSV souboru
df = pd.read_csv("../data-raw/data.csv", sep=';')

# Přejmenování sloupců podle zadaného formátu
df.columns = ['place', 'year', 'month', 'day', 'hour', 'verejnost', 'abonenti', 'total']


# Odstranění sloupců "verejnost" a "abonenti"
df = df.drop(columns=['verejnost', 'abonenti'])

df['total'] = pd.to_numeric(df['total'], errors='coerce').fillna(0).astype(int)



# Uložení upraveného souboru
df.to_csv("data_zpracovane.csv", index=False, sep=';')
