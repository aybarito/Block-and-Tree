import hashlib

class MerkleTree:
    def __init__(self):
        self.leaves = []

    def add_transaction(self, transaction):
        self.leaves.append(hashlib.sha256(transaction.encode()).hexdigest())

    def build_tree(self):
        tree = self.leaves[:]
        while len(tree) > 1:
            temp = []
            for i in range(0, len(tree), 2):
                if i + 1 < len(tree):
                    combined = tree[i] + tree[i + 1]
                    hash_value = hashlib.sha256(combined.encode()).hexdigest()
                    temp.append(hash_value)
                else:
                    temp.append(tree[i])
            tree = temp
        return tree[0] if tree else None
