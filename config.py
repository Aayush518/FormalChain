# Configuration settings for your blockchain project

# Network port for the Flask app
FLASK_PORT = 5000

# Mining difficulty level (adjust as needed)
MINING_DIFFICULTY = 4  # Adjust for your requirements

# Mining reward for miners (in your cryptocurrency)
MINING_REWARD = 1.0  # Example: 1 unit of your cryptocurrency

# Genesis block data
GENESIS_DATA = {
    'index': 1,
    'previous_hash': '0',
    'timestamp': 0,
    'transactions': [],
    'proof': 100,
}
