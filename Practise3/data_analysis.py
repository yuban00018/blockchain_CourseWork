import pandas as pd
import matplotlib.pyplot as plt

pd.options.mode.chained_assignment = None

# read data
price = pd.read_csv('../data/bitcoin-price.csv')

# head
print(price.head())

# data info
print(price.info())

# data tail
print(price.tail())

# drop NA
price = price.dropna()
print(price.tail())

# reformat the date
price['Date'] = pd.to_datetime(price['Date'], format="%Y-%m-%d")
print(price.info())

# set date as the index
price.index = price['Date']
del price['Date']
print(price.head())

# data during 2010
print(price.loc['2010'])

# close price of 2017-08-01
print(price.loc['2017-08-01'])

# close price since 2017-08-01
print(price.loc['2017-08-01':])

# min price
print(price.min())

# max price
print(price.max())

# count mean std min 25% 50% 75% max
print(price.describe())

price.plot()
plt.show()

price.loc['2017'].plot()
plt.show()
