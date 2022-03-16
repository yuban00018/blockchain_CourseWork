from blockchain import blockexplorer


block = blockexplorer.get_block('00000000000000000009a8642492b1f5ebbaa141b2cf357f26c67346e8bdc092')

print("Block Fee: %s" % block.fee)
print("Block size: %s" % block.size)
print("Block transactions: %s" % block.transactions)

block = blockexplorer.get_latest_block()
