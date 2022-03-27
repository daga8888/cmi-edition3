def sqrt2_iteration(n):
    a = 2
    for i in range(n):
          a = a/2 + 1/a
    return a

for i in range(1,10):
    print(f'Przybliżenie {i} wynosi {sqrt2_iteration(i)}')


