import pandas as pd
import matplotlib.pyplot as plt
file_path = '/Users/karolinagerych/Desktop/platy_2021_02.csv'
data = pd.read_csv(file_path)

plt.bar(data['cislo_zamestnance'], data['plat'], color='pink', edgecolor='purple')
plt.xlabel('Číslo zaměstnance')
plt.ylabel('Plat')
plt.title('Výše platů')
plt.show()