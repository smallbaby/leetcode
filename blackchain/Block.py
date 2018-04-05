# -*- coding: utf-8 -*-

import hashlib as hasher
import datetime as date


def _byte(key):
    return bytearray(str(key).encode())

def _hash(key):
    return hasher.sha256(key).hexdigest()


# 第一版：缺交易信息、工作量证明、共识机制、

class Block:

    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        hkey = _byte(self.index) + _byte(self.timestamp) + _byte(self.data) + _byte(self.previous_hash)
        return _hash(hkey)

def create_genesis_block():
    #  Manually construct a block with index 0 and arbitrary previous hash
    return Block(0, date.datetime.now(), "Genesis Block", "0")

def next_block(last_block):
    this_index = last_block.index + 1
    timestamp = date.datetime.now()
    data = 'hello i\'m block ' + str(this_index)
    hash  = last_block.hash
    return Block(this_index, timestamp, data, hash)


def blackchain_instace():
    return [create_genesis_block()]


# 创始块
blockchain = blackchain_instace()
previous_block = blockchain[0]
num_of_blocks_to_add = 20
for i in range(0, num_of_blocks_to_add):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    print("Block #{} has been added to the "
          "blockchain!".format(block_to_add.index))
    print("Hash: {}".format(block_to_add.hash))
    print("Data: {}\n".format(block_to_add.data))

































x = 10
y = 1
# 8位  10亿
# 7位  亿
# 6位  4kw
# 5位  5bw
# 4位  8w
# #
# while True:
#     h = _hash(str(x*y))
#     if h[0:2] != '00':
#         y += 1
#     else:
#         print y,h
#         break









