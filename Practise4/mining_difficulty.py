import pandas as pd
import matplotlib.pyplot as plt

difficulty = pd.read_csv('../data/difficulty.csv',header=None,names=['Date',"Difficulty"])
print(difficulty.head())
print(difficulty.info())

difficulty['Date'] = pd.to_datetime(difficulty['Date'],format='%Y-%m-%d')
difficulty.index = difficulty['Date']
del difficulty['Date']

difficulty.plot()
plt.show()