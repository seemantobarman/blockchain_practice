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

    def __str__(self):
        string = "nonce: "+str(self.nonce) +"\n"
        string += "transaction: "+str(self.transaction) +"\n"
        string += "timestamp: "+str(self.timestamp) +"\n"
        string += "previous hash: "+str(self.previous_hash) +"\n"
        string += "hash: "+str(self.hash) +"\n"

        return string


class BlockChain:
    def __init__(self):
        self.chain=[self.GenesisBlock(),]

    def GenesisBlock(self):
        genesis = Block(0,"First block of the chain","9/11/2020")
        return genesis

    def LastBlock(self):
        return self.chain[-1]

    def AddBlock(self,newBlock):
        newBlock.previous_hash = self.LastBlock().hash
        newBlock.hash = newBlock.calculate_hash()
        self.chain.append(newBlock)


