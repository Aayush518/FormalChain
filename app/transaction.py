class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def to_dict(self):
        # Convert the transaction to a dictionary
        # Implement conversion logic here
        pass

    @staticmethod
    def from_dict(transaction_dict):
        # Create a transaction object from a dictionary
        # Implement creation logic here
        pass
