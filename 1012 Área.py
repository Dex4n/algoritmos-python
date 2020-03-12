pi=3.14159
line1 = input().split()
A = float(line1[0])
B = float(line1[1])
C = float(line1[2])

triangulo = (A * C) / 2
circulo = pi * C * C
trapezio = ((A + B) * C) / 2
quadrado = B * B
retangulo = A * B

print('TRIANGULO: %.3f'%(triangulo))
print('CIRCULO: %.3f'%(circulo))
print('TRAPEZIO: %.3f'%(trapezio))
print('QUADRADO: %.3f'%(quadrado))
print('RETANGULO: %.3f'%(retangulo))






