from uuid import uuid4

from blockchain import Blockchain

from flask import Flask, jsonify, request

# Instantiate our Node
app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-','')

# Instantiate the Blockchain
blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    return "We will mind a new Block"


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()
    print(values)
    # Check that the required fields are in the POST'ed data
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing parameters', 400

    # Crate a new transaction
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])

    response = {
        'message': f'Transaction will be added to Block {index}',
    }
    return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
