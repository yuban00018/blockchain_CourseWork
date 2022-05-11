import datetime as date
import random as rand
import time

import matplotlib.pyplot as plt
import numpy as np

from Block import Block
from MinerNodeNaive import MinerNodeNaive


def test_question_1(index, block_time, data, previous_hash):
    new_block = Block(index, block_time, data, previous_hash)
    check_string = '2def27922fc1c67254a9cdb0c660b91abf9b135ad38fc13c7c77007448b824a0'
    print_statement = "PASSED!!! Move on to next Question" if str(
        new_block.hash) == check_string else "FAILED!!! Try Again"
    print(print_statement)


def test_question_2(genesis_block):
    block_1 = next_block(genesis_block)
    if block_1.index == 1 and\
            block_1.data == "Hey! I'm block 1" and\
            block_1.previous_hash == genesis_block.hash and\
            str(type(block_1.timestamp)) == "<class 'datetime.datetime'>":
        print("PASSED!!! Move on to next part")
    else:
        print("FAILED!!! Try again :(")


def test_question_3(blockchain, num_blocks):
    correct = True
    if len(blockchain) != num_blocks + 1:
        correct = False
    for i in range(len(blockchain) - 1):
        if blockchain[i + 1].previous_hash != blockchain[i].hash:
            correct = False
            break
    print_statement = "PASSED!!! Move on to the next Part" if correct else "FAILED!!! Try Again :("
    print(print_statement)


def test_question_4(blockchain_pow, num_blocks):
    correct = True
    difficulty = 3
    bound = generate_difficulty_bound(difficulty)
    if len(blockchain_pow) != num_blocks + 1:
        correct = False
    for i in range(len(blockchain_pow) - 1):
        if blockchain_pow[i + 1].previous_hash != blockchain_pow[i].hash:
            correct = False
            break
        if int(blockchain_pow[i + 1].hash, 16) > bound:
            correct = False
            break
    print_statement = "PASSED!!! Move on to the next Part" if correct else "FAILED!!! Try Again :("
    print(print_statement)


'''
Question 1
'''
block_time = '2019-10-17 00:37:35.256774'
data = 'Machine Learning Blockchain AI'
previous_hash = '6ffd1464f68ef4aeb385d399244efa19293ba5c842c464a82c02f8256ef71428'
index = 0

test_question_1(index, block_time, data, previous_hash)

'''
Question 2
'''


# Creates the first block with current time and generic data
def create_genesis_block():
    # Manually construct a block with
    # index zero and arbitrary previous hash
    return Block(0, date.datetime.now(), "Genesis Block", "0")


# Function that creates the next block, given the last block on the chain you want to mine on
def next_block(last_block, nonce=0):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Hey! I'm block " + str(this_index)
    this_prev_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_prev_hash)


genesis_block = create_genesis_block()
test_question_2(genesis_block)

'''
Question 3
'''
# Create the blockchain and add the genesis block
blockchain = [create_genesis_block()]

# Create our initial reference to previous block which points to the genesis block
previous_block = blockchain[0]

# How many blocks should we add to the chain after the genesis block
num_blocks = 20


def complete_chain(num_blocks, blockchain, previous_block):
    # Add blocks to the chain
    for i in range(0, num_blocks):
        # Your code for QUESTION 3 Here
        block_to_add = next_block(previous_block)
        blockchain.append(block_to_add)
        previous_block = block_to_add
        # Your code for QUESTION 3 ends Here
        # Tell everyone about it!
        print("Block #{} has been added to the blockchain!".format(block_to_add.index))
        print("Hash: {}\n".format(block_to_add.hash))


complete_chain(num_blocks, blockchain, previous_block)
test_question_3(blockchain, num_blocks)

'''
Question 4
'''


def generate_nonce(length=20):
    return ''.join([str(rand.randint(0, 9)) for i in range(length)])


def generate_difficulty_bound(difficulty=1):
    diff_str = ""
    for i in range(difficulty):
        diff_str += '0'
    for i in range(64 - difficulty):
        diff_str += 'F'
    diff_str = "0x" + diff_str  # "0x" needs to be added at the front to specify that it is a hex representation
    return (int(diff_str,
                16))  # Specifies that we want to create an integer of base 16 (as opposed to the default  base 10)


# Given a previous block and a difficulty metric, finds a nonce that results in a lower hash value
def find_next_block(last_block, difficulty, nonce_length):
    difficulty_bound = generate_difficulty_bound(difficulty)
    start = time.process_time()
    new_block = next_block(last_block)
    hashes_tried = 1
    # Your code for QUESTION 4 Starts here
    while int(new_block.hash, 16) > difficulty_bound:
        nonce = generate_nonce(nonce_length)
        new_block = Block(new_block.index, new_block.timestamp, new_block.data, new_block.previous_hash, nonce)
        hashes_tried += 1
        # Your code for QUESTION 4 Ends here
    time_taken = time.process_time() - start
    return time_taken, hashes_tried, new_block


