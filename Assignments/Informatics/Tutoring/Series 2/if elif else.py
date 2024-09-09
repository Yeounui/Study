import math

x = float(input())
y = float(input())

r = math.sqrt(x**2 + y**2)
beta = math.pi*11/20 - math.atan(y/x)

sector = int(beta//(math.pi/10)+1)

if r < 6.35:
    print(50)
elif 6.35 < r < 15.9:
    print(25)
elif 15.9 < r < 97.4:
    print(sector)
elif 97.4 < r < 107.0:
    print(sector*3)
elif 107.0 < r < 160.4:
    print(sector)
elif 160.4 < r < 170.0:
    print(sector*2)
else:
    print(0)