import math


    
print('Quadratic Solve-Yes\nax^ + bx + c = 0')

halfX = int(input('X graph length ?'))  
halfY = int(input('Y graph length ?')) 
sizeX = halfX  * 2 + 1
sizeY = halfY  * 2 + 1
accur = int(input('1/n accuracy ?'))

# Make Base Array [x][y] 11x11
array = [[ ' ' for i in range(sizeY) ] for j in range(sizeX)]
array[halfX] =  ['|' for i in range (sizeY)]

for x in array:
  x[halfY] = '-'

# Format and print [x][y] map
def format(array):
  for i in range (len(array)):
    l = ''
    for x in array:
      l += x[i]
    print(l)

a = float(input('a ?'))
b = float(input('b ?'))
c = float(input('c ?'))

tCords = []

# Adds X mark for each true value
for x in range (sizeX * accur):
  x = x / accur
  shiftX = x - halfX
  shiftY = int(round((a * (shiftX**2) + b * shiftX + c + 1e-15)))

  y = int(str(-shiftY + halfY))
  if (y < sizeY and y > -1) :
    x = int(round(x + 1e-15))
    array[x][y] = 'x'


print(tCords)

format(array)
print(str(a)+'x^2 +',str(b)+'x +',str(c),'= 0')