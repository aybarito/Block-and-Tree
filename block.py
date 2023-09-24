# block.py

import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, transactions, merkle_root):
        self.index = index
        self.timestamp = time.time()
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.merkle_root = merkle_root  # Add the Merkle root
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = str(self.index) + str(self.timestamp) + str(self.previous_hash) + str(self.transactions) + str(self.merkle_root)
        return hashlib.sha256(data.encode()).hexdigest()

class MerkleTree:
    def init(self, transactions):
        self.transactions = transactions
        self.root = self.build_merkle_tree()

    def build_merkle_tree(self):
        if len(self.transactions) == 0:
            return None

        if len(self.transactions) == 1:
            return self.transactions[0]

        new_transactions = []
        for i in range(0, len(self.transactions), 2):
            transaction1 = self.transactions[i]
            if i + 1 < len(self.transactions):
                transaction2 = self.transactions[i + 1]
            else:
                transaction2 = transaction1  # Duplicate for odd number of transactions
            combined = transaction1 + transaction2
            new_transactions.append(hashlib.sha256(combined.encode()).hexdigest())

        return self.build_merkle_tree(new_transactions)

class Blockchain:
    def create_genesis_block(self):
        return Block(0, "0", ["Genesis Block"], "0")

    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.transaction_pool = []

    def add_transaction(self, transaction):
        self.transaction_pool.append(transaction)

    def mine(self):
        if len(self.transaction_pool) == 0:
            print("No transactions to mine.")
            return

        merkle_tree = MerkleTree(self.transaction_pool)
        merkle_root = merkle_tree.root
        previous_block = self.chain[-1]
        new_index = previous_block.index + 1
        new_block = Block(new_index, previous_block.hash, self.transaction_pool, merkle_root)
        self.chain.append(new_block)
        self.transaction_pool = []

    def view_chain(self):
        for block in self.chain:
            print("Index:", block.index)
            print("Block Hash:", block.hash)
            print("Previous Hash:", block.previous_hash)
            print("Timestamp:", block.timestamp)
            print("Transactions:", block.transactions)
            print("Merkle Root:", block.merkle_root)
            print()
