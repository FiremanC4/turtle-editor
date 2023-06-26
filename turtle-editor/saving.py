import data
import os

path = os.path.realpath(__file__)
path = os.path.dirname(path)
os.chdir(path)

def save(fileName = None, auth = None):
    if not(fileName): fileName = fileExists()
    else: fileName = f'{fileName}.py'
    fileName = f'records/{fileName}'

    copyBlank(fileName, auth)

    with open(fileName, 'a') as f:
        for action in data.actions:
            f.write(action + '\n')

        f.write('wn.exitonclick()') # Exit program when window is closed
    
    print(f'[S] Saved to {path}records/{fileName}')

def fileExists():
    name = f'{data.untitled}{data.num}.py'
    while name in os.listdir():
        data.num += 1
        name = f'{data.untitled}{data.num}.py'
    return name

def copyBlank(fileName, auth):
    os.makedirs(os.path.join(path, 'records', ''), exist_ok=True)
    with open('files/blank.py', 'r') as f:
        with open(fileName, 'w') as f2:
            if auth: f2.write(f'#=============\n#Created by {auth}\n#=============\n') # Add author to file
            for line in f:
                if line.startswith('#'): continue
                f2.write(line)

def GoTo(x, y):
    data.actions.append(f'Tt.goto({x}, {y})')

def Up():
    data.actions.append(f'Tt.up()')

def Down():
    data.actions.append('Tt.down()')

def Fd(distance):
    data.actions.append(f'Tt.fd({distance})')

def Left(angle):
    data.actions.append(f'Tt.left({angle})')

def Right(angle):
    data.actions.append(f'Tt.right({angle})')

def FillColor(color):
    data.actions.append(f'Tt.fillcolor("{color}")')

def BeginFill():
    data.actions.append('Tt.begin_fill()')

def EndFill():
    data.actions.append('Tt.end_fill()')

def Circle(radius):
    data.actions.append(f'Tt.circle({radius})')

def Seth(heading):
    data.actions.append(f'Tt.seth({heading})')

def RandomMSnow(high):
    data.actions.append(f'randomMountainSnow = {high}')
