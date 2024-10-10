#!/bin/python3
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

print(unique_places)

temp = pd.read_csv('../data-raw/weather_data.csv', sep=';')

# Melt the temperature dataframe so that each day becomes a row
temp_melted = temp.melt(
    id_vars=['year', 'month'], 
    var_name='day', 
    value_name='temperature')

temp_melted['day'] = temp_melted['day'].astype(int)

# Merge the two dataframes on year, month, and day
df = pd.merge(df, temp_melted, on=['year', 'month', 'day'], how='left')


# Uložení upraveného souboru
df.to_csv("data_zpracovane.csv", index=False, sep=';')
