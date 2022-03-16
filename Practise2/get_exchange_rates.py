from blockchain import exchangerates


ticker = exchangerates.get_ticker()
print("Bitcoin Prices in various currencies:")
for k in ticker:
    print(k, ticker[k].p15min)

btc = exchangerates.to_btc('EUR', 100)
print("100 euros in Bitcoin: %s " % btc)