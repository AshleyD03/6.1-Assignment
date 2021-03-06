# Finished p3 Work
# Further evidence of use of programming structure and design

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
  while True:
      try:
        for i in range (sizeX):
            l = ''
            for x in array:
                if (i != sizeX) :
                    l += x[i]    
            print(l)
        break
        
      # Error only occurs under large x y conditions on last line
      # May be due to size of 2D array being 50+ 
      except IndexError:
          break
    
a = float(input('a ?'))
b = float(input('b ?'))
c = float(input('c ?'))

# Adds X mark for each true value
for x in range (sizeX * accur):
  x = x / accur
  shiftX = x - halfX
  shiftY = int(round((a * (shiftX**2) + b * shiftX + c + 1e-15)))

  y = int(str(-shiftY + halfY))
  if (y < sizeY and y > -1) :
    x = int(round(x + 1e-15))
    array[x][y] = 'x'

format(array)
print(str(a)+'x^2 +',str(b)+'x +',str(c),'= 0')