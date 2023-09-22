# main.py

import hashlib
import time
from block import Block, Blockchain

def main():
    blockchain = Blockchain()  # Rename the variable

    while True:
        print("1. Add transactions")
        print("2. View blockchain")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            data = input("Enter transaction data: ")
            blockchain.add_block(data)  # Add the transaction directly to the blockchain
            print("\nTransaction added to the blockchain!\n")
        elif choice == "2":
            for block in blockchain.chain:
                print("Index:", block.index)
                print("Block Hash:", block.hash)
                print("Previous Hash:", block.previous_hash)
                print("Timestamp:", block.timestamp)
                print("Transactions:", block.transactions)
                print()
        elif choice == "3":
            break

if __name__ == "__main__":
    main()