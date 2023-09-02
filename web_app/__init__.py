from flask import Flask

def create_app(blockchain):
    app = Flask(__name__)

    # Register your blockchain blueprint
    from .routes import create_blockchain_routes
    app.register_blueprint(create_blockchain_routes(blockchain))

    return app
