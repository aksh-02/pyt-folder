import hashlib
import datetime

class Block:
    
    def __init__(self,index,timestamp,data,pre_hash):
        self.index=index
        self.timestamp=timestamp
        self.data=data
        self.previous_hash=pre_hash
        self.hash=self.hash_block()

    def hash_block(self):
        sha=hashlib.sha256()
        sha.update((str(self.index)+str(self.timestamp)+str(self.data)+str(self.previous_hash)).encode())
        return(sha.hexdigest())

def genesis_block(): # this creates the first block of the block chain
     return Block(0,datetime.datetime.now(),"Hi, I'm Genesis Block","0")

def next_block(last_block):
    present_index=last_block.index+1
    present_timestamp=datetime.datetime.now()
    present_data="Hi I'm block number "+str((present_index))
    present_prev_hash=last_block.hash
    return Block(present_index,present_timestamp,present_data,present_prev_hash)
    

if __name__=="__main__":
    block_chain=[genesis_block()]
    number_of_blocks=int(input())
    last_block=block_chain[0]
    for i in range(number_of_blocks):
        cur_block=next_block(last_block)
        block_chain.append(cur_block)
        last_block=cur_block
        # let's print the block chain
        print(cur_block.index)
        print("data stored is {}".format(cur_block.data))
        print(f"hash of this block is {cur_block.hash}\n")

