from tealight.logo import move, turn

def tri(scale):
  for i in range(3):
    move(scale)
    turn(120)
    

def trifrac(level, scale):
  if level == 1:
    return
  
  scale = level * 2
  tri(scale)
  for i in range(3):
    move(scale)
    turn(120)
    trifrac(scale/2)

turn(-90)
trifrac(1, 100)