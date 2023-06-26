import movement as move
from tkinter import colorchooser
import data 
import saving
import config

def click(x, y):
    if data.ready:
        data.ready = False
        xy = (x, y)
        curentShape = data.curentShape

        if curentShape != 'rectangle':
            data.rectangle = []
            print(f'| Clicked: {x=}, {y=} |', xy)
            exec(f'move.{curentShape}(xy)')
            # if curentShape != 'mountain': data.actions.append(f'{curentShape}({xy})')
        else:
            if data.rectangle:
                data.rectangle += [x, y]
                print(f'| End click:, {x=}, {y=} |', xy)
                move.rectangle(data.rectangle)
                # data.actions.append(f'{curentShape}({data.rectangle})')
                data.rectangle = []
            else:
                data.rectangle = [x, y]
                print(f'| Start click:, {x=}, {y=} |', xy)
        data.ready = True


def chooseColor(x, y):
    if data.ready:
        color = colorchooser.askcolor()
        if color[1]: 
            data.color = color[1]
            data.actions.append(f'color = "{data.color}"')
            print(f"| Swidched color to: {color[1]}")
        else: print('| Color not chosen')
    
def chooseSize(x, y):
    if data.ready:
        size = int(input('Enter size: '))
        if size:
            data.size = size
            data.actions.append(f'size = {data.size}')
            print(f'| Swidched size to: {size}')
        else: print('| Size not chosen')


def keyZ():
    print('[Z] switched to triangle')
    data.curentShape = 'triangle'

def keyX():
    print('[X] switched to square')
    data.curentShape = 'square'

def keyC():
    print('[C] switched to circle')
    data.curentShape = 'circle'

def keyV():
    print('[V] switched to rectangle')
    data.curentShape = 'rectangle'

def keyB():
    print('[B] switched to mountain')
    data.curentShape = 'mountain'

def keyN():
    print('[N] switched to tree')
    data.curentShape = 'tree'


def keyS():
    if config.askForFileName:
        inp = input('Enter file name: ')
        if inp: author = input('Enter author: ')
        else: author = None
        print('[S] saving')
        saving.save(inp, author)
    else: 
        print('[S] saving')
        saving.save()