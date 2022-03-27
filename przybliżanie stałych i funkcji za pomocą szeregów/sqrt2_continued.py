def sqrt2_continued_fraction(n):
    tmp = 2
    for i in reversed(range(1,n)):
        tmp = 2 + 1 / tmp
    return 1+1/tmp

for i in range(1,25):
    print(f'Przybliżenie {i} wynosi {sqrt2_continued_fraction(i)}')

