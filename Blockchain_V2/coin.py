import hashlib
import json

class Block:
    def __init__(self,nonce,transaction,timestamp,previous_hash=""):
        self.nonce = nonce
        self.transaction = transaction
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        block_details=json.dumps({"nonce":self.nonce, "timestamp":self.timestamp, "transaction":self.transaction, "previous_hash":self.previous_hash},sort_keys=True).encode()
        hash_calculation = hashlib.sha256(block_details).hexdigest()
        return hash_calculation

    def hash_details(self):
        print("Previous Hash: " +self.previous_hash)
        print("Current Hash: " +self.hash)
    
