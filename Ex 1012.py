A,B,C = map(float, input().split())

#area triangulo
AT = (A * C)/2

#area circulo
AC = 3.14159 * (C**2)

#area trapezio
ATRAP = ((A+B)*C)/2

#area quadrado
AQ = B * B

#area retangulo
AR = A * B

print('TRIANGULO: %.3f' %AT)

print('CIRCULO: %.3f' %AC)

print('TRAPEZIO: %.3f' %ATRAP)

print('QUADRADO: %.3f' %AQ)

print('RETANGULO: %.3f' %AR)





