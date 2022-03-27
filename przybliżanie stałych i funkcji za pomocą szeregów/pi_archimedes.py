import math

def pi_ciagowo(n):
    return 0.5 * n * math.sin(2*math.pi / n)

for i in range(1,40):
    print(f'Przybliżenie {i} wynosi {pi_ciagowo(i)}')