'''
Crate Proof of Work Blockchain
'''
# Create the blockchain and add the genesis block
blockchain_pow = [create_genesis_block()]

# Create our initial reference to previous block which points to the genesis block
previous_block = blockchain_pow[0]

# How many blocks should we add to the chain after genesis block
num_blocks = 20

# magnitude of difficulty of hash - number of zeroes that must be in the beginning of the hash
difficulty = 3

# length of nonce that will be generated and added
nonce_length = 20


# Add blocks to the chain based on difficulty with nonces of length nonce_length
def create_pow_blockchain(num_blocks, difficulty, blockchain_pow, previous_block, nonce_length, print_data=1):
    hash_array = []
    time_array = []
    for i in range(0, num_blocks):
        time_taken, hashes_tried, block_to_add = find_next_block(previous_block, difficulty, nonce_length)
        blockchain_pow.append(block_to_add)
        previous_block = block_to_add
        hash_array.append(hashes_tried)
        time_array.append(time_taken)
        # Tell everyone about it!
        if print_data:
            print("Block #{} has been added to the blockchain!".format(block_to_add.index))
            print("{} Hashes Tried!".format(hashes_tried))
            print("Time taken to find block: {}".format(time_taken))
            print("Hash: {}\n".format(block_to_add.hash))
    return hash_array, time_array


hash_array, time_array = create_pow_blockchain(num_blocks, difficulty, blockchain_pow, previous_block, nonce_length)
test_question_4(blockchain_pow, num_blocks)

'''
Question 5
'''
# Initialize multiple miners on the network
berkeley_Miner = MinerNodeNaive("Berkeley Miner", 10)
stanford_Miner = MinerNodeNaive("Stanford Miner", 5)
MIT_Miner = MinerNodeNaive("MIT Miner", 2)
UCLA_Miner = MinerNodeNaive("UCLA Miner", 1)

miner_array = [berkeley_Miner, stanford_Miner, MIT_Miner, UCLA_Miner]


def create_compute_simulation(miner_array):
    compute_array = []
    for miner in miner_array:
        for i in range(miner.compute):
            compute_array.append(miner.name)
    return compute_array


compute_simulation_array = create_compute_simulation(miner_array)
rand.shuffle(compute_simulation_array)

chain_length = 20
blockchain_distributed = [create_genesis_block()]
genesis_block_dist = blockchain_distributed[0]
chain_difficulty = [rand.randint(2, 4) for i in range(chain_length)]

for i in range(len(chain_difficulty)):
    while len(blockchain_distributed) < i + 2:
        next_miner_str = rand.sample(compute_simulation_array, 1)[0]
        next_miner = berkeley_Miner  # random default (go bears)
        for miner in miner_array:
            if next_miner_str == miner.name:
                next_miner = miner
        next_miner.try_hash(chain_difficulty[i], blockchain_distributed)

'''
Blockchain Data Analytics
'''
blockchain = [create_genesis_block()]
previous_block = blockchain[0]
num_blocks = 10

# 3 different types of difficulty to analyze
difficulty_0 = 1
difficulty_1 = 2
difficulty_2 = 3
difficulty_3 = 4

nonce_length = 20

hash_array_0, time_array_0 = create_pow_blockchain(num_blocks, difficulty_0, blockchain, previous_block, nonce_length,
                                                   0)
print("Difficulty Level: {} complete".format(difficulty_0))
hash_array_1, time_array_1 = create_pow_blockchain(num_blocks, difficulty_1, blockchain, previous_block, nonce_length,
                                                   0)
print("Difficulty Level: {} complete".format(difficulty_1))
hash_array_2, time_array_2 = create_pow_blockchain(num_blocks, difficulty_2, blockchain, previous_block, nonce_length,
                                                   0)
print("Difficulty Level: {} complete".format(difficulty_2))
hash_array_3, time_array_3 = create_pow_blockchain(num_blocks, difficulty_3, blockchain, previous_block, nonce_length,
                                                   0)
print("Difficulty Level: {} complete".format(difficulty_3))

mean_arr_hash = [np.mean(hash_array_0), np.mean(hash_array_1), np.mean(hash_array_2), np.mean(hash_array_3)]
mean_arr_time = [np.mean(time_array_0), np.mean(time_array_1), np.mean(time_array_2), np.mean(time_array_3)]

plt.plot(mean_arr_hash)
plt.show()

diff_factor_1 = np.mean(hash_array_1) / np.mean(hash_array_0)
diff_factor_2 = np.mean(hash_array_2) / np.mean(hash_array_1)
diff_factor_3 = np.mean(hash_array_3) / np.mean(hash_array_2)
print("Factor of difficulty increase from 1 to 2: {}".format(diff_factor_1))
print("Factor of difficulty increase from 2 to 3: {}".format(diff_factor_2))
print("Factor of difficulty increase from 3 to 4: {}".format(diff_factor_3))
