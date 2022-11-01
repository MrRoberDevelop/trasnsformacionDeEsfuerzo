import numpy as np
from numpy import *
import matplotlib.pyplot as plt
from matplotlib.pyplot import *

#Ingresar el esfuerzo de fluencia del material
sigma_yield = 500

#Ingresar los esfuerzos originales
# sigma_x = float(input('Ingresar σ_x: '))
# sigma_y = float(input('Ingresar σ_y: '))
# Tau_xy = float(input('Ingrese τ_xy: '))
sigma_x = 40
sigma_y = 50
Tau_xy = 80

#Ingresar ángulo de rotación
# theta = np.radians(float(input('Ingrese el ángulo de rotación: ')))
theta = np.radians(4)

#Esfuerzos transformados
sigma_xprima = (sigma_x+sigma_y)/2+(sigma_x-sigma_y)/2*cos(2*theta)-Tau_xy*sin(2*theta)
sigma_yprima= (sigma_x+sigma_y)/2-(sigma_x-sigma_y)/2*cos(2*theta)+Tau_xy*sin(2*theta)
Tau_xyprima= (sigma_x-sigma_y)/2*sin(2*theta)+Tau_xy*cos(2*theta)
print("σ_x' para un ángulo de", np.degrees(theta), '= {}'.format(sigma_xprima))
print("σ_y' para un ángulo de", np.degrees(theta), '= {}'.format(sigma_yprima))
print("τ_xy' para un ángulo de", np.degrees(theta), '= {}'.format(Tau_xyprima))

#Realizar círculo de mohr
Angulo = arange(0,181,1)
Angulo_rad = radians(Angulo)
sigma_xp = (sigma_x+sigma_y)/2+(sigma_x-sigma_y)/2*cos(2*Angulo_rad)-Tau_xy*sin(2*Angulo_rad)
Tau_xyp= (sigma_x-sigma_y)/2*sin(2*Angulo_rad)+Tau_xy*cos(2*Angulo_rad)

#Ángulo para esfuerzo principal
theta_p = 1/2*np.arctan(-(2*Tau_xy)/(sigma_x-sigma_y))
print('El ángulo para los esfuerzos máximos = {}'.format(degrees(theta_p)))

#Esfuerzos principales
sigma_xprin = (sigma_x+sigma_y)/2+(sigma_x-sigma_y)/2*cos(2*theta_p)-Tau_xy*sin(2*theta_p)
sigma_yprin= (sigma_x+sigma_y)/2-(sigma_x-sigma_y)/2*cos(2*theta_p)+Tau_xy*sin(2*theta_p)
Tau_xyprin= (sigma_x-sigma_y)/2*sin(2*theta_p)+Tau_xy*cos(2*theta_p)
print('σ_x principal = {}'.format(sigma_xprin))
print('σ_y principal = {}'.format(sigma_yprin))
print('τ_xy principal = {}'.format(round(Tau_xyprin,2)))

#Gráfica circulo de Mohr
fig, Mohr = subplots(figsize=(10,9))
Mohr.plot(sigma_xp,Tau_xyp, label='Cículo de Mohr')
Mohr.plot([sigma_x,sigma_y],[Tau_xy,-Tau_xy], label='Esfuerzos originales')
Mohr.plot([sigma_xprima,sigma_yprima],[Tau_xyprima,-Tau_xyprima], label='Esfuerzos transformados')
Mohr.plot([sigma_xprin,sigma_yprin],[Tau_xyprin,-Tau_xyprin], label='Esfuerzos principales')
plt.legend(loc='upper right', fontsize='x-small')
plt.title('Cículo de Mohr')
plt.show()

#Gráfica esfuerzos vs ángulo
fig, SvsA = subplots()
SvsA.plot(Angulo, sigma_xp, label="σ_x' vs θ")
SvsA.plot(Angulo,Tau_xyp, label="T_xy' vs θ")
plt.legend(loc='lower left', fontsize='x-small')
plt.title('Esfuerzos vs Ángulo')
plt.show()

#Criterio de falla según Tresca
FS_T = sigma_yield/abs(sigma_xprin-sigma_yprin)
print('Factor de seguridad Tresca = {} '.format(FS_T))
x_tresca = [-sigma_yield,0,sigma_yield,sigma_yield,0,-sigma_yield,-sigma_yield]
y_tresca = [0,sigma_yield,sigma_yield,0,-sigma_yield,-sigma_yield,0]

#Criterio de falla según Von Mises
FS_VM = sigma_yield/np.sqrt(sigma_xprin**2+sigma_yprin**2-sigma_xprin*sigma_yprin)
print('Factor de seguridad Von Mises = {} '.format(FS_VM))

#Datos para gráfica Von Mises
Angulo = arange(0,361,1)
Angulo_rad = radians(Angulo)
a = np.sqrt(2)*sigma_yield
b = np.sqrt(2)/np.sqrt(3)*sigma_yield
x_prima = a*cos(Angulo_rad)
y_prima = b*sin(Angulo_rad)
x = x_prima*cos(radians(45))-y_prima*sin(radians(45))
y = x_prima*sin(radians(45))+y_prima*cos(radians(45))

#Gráficas criterios de falla
fig, Criterios = subplots()
Criterios.plot(x_tresca,y_tresca, label='Tresca')
Criterios.plot(x,y, label='Von Mises')
Criterios.plot(sigma_xprin,sigma_yprin, marker='o', label='Esfuerzo original')
plt.legend(loc='lower right',fontsize='small')
plt.show()