from bitcoin import *

private_key1 = random_key()
private_key2 = random_key()
private_key3 = random_key()

print("Private key1: %s" % private_key1)
print("Private key2: %s" % private_key2)
print("Private key3: %s\n" % private_key3)

public_key1 = privtopub(private_key1)
public_key2 = privtopub(private_key2)
public_key3 = privtopub(private_key3)

print("Public key1: %s" % public_key1)
print("Public key2: %s" % public_key2)
print("Public key3: %s\n" % public_key3)

multi_sig = mk_multisig_script(private_key1, private_key2, private_key3, 2, 3)
multi_address = scriptaddr(multi_sig)
print("Multi signature address: %s" % multi_address)
