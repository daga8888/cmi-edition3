def pi_gregory_leibniz(n):
    result = 0
    for i in range(n):
        result += 1/(4*i+1)
        result -= 1/(4*i+3)
    return result * 4

for i in range(1,50):
    print(f'Przybliżenie {i} wynosi {pi_gregory_leibniz(i)}')

