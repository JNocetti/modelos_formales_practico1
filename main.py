import math

# Parámetros de la letra 
# M/M/1 FIFO/-/m=5
m = 5
lambda_total = 2
mu = 12
lambda_i = lambda_total / m # 0.4
psi = lambda_i / mu # 1/30

# Calcular p0
# Primero calculo la sumatoria
suma = sum([math.comb(m, n) * (psi ** n) for n in range(1, m + 1)])

# Calculo el inverso
p0 = 1 / (1 + suma) 

# a) Número medio de equipos rotos
n = m - (1 / psi) * (1 - p0)

# b) Tiempo medio de espera en la línea
t_f = (1 / mu) * ((m / (1 - p0)) - ((1 + psi) / psi))

# c) Probabilidad de que haya más de 2 equipos rotos
p1 = math.comb(m, 1) * psi * p0
p2 = math.comb(m, 2) * (psi ** 2) * p0
p_mas_2 = 1 - (p0 + p1 + p2)

# Resultados
print(f"a) Equipos rotos en promedio: {n:.4f}")
print(f"b) Tiempo medio de espera (días): {t_f*24:.4f}")
print(f"c) Probabilidad de n > 2: {p_mas_2:.4%}")


