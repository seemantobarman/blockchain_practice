from coin import Block,BlockChain

one = BlockChain()
one.AddBlock(Block(1,"9/12/2020",100))
one.AddBlock(Block(2,"10/12/2020",200))

for block in one.chain:
    print(block)
