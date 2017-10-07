class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transaction = []

    def new_block(self):
        """Create a new block and adds it the the chain"""
        pass

    def new_transaction(self):
        """Adds a new transaction to the list of transaction"""
        pass

    @staticmethod
    def hash(block):
        """Hash a block"""
        pass

    @property
    def last_block(self):
        """Returns the last block in the chain"""
        pass

