#from hashlib import sha256
#import json
#from time import datetime

#class MyBlockchain:
#    def __init__(self, data, previous_block_hash, transaction_list, timestamp, nonce=0):

#        self.timestamp = datetime.utcnow()
#        self.data = data
#        self.previous_block_hash = previous_block_hash
#        self.transaction_list = transaction_list
#        self.nonce = nonce
#        self.calculate_valid_hash()
from datetime import datetime
import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_items = []

        self.new_block(previous_hash="On 03/Jan/2009 the banana plantation farm was founded.", proof=100)

# Create a new block listing key/value pairs of block information in a JSON object. Reset the list of pending transactions & append the newest block to the chain.

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'items': self.pending_items,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.pending_transactions = []
        self.chain.append(block)

        return block

#Search the blockchain for the most recent block.

    @property
    def last_block(self):
 
        return self.chain[-1]

# Add a new item with relevant info to the 'blockpool' - list of pending info for individual products. 

    def new_item(self, product, origin, producer, location, date):
        transaction = {
            'product': product,
            'origin': origin,
            'producer': producer,
            'location': location,
            'date': date
        }
        self.pending_transactions.append(transaction)
        return self.last_block['index'] + 1

# receive one block. Turn it into a string, turn that into Unicode (for hashing). Hash with SHA256 encryption, then translate the Unicode into a hexidecimal string.

    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash


blockchain = Blockchain()
i1 = blockchain.new_item("Banana", "Peru", "BananaRepublic", 'Supermarket', 2022)
i2 = blockchain.new_item("Pineapple", "Argentina", "PineappleParty", 'Supermarket', datetime())
i3 = blockchain.new_item("Tomato", "Ecuador", "TomatoFarm", 'Supermarket', datetime())
blockchain.new_block(12345)

i4 = blockchain.new_item("Beer", "Mexico", "BeerVille", 'Supermarket', datetime())
i5 = blockchain.new_item("Strawberries", "United States", "StrawberryRepublic", 'Supermarket', datetime())
i6 = blockchain.new_item("Honey", "Canada", "HoneyRepublic", 'Supermarket', datetime())
blockchain.new_block(6789)

print("Genesis block: ", blockchain.chain)
