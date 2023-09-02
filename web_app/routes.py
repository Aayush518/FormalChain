from flask import Blueprint, jsonify, request
from app.transaction import Transaction
from uuid import uuid4

def create_blockchain_routes(blockchain):
    blockchain_bp = Blueprint('blockchain', __name__)

    @blockchain_bp.route('/mine', methods=['GET'])
    def mine():
        # Mining a new block
        last_block = blockchain.last_block
        last_proof = last_block['proof']
        proof = blockchain.proof_of_work(last_proof)

        # Reward the miner for mining a new block
        blockchain.new_transaction(
            sender="0",  # Special sender to signify mining reward
            recipient=str(uuid4()),  # Miner's address
            amount=config.MINING_REWARD
        )

        # Create a new block and add it to the chain
        previous_hash = blockchain.hash(last_block)
        block = blockchain.new_block(proof, previous_hash)

        response = {
            'message': 'New block mined successfully!',
            'index': block['index'],
            'transactions': block['transactions'],
            'proof': block['proof'],
            'previous_hash': block['previous_hash'],
        }
        return jsonify(response), 200

    @blockchain_bp.route('/transactions/new', methods=['POST'])
    def new_transaction():
        data = request.get_json()
        required_fields = ['sender', 'recipient', 'amount']
        if not all(field in data for field in required_fields):
            return 'Missing fields in transaction data', 400

        # Create a new transaction
        index = blockchain.new_transaction(data['sender'], data['recipient'], data['amount'])
        response = {'message': f'Transaction will be added to Block {index}'}
        return jsonify(response), 201

    @blockchain_bp.route('/chain', methods=['GET'])
    def full_chain():
        # Return the entire blockchain
        return jsonify({'chain': blockchain.chain})

    return blockchain_bp
