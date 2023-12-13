import pandas as pd
import matplotlib.pyplot as plt
file_path = '/Users/karolinagerych/Desktop/platy_2021_02.csv'
data = pd.read_csv(file_path)

bins = range(30000, 60000, 2000)
plt.hist(data['plat'], bins=bins, edgecolor='black', alpha=1)
plt.xlabel('Plat')
plt.ylabel('Číslo zaměstnance')
plt.title('Histogram')
plt.show()