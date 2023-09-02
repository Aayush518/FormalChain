from app.blockchain import Blockchain
from web_app import create_app

# Create a blockchain instance
blockchain = Blockchain()

# Create a Flask app
app = create_app(blockchain)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
