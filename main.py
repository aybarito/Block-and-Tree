import hashlib
import time
from block import Block, Blockchain, MerkleTree

def main():
    blockchain = Blockchain()  # Rename the variable

    while True:
        print("1. Add transactions")
        print("2. View blockchain")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            data = input("Enter transaction data: ")
            blockchain.add_transaction(data)  # Add the transaction to a transaction pool
            print("\nTransaction added to the transaction pool!\n")
        elif choice == "2":
            blockchain.mine()  # Mine a new block with transactions from the pool
            blockchain.view_chain()
        elif choice == "3":
            break

if name == "main":
    main()
