import hashlib
import json
from time import time
from uuid import uuid4

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.nodes = set()  # Set to store network nodes

        # Create the genesis block
        self.new_block(proof=100, previous_hash='1')

    def new_block(self, proof, previous_hash=None):
        # Create a new block in the blockchain
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reset the current list of transactions
        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        # Create a new transaction to be included in the next block
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    def proof_of_work(self, last_proof):
        # Simple Proof of Work algorithm (adjust MINING_DIFFICULTY in config.py)
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        # Check if the proof is valid (satisfies MINING_DIFFICULTY)
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:config.MINING_DIFFICULTY] == '0' * config.MINING_DIFFICULTY

    @staticmethod
    def hash(block):
        # Hashes a block using SHA-256
        return hashlib.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]
