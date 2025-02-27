import numpy as np
import matplotlib.pyplot as plt

# Definir la función de densidad de probabilidad (PDF) de X2
def f_X2(x):
    return 1/2 if 8 < x < 10 else 0

# Calcular P(X2 > 9)
p_X2_greater_9 = (10 - 9) / (10 - 8)
print(f"P(X2 > 9) = {p_X2_greater_9}")

# Graficar la PDF de X2
x_values = np.linspace(7, 11, 1000)
y_values = [f_X2(x) for x in x_values]

plt.plot(x_values, y_values, label='$f_{X_2}(x)$', color='blue')
plt.xlabel('$x$')
plt.ylabel('$f_{X_2}(x)$')
plt.title('Densidad de Probabilidad de $X_2$')
plt.axhline(y=0, color='black', linewidth=0.5)
plt.axvline(x=8, color='red', linestyle='dashed', label='$x=8$')
plt.axvline(x=10, color='red', linestyle='dashed', label='$x=10$')
plt.legend()
plt.show()
