import random

#main
size = 250
color = 'blue'

#clickEvent
rectangle = []
ready = True
curentShape = 'rectangle'

#movement
sqrt3dev2 = 0.8660254037844386 #sqrt(3) / 2
treeSide  = 4.618802153517006
logHalfWidth  = 0.5773502691896257
def randomMountainSnow(): return (random.random() * 2) + 3 #random from3 to 5

#save
actions = []
untitled = 'Untitled'
num = 1