# Hanoi-Tower

Two solutions to the Hanoi-Tower.

# The recusive solution:
if there is only one disc：
    just move it directly.
else：
    move all above discs to alternate
    move the bottom disc to destination
    move all above discs to destination
  
  
  
# The Object-Oreiginted solution:
Lets think of the discs as being animated. Then we can request one of them to move itself, along with all of the smaller brethren above it, to another peg. 

We'll have each disc use the following strategy:
    if there is no smaller disc on top:
	    simply move to the requested peg. 
    else:
	    pass the buck. 
        first ask the smaller disc above you to move to the alternate peg 
        (along with its brethren above, if any), 
        make your move, and finally ask the same above disc to now move to your peg. 
        when that is done, declare success. 

Note: each disc will need only to talk to the one just smaller.
