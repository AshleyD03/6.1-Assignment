import math

print('Quadratic Solve-Yes\nax^ + bx + c = 0')
a = int(input('a ?'))
b = int(input('b ?'))
c = int(input('c ?'))

ans_1 = (-b + math.sqrt((b**2 - (4 * a * c)))) / (2 * a)
ans_2 = (-b - math.sqrt((b**2 - (4 * a * c)))) / (2 * a)

print('for :\n'+str(a)+'x^2 +',str(b)+'x +',str(c),'= 0\nx =',str(ans_1),',',str(ans_2))