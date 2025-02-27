from sympy import symbols
from sympy.stats import Uniform, P

# Definir X2 como una variable uniforme continua en el intervalo (8,10)
X2 = Uniform("X2", 8, 10)

# En distribuciones continuas, la probabilidad de un punto específico es siempre 0
# porque la densidad de probabilidad representa áreas bajo la curva, y un solo punto no tiene área.
# Inciso f
prob_X2_equals_9 = 0

#Inciso g
# Calcular P(X2 > 9)
prob_X2_greater_9 = P(X2 > 9)

# Imprimir resultados
print("Inciso f: P(X2 = 9) =", prob_X2_equals_9)
print("Inciso g:P(X2 > 9) =", float(prob_X2_greater_9))