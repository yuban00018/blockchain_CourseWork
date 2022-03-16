from bitcoin import *

my_private_key = random_key()
print("Private Key: %s\n" % my_private_key)

my_public_key = privtopub(my_private_key)
print("Public Key: %s\n" % my_public_key)

my_bitcoin_address = pubkey_to_address(my_public_key)
print("Bitcoin Address: %s" % my_bitcoin_address)
