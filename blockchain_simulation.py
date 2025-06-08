import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return hashlib.sha256((str(self.index) + str(self.timestamp) +
                               str(self.data) + str(self.previous_hash) +
                               str(self.nonce)).encode()).hexdigest()

# Create 3 blocks
blockchain = [Block(0, time.time(), "Genesis Block", "0")]
blockchain.append(Block(1, time.time(), "Second Block", blockchain[-1].hash))
blockchain.append(Block(2, time.time(), "Third Block", blockchain[-1].hash))

# Display blocks
for block in blockchain:
    print(f"Block {block.index}:")
    print(f"  Data: {block.data}")
    print(f"  Hash: {block.hash}")
    print(f"  Prev Hash: {block.previous_hash}\n")

# Tamper with Block 1
print("Tampering Block 1...")
blockchain[1].data = "Tampered Data"
blockchain[1].hash = blockchain[1].calculate_hash()
print(f"New Hash of Block 1: {blockchain[1].hash}")
print(f"Previous Hash in Block 2 (unchanged): {blockchain[2].previous_hash}")
