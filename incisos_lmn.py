from sympy import Rational

# Probabilidades dadas
P_X1_eq_8 = Rational(1, 8)  # P(X1 = 8)
P_X3_eq_X1 = Rational(3, 4) # Probabilidad de que X3 = X1
P_X3_eq_X2 = Rational(1, 4) # Probabilidad de que X3 = X2

# Calcular P(X3 = 8)
P_X3_eq_8 = P_X3_eq_X1 * P_X1_eq_8

# Calcular P(X3 > 8)
P_X3_gt_8 = P_X3_eq_X2  # Porque X2 siempre está en (8,10)

# Calcular P(X3 < 8)
P_X1_lt_8 = Rational(7, 8) # P(X1 < 8), sumando probabilidades individuales
P_X3_lt_8 = P_X3_eq_X1 * P_X1_lt_8

# Imprimir resultados
print("P(X3 = 8) =", P_X3_eq_8)
print("P(X3 > 8) =", P_X3_gt_8)
print("P(X3 < 8) =", P_X3_lt_8)
