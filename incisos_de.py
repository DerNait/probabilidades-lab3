import math

# Inciso d
def funcion_probabilidad_X1(j):
    if 1 <= j <= 8:
        return 1/8
    else:
        return 0

# Inciso e
def funcion_distribucion_X1(x):
    if x < 1:
        return 0.0
    elif 1 <= x <= 8:
        return math.floor(x) / 8
    else:
        return 1.0


# Prueba inciso d
print("Inciso d:")
print(f"P(X1=3) = {funcion_probabilidad_X1(3)}")
print(f"P(X1=9) = {funcion_probabilidad_X1(9)}")

# Prueba inciso e
print("\nInciso e:")
print(f"F_X1(0.5) = {funcion_distribucion_X1(0.5)}")
print(f"F_X1(3) = {funcion_distribucion_X1(3)}")
print(f"F_X1(5.7) = {funcion_distribucion_X1(5.7)}")
print(f"F_X1(10) = {funcion_distribucion_X1(10)}")