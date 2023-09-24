# main.py

import time
from block import Block, Blockchain
from tree import MerkleTree

def main():
    blockchain = Blockchain()
    tree = MerkleTree()

    while True:
        print("1. Add transactions")
        print("2. View blockchain")
        print("3. Verify blockchain")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            data = input("Enter transaction data: ")
            tree.add_transaction(data)
            print("\nTransaction added to the Merkle tree!\n")
        elif choice == "2":
            for block in blockchain.chain:
                print("Index:", block.index)
                print("Block Hash:", block.hash)
                print("Previous Hash:", block.previous_hash)
                print("Timestamp:", block.timestamp)
                print("Transactions (Merkle Root):", block.transactions)
                print()
        elif choice == "3":
            if blockchain.verify_merkle_root(tree.build_tree()):
                print("Blockchain is verified and valid.")
            else:
                print("Blockchain verification failed. It may have been tampered with.")
        elif choice == "4":
            break

if __name__ == "__main__":
    main()
