from flask import Flask

def create_app():
    app = Flask(__name__)

    # Initialize the blockchain and user system
    from .blockchain import Blockchain
    from .user import User
    blockchain = Blockchain()
    user = User()

    # Register blueprints
    from web_app.routes import blockchain_bp, user_bp
    app.register_blueprint(blockchain_bp)
    app.register_blueprint(user_bp)

    return app

app = create_app()  # Create the Flask app instance
