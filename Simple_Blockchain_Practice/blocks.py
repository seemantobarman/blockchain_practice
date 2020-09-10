import hashlib
import re

# Unique Fingerprint = message + previous hash
class Block:
    def __init__(self, pre_hash, message):
        self.messages = message
        self.pre_hashs = pre_hash
        self.full_string_plus_hash = "".join(self.messages) + self.pre_hashs
        print("Concatination of message and hash: " +self.full_string_plus_hash)
    
    def block_hash(self):
        hash = "".join(hashlib.sha256(self.full_string_plus_hash.encode()).hexdigest())
        return hash