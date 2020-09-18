import math

sizeX = 11
sizeY = 11

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
a = int(input('a ?'))
b = int(input('b ?'))
c = int(input('c ?'))

for i in range (11):
  x = i - 5
  y = -(a * (x**2) + b * x + c) + 5
  if (y < 11 and y > -1) :
    array[i][y] = 'x'

format(array)
print(str(a)+'x^2 +',str(b)+'x +',str(c),'= 0')