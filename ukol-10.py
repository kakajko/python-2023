import pandas as pd
praha = pd.read_csv('/Users/karolinagerych/Desktop/zam_praha.csv')
plzen = pd.read_csv('/Users/karolinagerych/Desktop/zam_plzeň.csv')
liberec = pd.read_csv('/Users/karolinagerych/Desktop/zam_liberec.csv')
#part 1
praha['mesto'] = 'Praha'
plzen['mesto'] = 'Plzeň'
liberec['mesto'] = 'Liberec'

zamestnanci = pd.concat([praha, plzen, liberec], ignore_index=True)

platy = pd.read_csv('/Users/karolinagerych/Desktop/platy_2021_02.csv')

zamestnanci = zamestnanci.set_index('cislo_zamestnance')
platy = platy.set_index('cislo_zamestnance')
final = zamestnanci.join(platy, how='left')
final.reset_index(inplace=True)

print("size zamestnanci", zamestnanci.shape)
print("size platy:", platy.shape)
print("size final:", final.shape)

nepracuje = final[final['plat'].isnull()]
prumer = final.groupby('mesto')['plat'].mean()

print("RIP:")
print(nepracuje)

print("Kde jsou na tom líp?:")
print(prumer)

#part 2
vykazy= pd.read_csv('/Users/karolinagerych/Desktop/vykazy.csv')

h_dotace = vykazy.groupby('project')['hours'].sum()

print("Hodiny/projekt:")
print(h_dotace)
