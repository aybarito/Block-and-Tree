# block.py

import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, transactions):
        self.index = index 
        self.timestamp = time.time()
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = str(self.index) + str(self.timestamp) + str(self.previous_hash) + str(self.transactions)
        return hashlib.sha256(data.encode()).hexdigest()

class Blockchain:
    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")  # Initialize index for the genesis block

    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def add_block(self, transactions):
        previous_block = self.chain[-1]
        new_index = previous_block.index + 1  # Increment index
        new_block = Block(new_index, previous_block.hash, transactions)
        self.chain.append(new_block)