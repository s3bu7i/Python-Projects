
import hashlib
from datetime import datetime, date

class Block:
    
    def __init__(self,data,previoushash = ''):
        self.data = data
        self.timestanp = datetime.now()
        self.previoushash = previoushash
        self.hash = self.addHash()
        
    def addHath(self):
        block_hash = hashlib.sha256()
        data = '_'.join(map(str,self.data))
        block_hash.update(
            data +
            self.timestanp.isoformat() + self.previoushash
        )
        
        return block_hash.hexdigest()
        
class Blockchain:
    def __init__(self):
        self.chain = [self.genesisBlock()]
    
    def genesisBlock(self):
        return Block([],'000')
    
    def lastChain(self):
        return self.chain[-1]
                
    def addBlock(self, newblock):
        newblock.previoushash = self.lastChain().hash
        newblock.hash =newblock.addHash()
        self.chain.append(newblock)
        
    def chainvaild(self):
        for i in range(1,len(self.chain)):
            block =self.chain[i]
            previous_block = self.chain[i-1]
            
            if block.hash != block.addHath():
                return False
            
            elif block.previoushash != previous_block.hash:
                return False
            
        return True
            
            
            
            