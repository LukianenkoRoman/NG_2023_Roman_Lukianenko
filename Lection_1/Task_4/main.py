import math

a = float(input('enter a:'))
b = float(input('enter b:'))
c = float(input('enter c:'))

discriminant =  b**2 - 4 * a * c 

if discriminant > 0:
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    print('roots:', x1, x2)
elif discriminant == 0:
    x = -b / (2*a)
    print('only one root:', x)
else:
    print('none decision:')
