

import hashlib
import time

class Block:
    def __init__(self,index,proof_no,prev_hash,data,timestamp = None):
        self.index = index
        self.proof_no = proof_no
        self.prev_hash = prev_hash
        self.data = data
        self.timestamp = timestamp
        
    def calculate_hash(self):
        
        block_of_sting = "{} {} {} {} {}".format(self.index,self.proof_no,self.prev_hash,self.data,self.timestamp)
        
        return hashlib.sha256(block_of_sting.encode().hexdigestr())
    
    def __repr__(self):
        return "{} - {} - {} - {} - {}".format(self.index,self.proof_no,self.prev_hash,self.data,self.timestamp)

