import pandas as pd
import matplotlib.pyplot as plt

tylerdf = pd.read_csv('NC_Tyler.csv')
print(tylerdf.head())

occur = list(tylerdf['Occurences'])
print(occur)
index = [i + 1 for i in range(len(occur))]
print(index)

plt.figure(figsize=(10, 6))
plt.bar(index, occur, align='center', width=.7)
plt.grid(axis="y")
plt.xticks(index)
plt.show()
