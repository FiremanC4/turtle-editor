import os

path = os.path.realpath(__file__)
path = os.path.dirname(path)
os.chdir(path)

# with open('blank.py', 'r') as f:
#     for line in f:
#         if line.startswith('#'): continue
#         print(line, end='')

os.makedirs(os.path.join(path, 'records', ''), exist_ok=True)