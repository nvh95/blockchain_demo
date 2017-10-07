from time import time


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transaction = []

    def new_block(self, proof, previous_hash=None):
        """
        Create a new block and adds it the the chain
        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash: (Optional) <str> hash of the previous block
        :return: <dict> a new block
        """
        block = {
            'index': len(self.chain) +1,
            'timestamp': time(),
            'transaction': self.current_transaction,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reset the current list of transaction
        self.current_transaction = []

        self.chain.append(block)

        return block

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
        return self.chain[-1]

