import movement as move
import config
import clickEvent as click
import data
import saving

config.wn.listen()

config.wn.onscreenclick(click.click, 1)
config.wn.onscreenclick(click.chooseColor, 3)
config.wn.onscreenclick(click.chooseSize, 2)


config.wn.onkey(click.keyZ, 'z') # triangle
config.wn.onkey(click.keyX, 'x') # square
config.wn.onkey(click.keyC, 'c') # circle
config.wn.onkey(click.keyV, 'v') # rectangle
config.wn.onkey(click.keyB, 'b') # mountain
config.wn.onkey(click.keyN, 'n') # tree

config.wn.onkey(click.keyS, 's') # save


config.wn.mainloop()
