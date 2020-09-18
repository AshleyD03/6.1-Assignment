import math

sizeX = 5 * 2 + 1
sizeY = 5 * 2 + 1

# Make Base Array [x][y] 11x11
array = [[ ' ' for i in range(sizeY) ] for j in range(sizeX)]
array[5] =  ['|' for i in range (sizeY)]

for x in array:
  x[5] = '-'

# Format and print [x][y] map
def format(array):
  for i in range (len(array)):
    l = ''
    for x in array:
      l += x[i]
    print(l)
    
print('Quadratic Solve-Yes\nax^ + bx + c = 0')
a = float(input('a ?'))
b = float(input('b ?'))
c = float(input('c ?'))

for i in range (sizeX):
  x = i - 5
  y = int(str(round(-(a * (x**2) + b * x + c + 1e-15) + 5))[:-2])
  if (y < 11 and y > -1) :
    array[i][y] = 'x'

format(array)
print(str(a)+'x^2 +',str(b)+'x +',str(c),'= 0')