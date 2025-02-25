from sympy import Eq
from sympy.stats import FiniteRV, P, density, cdf, ContinuousRV

X1 = FiniteRV('X1', {1:1/8,2:1/8,3:1/8,4:1/8,5:1/8,6:1/8,7:1/8,8:1/8})

# a)
print("a) P(X1 = 2):", P(Eq(X1, 2)))

# b) 
print("b) P(X1 > 2):", P(X1 > 2))

# c) 
print("c) P(X1 < 2):", P(X1 < 2))