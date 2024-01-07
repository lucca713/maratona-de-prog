import math
x1, y1 = input().split()
x2, y2 = input().split()
x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

a = x2 - x1
b = y2 - y1
DISTANCIA = math.sqrt(pow(a,2) + pow(b,2))

print('%.4f'%DISTANCIA)