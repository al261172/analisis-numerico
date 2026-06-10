
# matricula: 261172
# nombre: "Marcelo Murillo Estrada"

import numpy as np

# Area de un circulo - - - - - - - - - - - - - - - - - - - - - - - -

r = 7
A = (np.pi) * (r**2)

print(f"El area de un círculo con radio {r:.3f} es {A:.3f}")

#Area de un traingulo - - - - - - - - - - - - - - - - - - - - - - - -
a_tri = 6
b_tri = 8
c_tri = 9
s_tri = (a_tri + b_tri + c_tri) / 2
A_tri = (s_tri * ((s_tri - a_tri)*(s_tri - b_tri)*(s_tri - c_tri)))**(0.5)

print(f"El area de un triangulo es {A_tri:.3f}")

#Volumen esfera

r_esf = 4
V_esf = (4/3)*np.pi*(r**3)

print(f"El vol de una esfera con radio {r_esf} es: {V_esf}")

# Distancia entre dos puntos - - - - - - - - - - - - - - - - - - - - -

x_1 = 2
y_1 = 3
x_2 = 10
y_2 = 9

d = ((x_2 - x_1)**2 + (y_2 - y_1)**2)**(0.5)

print(f"La dist entre los puntos ({x_1},{y_1}) y ({x_2},{y_2}) = {d:.3f}")

#pH de una solucion - - - - - - - - - - - - - - - - - - - - - - - - - -

hyd = 3.2 * 10**(-5)
pH = - np.log10(hyd)

print(f"El pH de la solucion = {pH:.3f}")

#Decaimiento radiactivo - - - - - - - - - - - - - - - - - - - - - - - - - -

n_0 = 500
k = 0.03
t = 20
N_rad = n_0 * np.exp(-k * t)

print(f"El decaimiento radiactivo = {N_rad:.3f}")

#Altura de un edificio  - - - - - - - - - - - - - - - - - - - - - - - - -

d_edi = 50
theta = 32 #deg
h = d_edi * np.tan(theta*(np.pi/180))

print(f"La altura de un edificio es {h:.3f}")

#operacion con matricula  - - - - - - - - - - - - - - - - - - - - - - - - -

matricula = "261172"
q = [int(c) for c in matricula]
matricula_num = int(matricula)

print(matricula)
print(q)
print(matricula_num)
print(type(matricula_num))

#Suma  - - - - - - - - - - - - - - - - - - - - - - - - -
sum = 0
for i in q:
    sum = sum + i
print(f"Suma de los digitos {q} es: {sum:.3f}")

#resta  - - - - - - - - - - - - - - - - - - - - - - - - -
res = q[0] - q[5]
print(f"Resta: {q[0]} - {q[5]} = {res:.3f}")

#multiplicacion  - - - - - - - - - - - - - - - - - - - - - - - - -
mul = q[1] * q[4]
print(f"Multiplicacion: {q[1]} * {q[4]} = {mul:.3f}")

#Division  - - - - - - - - - - - - - - - - - - - - - - - - -
div = q[2] / (q[3] + 1)
print(f"Division: {q[2]} / ({q[3]} + 1) = {div:.3f}")

#potencia  - - - - - - - - - - - - - - - - - - - - - - - - -
pot = q[1] ** 3
print(f"Potencia: {q[1]} ** 3 = {pot:.3f}")

#trigonometrica  - - - - - - - - - - - - - - - - - - - - - - - - -
trg = np.sin(np.radians(q[0]*10+q[1]))
print(f"Trigonometrica sin({q[0]} * 10 + {q[1]}) = {trg:.3f}")

#inversa, logaritmo y exponencial  - - - - - - - - - - - - - - -
inv = np.arctan(q[2] / (q[4] + 1))
print(f"Inversa arctan({q[2]} / ({q[4]} + 1))= {inv:.3f}")

log = np.log10(matricula_num)
print(f"Logaritmo: log10({matricula_num}) = {log:.3f}")

exp = np.exp(q[5] / 2)
print(f"Exponencial: e^({q[5]} / 2) = {exp:.3f}")


#Reto extra - - - - - - - - - - - - - - - - - - - - - - - - -

resultado = ((3.3)**2 - 5)**(1/2)

print(f"resultado de sqr(x^2 - 5), x = 3.3 es --> {resultado:.3f}")