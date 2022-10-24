import numpy
from numpy import *
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
from numpy.polynomial import *
from sympy import *

#Ingresar los esfuerzos xx, yy, zz, xy
sigma_xx = 64*10**6
sigma_yy = 55*10**6
sigma_zz = 100*10**6
T_xy = 65*10**6
T_yz = 0
T_xz = 0

#Ingresar el esfuerzo de fluencia del material
sigma_yield = 131*10**6

#Hallar coeficientes
A = sigma_xx+sigma_yy+sigma_zz
B = sigma_xx*sigma_yy+sigma_yy*sigma_zz+sigma_xx*sigma_zz-T_xy**2
C = sigma_xx*sigma_yy*sigma_zz+2*T_xy*T_xz*T_yz-sigma_xx*T_yz**2-sigma_yy*T_xz**2-sigma_zz*T_xy**2
print('Coeficiente 1 {}'.format(A))
print('Coeficiente 2 {}'.format(B))
print('Coeficiente 3 {}'.format(C))

#Hallar las raices de la ecuación
var('x')
Sol = solve(1*x**3-A*x**2+B*x-C,x)
Raices = [Sol[0], float(Sol[1]), float(Sol[2])]
print('Las raices son: {}'.format(Raices))

#Organizar las raices de mayor a menor
Raices_org = []

while Raices:
    mayor = Raices[0]
    for i in Raices:
        if i > mayor:
            mayor = i
    Raices_org.append(mayor)
    Raices.remove(mayor)

print('Sigma 1 {}'.format(Raices_org[0]))
print('Sigma 2 {}'.format(Raices_org[1]))
print('Sigma 3 {}'.format(Raices_org[2]))

#Se halla el esfuerzo promedio
sigma_prom = (max(Raices_org)+min(Raices_org))/2
print('Esfuerzo promedio = {}'.format(sigma_prom))

#Hallar los esfuerzos cortantes
T_12 = (Raices_org[0]-Raices_org[1])/2
T_23 = (Raices_org[1]-Raices_org[2])/2
T_13 = (Raices_org[0]-Raices_org[2])/2

print('Cortante 1 a 2 = {}'.format(T_12))
print('Cortante 2 a 3 = {}'.format(T_23))
print('Cortante 1 a 3 = {}'.format(T_13))

#Hallar el cortante máximo
T_max = (Raices_org[0]-Raices_org[2])/2
print('Cortante máximo = {}'.format(T_max))

#Hallar el cortante máximo absoluto
if Raices_org[2] > 0:
    T_max_abs = Raices_org[0]/2
    print('Cortante máximo absoluto = {}'.format(T_max_abs))
else:
    T_max_abs = (Raices_org[0]-Raices_org[2])/2
    print('Cortante máximo absoluto = {}'.format(T_max_abs))

#Hallar el ángulo
theta = 1/2*numpy.arctan(abs(T_xy/T_max))
print(theta)

#Circulo de Mohr

#Primer círculo
C1 = (Raices_org[0]+Raices_org[2])/2
r1 = T_13
print('Centro 1 = {}'.format(C1))
print('Radio 1 = {}'.format(r1))

#Segundo círculo
C2 = (Raices_org[0]+Raices_org[1])/2
r2 = T_12
print('Centro 2 = {}'.format(C2))
print('Radio 2 = {}'.format(r2))

#Tercer círculo
C3 = (Raices_org[1]+Raices_org[2])/2
r3 = T_23
print('Centro 3 = {}'.format(C3))
print('Radio 3 = {}'.format(r3))

#Datos para graficar el cículo de morh
Angulo = arange(0,361,1)
Angulo_rad = radians(Angulo)

def sigma(Centro, radio, angulo):
    # Crear matriz de sigma
    Long = len(angulo)
    Sigma = numpy.zeros(Long)
    for i in range(Long):
        Sigma[i] = Centro+radio*cos(2*angulo[i])
    #Crear matriz de Tau
    Tau = numpy.zeros(Long)
    for i in range(Long):
        Tau[i] = -radio*sin(2*angulo[i])
    return Sigma, Tau

#Sigma y Tau
Sigma1, Tau1 = sigma(C1, r1, Angulo_rad)
Sigma2, Tau2 = sigma(C2, r2, Angulo_rad)
Sigma3, Tau3 = sigma(C3, r3, Angulo_rad)

#Graficar el circulo de mohr
fig, Mohr = subplots()
Mohr.plot(Sigma1,Tau1)
Mohr.plot(Sigma2,Tau2)
Mohr.plot(Sigma3,Tau3)
plt.show()