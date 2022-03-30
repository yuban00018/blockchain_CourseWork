import pandas as pd
import matplotlib.pyplot as plt

transactions = pd.read_csv('../data/n-transactions-per-block.csv',header=None,names=['Date','Transactions'])
print(transactions.head())
print(transactions.info())

transactions['Date'] = pd.to_datetime(transactions['Date'],format="%Y-%m-%d")
transactions.index = transactions['Date']
del transactions['Date']

transactions.plot()
plt.show()