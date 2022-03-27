import math

def my_sin(x, n):
    result = x
    temp_x = x
    x_sqrt = x*x
    factor = 1
    for i in range(n):
        temp_x *= x_sqrt
        factor *= (4*i+3)*(4*i+2)
        result -= temp_x / factor
        temp_x *= x_sqrt
        factor *= (4*i+5)*(4*i+4)
        result += temp_x / factor
    return result

print(f'Przybliżenie sin(1) wynosi {math.sin(1)}')
for i in range(1,10):
    print(f'Przybliżenie sin(1) no {i} wynosi {my_sin(1,i)}')