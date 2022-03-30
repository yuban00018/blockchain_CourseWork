import pandas as pd
import matplotlib.pyplot as plt

pd.options.mode.chained_assignment = None

bitcoins = pd.read_csv("../data/total-bitcoins.csv",header=None,names=['Date','Bitcoins'])

print(bitcoins.head())
print(bitcoins.info())

bitcoins['Date'] = pd.to_datetime(bitcoins['Date'],format="%Y-%m-%d")
bitcoins.index = bitcoins['Date']
del bitcoins['Date']
print(bitcoins.head())
print(bitcoins.info())

bitcoins.plot()
plt.show()
