import pandas as pd
df = pd.read_csv('/Users/karolinagerych/Desktop/temperature.csv')
df.info()
print(df.head())

praha = df[df['City'] == 'Prague']
print("Data Praha:")
print(praha)
#tyhle tropy teda v listopadu nepamatuju :D bylo by teda fajn mít v názvu sloupce jednotky [F/C]

t_nad_osmdesat = df[df['AvgTemperature'] > 80]
print("Teplota vyšší než 80F:")
print(t_nad_osmdesat)

evropa_t_nad_sedesat = df[(df['AvgTemperature'] > 60) & (df['Region'] == 'Europe')]
print("Teplota v Evropě vyšší než 60F:")
print(evropa_t_nad_sedesat)

extrem = df[(df['AvgTemperature'] > 80) | (df['AvgTemperature'] < -20)]
print("Teploty vyšší než 80F nebo nižší než -20F:")
print(extrem)
