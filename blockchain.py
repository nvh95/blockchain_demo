class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transaction = []

    def new_block(self):
        """Create a new block and adds it the the chain"""
        pass

    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined Block

        :param sender: <str> Address of the sender
        :param recipient: <str> Address of the recipient
        :param amount:  <int> Amount
        :return: <int> Index of block gold this transaction
        """

        self.current_transaction.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """Hash a block"""
        pass

    @property
    def last_block(self):
        """Returns the last block in the chain"""
        pass

