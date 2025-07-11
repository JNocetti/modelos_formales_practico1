import numpy as np
from scipy.optimize import linprog

# Costos ($) por unidad de 30 g de cereal
c = np.array([30, 36])

# Restricciones convertidas a forma ≤ 
A_ub = -np.array([
    [0.10, 0.25],  # Tiamina ≥ 1 mg
    [1.00, 0.25],  # Niacina ≥ 5 mg
    [110 , 120 ]   # Calorías ≥ 400 kcal
])
b_ub = -np.array([1, 5, 400])

# Límites de las variables (x ≥ 0, y ≥ 0)
bounds = [(0, None), (0, None)]

# Resolución del problema
result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')

# Salida de resultados
x_opt, y_opt = result.x    
print(f"T (30 g): {x_opt:.4f} ({x_opt*30:.0f} g)")
print(f"D (30 g): {y_opt:.4f} ({y_opt*30:.0f} g)")
print(f"Costo mínimo: ${result.fun:.2f}")

