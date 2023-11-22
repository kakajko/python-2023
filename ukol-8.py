import pandas as pd
file_path = '/Users/karolinagerych/Desktop/adopce-zvirat.csv'
df = pd.read_csv(file_path, sep=';')
print(df.shape)
#řádků 513 a sloupců 6

columns = df.columns
print(columns)
#názvy sloupců: 'id', 'nazev_cz', 'nazev_en', 'trida_cz', 'cena', 'k_prohlidce'

index_34_cz = df.loc[34, 'nazev_cz']
index_34_en = df.loc[34, 'nazev_en']
print(f"Název zvířete v češtině: {index_34_cz}")
print(f"Název zvířete v angličtině: {index_34_en}")
#Název zvířete v češtině: Ibis bílý
#Název zvířete v angličtině: White ibis