import hashlib
import json
from time import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # Create the genesis block
        self.new_block(proof=100, previous_hash='1')

    def new_block(self, proof, previous_hash=None):
        """
        Create a new block in the blockchain.

        :param proof: The proof given by the Proof of Work algorithm
        :param previous_hash: Hash of the previous block (optional)
        :return: New block
        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]) if self.chain else None,
        }

        # Reset the list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        Create a new transaction to go into the next mined block.

        :param sender: Address of the sender
        :param recipient: Address of the recipient
        :param amount: Amount
        :return: The index of the block that will hold this transaction
        """
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        }
        self.current_transactions.append(transaction)
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """
        Hash a block.

        :param block: Block
        :return: Hash value
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        """
        Get the last block in the blockchain.

        :return: Last block
        """
        return self.chain[-1]
