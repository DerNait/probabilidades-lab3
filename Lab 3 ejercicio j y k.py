import numpy as np
#ejercio J
def F_X2(x):
    if x < 8:
        return 0
    elif x <= 10:
        return (x - 8) / 2
    else:
        return 1
#ejercio k
def F_X3(x):
    if x < 1:
        return 0
    elif x < 8:
        return (3/4) * (np.floor(x) / 8)
    elif x <= 10:
        return (3/4) + (1/4) * (x - 8) / 2
    else:
        return 1

# Resolver ejercicios j y k
F_X2_result = F_X2(9)
F_X3_result = F_X3(9)

print(f"F_X2(9) = {F_X2_result}")
print(f"F_X3(9) = {F_X3_result}")
