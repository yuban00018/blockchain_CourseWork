from blockchain import statistics


stats = statistics.get()
print("Bitcoin Trade Volume: %s" % stats.trade_volume_btc)
print("Bitcoin mined: %s" % stats.btc_mined)
print("Bitcoin market price: %s" % stats.market_price_usd)