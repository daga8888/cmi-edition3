def pi_wallis(n):
    result = 1
    for i in range(1,n+1):
        result *= (2*i) * (2*i) / (2*i-1) / (2*i+1)
    return result * 2

for i in range(1,50):
    print(f'Przybliżenie {i} wynosi {pi_wallis(i)}')

