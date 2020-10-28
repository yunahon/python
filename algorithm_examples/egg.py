import math

def twoEggDrop(k): 
    return math.ceil((-1.0 + 
           math.sqrt(1 + 8 * k)) / 2) 
  

print(twoEggDrop(100))