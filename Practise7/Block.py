import hashlib as hasher
import random as rand
import time
import datetime as date
import ipyparallel as ipp
import numpy as np
import matplotlib.pyplot as plt


class Block:
    def __init__(self, index, timestamp, data, previous_hash, nonce=0):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce  # set to zero as default not applicable in first section
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        # Your code for QUESTION 1 Here

        sha = hasher.sha256()
        block_hash = (str(self.index) +
                      str(self.timestamp) +
                      str(self.data) +
                      str(self.previous_hash) +
                      str(self.nonce))
        block_hash = block_hash.encode('utf-8')
        sha.update(block_hash)
        return sha.hexdigest()