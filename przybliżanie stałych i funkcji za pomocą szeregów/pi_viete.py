import math

def pi_viete(n):
    root = 0
    result = 1
    for i in range(n):
        root = math.sqrt(2+root)
        result *= root
        result /= 2
    return 2/result

for i in range(1,30):
    print(f'Przybliżenie {i} wynosi {pi_viete(i)}')


