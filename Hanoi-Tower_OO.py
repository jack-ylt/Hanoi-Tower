# -*- coding: utf-8 -*-
"""
The Tower of Hanoi

Created on Sun Aug 20 16:15:17 2017
@author: Jack
"""


# Lets think of the discs as being animated.
# and that we can request one of them to move itself, 
# along with all of the smaller brethren above it, to another peg. 

# We'll have each disc use the following strategy. 
    # If there is no smaller disc on top, simply move to the requested peg. 
    # But if there is, pass the buck. 
    # First ask the smaller disc above you to move to the alternate peg 
    # (along with its brethren above, if any), 
    # make your move, and finally ask the same above disc to now move to your peg. 
    # When that is done, declare success. 

# Note: Each disc will need only to talk to the one just smaller.



def get_alternate(peg1, peg2):
    all_pegs = set(['A', 'B', 'C'])
    peg_1and2 = set([peg1, peg2])
    alternate = all_pegs.difference(peg_1and2).pop()
    return alternate



class Disc(object):
    total_move_times = 0
    
    def __init__(self, name, peg='A'):
        self.name = name
        self.peg = peg
        
    def __str__(self):
        return self.name
    
    def set_above_disc(self, other_disc):
        self.above_disc = other_disc
        
    def get_above_disc(self):
        return self.above_disc
    
    def move(self, destination):
        print("Disc{} move from {} to {}.".\
              format(self.name, self.peg, destination))
        self.peg = destination
        Disc.total_move_times += 1
        
    def be_requested(self, destination): 
        """
        be requested to move from original position to the destination
        """
        print("Disc{}: I have been requested to move to {}.".\
              format(self.name, destination))
        
        if not self.above_disc:
            return self.move(destination)
        
        # remove the above_disc disc
        alternate = get_alternate(self.peg, destination)
        print ("Disc{}: Asking disc{} to get out of my way and move to {}.".\
              format(self.name, self.above_disc.name, alternate))
        self.above_disc.be_requested(alternate)
        self.move(destination)
       
        # let the above_disc disc rejoin
        print ("Disc{}: Asking disc{} to rejoin me on {}.".\
               format(self.name, self.above_disc.name, destination))
        self.above_disc.be_requested(destination)



class Tower(object):
    def __init__(self, size, discs=None):
        self.size = size
        if discs == None:
            self.discs = self.create_discs()
            self.init_discs()
        
    def __str__(self):
        return str([str(i) for i in self.discs])
        
    def create_discs(self):
        """
        create the discs in order
        """
        return [Disc(str(i)) for i in range(1, self.size + 1)[::-1]]
    
    def init_discs(self):
        """
        set disc.above_disc for each discs.
        """
        for i in range(len(self.discs)):
            try:
                self.discs[i].set_above_disc(self.discs[i+1])
            except:
                self.discs[i].set_above_disc(None)
                
    def play(self):
        """
        move all discs from peg A to peg C
        """
        print "move tower: {} from peg A to C".format(self)
        self.discs[0].be_requested('C')
        print "\nTotal moves: ", (Disc.total_move_times)



if __name__ == '__main__':
    tower = Tower(3)
    tower.play()
    
        
        