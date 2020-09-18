import math

print('Quadratic Solve-Yes\nax^ + bx + c = 0')
a = int(input('a ?'))
b = int(input('b ?'))
c = int(input('c ?'))

print(str(a)+'x^2 +',str(b)+'x +',str(c),'= 0')

det = b**2 - (4 * a * c)

if (det < 0) :
  print('No real routes')
  
elif (det == 0) :
  ans = ans = (-b + math.sqrt(det)) / (2 * a)
  print('x =', str(ans))
  
else :
  ans_1 = (-b + math.sqrt(det)) / (2 * a)
  ans_2 = (-b - math.sqrt(det)) / (2 * a)
  print('x =', str(ans_1), ',', str(ans_2))
