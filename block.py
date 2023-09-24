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
        return Block(0, "0", ["Genesis Block"])  # Initialize index and transactions for the genesis block

    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def add_block(self, transactions):
        previous_block = self.chain[-1]
        new_index = previous_block.index + 1
        new_block = Block(new_index, previous_block.hash, transactions)
        self.chain.append(new_block)

    # Inside the `verify_merkle_root` method in the `Blockchain` class
    def verify_merkle_root(self, merkle_root):
        computed_merkle_root = self.compute_merkle_root()
        print("Computed Merkle Root:", computed_merkle_root)
        print("Provided Merkle Root:", merkle_root)
        return computed_merkle_root == merkle_root


    def compute_merkle_root(self):
        # Implement the logic to compute the Merkle root of all transactions in the blockchain
        merkle_tree = [block.transactions for block in self.chain]
        while len(merkle_tree) > 1:
            temp = []
            for i in range(0, len(merkle_tree), 2):
                if i + 1 < len(merkle_tree):
                    combined = merkle_tree[i] + merkle_tree[i + 1]
                    hash_value = hashlib.sha256(combined.encode()).hexdigest()
                    temp.append(hash_value)
                else:
                    temp.append(merkle_tree[i])
            merkle_tree = temp
        return merkle_tree[0] if merkle_tree else None

    def get_blockchain_size(self):
        return len(self.chain)
