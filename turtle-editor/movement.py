import config
import data
import saving as sv
Tt = config.Tt

#system
def upTo(a):
    Tt.up()
    Tt.seth(90)
    Tt.fd(a)
    Tt.seth(0)
    Tt.down()

    sv.Up()
    sv.Seth(90)
    sv.Fd(a)
    sv.Seth(0)
    sv.Down()

def preparing(size, color, xy, move = True):
    if xy:
        Tt.up() 
        Tt.goto(*xy)
        Tt.down()
        sv.Up()
        sv.GoTo(*xy)
        sv.Down()

    if move: 
        Tt.fd(-size / 2)
        sv.Fd(-size / 2)
    if color: 
        Tt.fillcolor(color)
        Tt.begin_fill()
        sv.FillColor(color)
        sv.BeginFill()

def ending(size, color, move = True):
    if color: 
        Tt.end_fill()
        sv.EndFill() 
    if move: 
        Tt.fd(size / 2)
        sv.Fd(size / 2)


#shapes
def triangle(xy = False, size = False, color = False): 
    if not(size) : size  = data.size
    if not(color): color = data.color

    preparing(size, color, xy)
    for _ in range(3):
        Tt.forward(size)
        Tt.left(120)
        sv.Fd(size)
        sv.Left(120)
    ending(size, color)

def square(xy = False):
    size = data.size
    color = data.color

    preparing(size, color, xy)
    for _ in range(4):
        Tt.forward(size)
        Tt.left(90)
        sv.Fd(size)
        sv.Left(90)
    ending(size, color)

def circle(xy = False):
    size = data.size / 2
    color = data.color

    preparing(size, color, xy, move=False)
    Tt.circle(size)
    sv.Circle(size)
    ending(size, color, move=False)

def rectangle(xy, color = False):
    size = False
    if not(color): color = data.color

    preparing(size, color, xy[0:2], False)
    
    Tt.goto(xy[0], xy[3])
    Tt.goto(xy[2], xy[3])
    Tt.goto(xy[2], xy[1])
    Tt.goto(xy[0], xy[1])

    sv.GoTo(xy[0], xy[3])
    sv.GoTo(xy[2], xy[3])
    sv.GoTo(xy[2], xy[1])
    sv.GoTo(xy[0], xy[1])
        
    ending(size, color, False)

def mountain(xy, snow = False):
    if not(snow): snow = data.randomMountainSnow()
    sv.RandomMSnow(snow)

    triangle(xy)
    upTo(data.size * (snow-1) * data.sqrt3dev2/snow)
    triangle(False, data.size/snow, color = 'white')
        
def tree(xy, color = False):
    size = data.size
    if data.color == 'blue': color = 'green'
    a = size / 9
    Rxy = [xy[0] + data.logHalfWidth * a, xy[1], xy[0] - data.logHalfWidth * a, xy[1] + a]
    
    rectangle(Rxy, 'brown')
    Tt.up()
    Tt.fd(-data.logHalfWidth * a)

    sv.Up()
    sv.Fd(-data.logHalfWidth * a)

    upTo(a)
    Tt.down()
    sv.Down()

    for i in range(3):
        triangle(False, a * data.treeSide - (i * a), color)
        upTo(2 * a)
