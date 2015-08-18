from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)
from random import *

#last = smell()
#while True:
#  move()
#  if last < smell()

while True:
  if touch() == "wall":
    turn(2)
    
  if left_side() == "fruit":
    turn(-1)
    move()
    continue
   
  if right_side() == "fruit":
    turn(1)
    move()
    continue
  
  for i in range(4):
    if look() == "fruit":
      move()
      break
    else:
      turn(1)
  move()