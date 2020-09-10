from blocks import Block

Block_one = Block("Random text...",["A to B","B to C","C to D"])
print(Block_one.block_hash())

Block_two = Block(Block_one.block_hash(),["D to E","E to F","F to G"])
print(Block_two.block_hash())

Block_three = Block(Block_two.block_hash(),["G to H","H to I","I to J"])
print(Block_three.block_hash())

Block_four = Block(Block_three.block_hash(),["J to K","K to L","L to M"])
print(Block_four.block_hash())

Block_five = Block(Block_four.block_hash(),["M to N","N to O","O to P"])
print(Block_five.block_hash())




