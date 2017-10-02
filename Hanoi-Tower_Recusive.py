# -*- coding: utf-8 -*-
"""
The Tower of Hanoi

Created on Sun Aug 20 23:12:27 2017
@author: Jack
"""



def play(tower):
    """
    move all discs on tower from peg A to peg C
    """
    global step
    step = 1
    print "move tower: {} from peg A to C".format(tower)
    move(tower, 'A', 'C')

def move(tower, original, destination):
    """
    move all above discs to alternate
    move the bottom disc to destination
    move all above discs to destination
    """   
    if len(tower) == 1:
        move_disc(tower[0], original, destination)
    else:
        bottom_disc = tower[0]
        above_discs = tower[1:]
        alternate = get_alternate(original, destination)
        
        move(above_discs, original, alternate)
        move_disc(bottom_disc, original, destination)
        move(above_discs, alternate, destination)

def move_disc(disc, original, destination):
    global step
    print "{}: move disc{} from {} to {}".\
            format(step, disc, original, destination)
    step += 1

def get_alternate(origianl, destination):
    all_pegs = ['A', 'B', 'C']  
    all_pegs.remove(origianl)
    all_pegs.remove(destination)
    return all_pegs[0]



if __name__ == '__main__':
    play([3, 2, 1])

