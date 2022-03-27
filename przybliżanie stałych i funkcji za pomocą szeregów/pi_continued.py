def pi_continued_fraction(n):
    tmp = 6
    for i in reversed(range(1,n)):
        tmp = 6 + (2*i+1)**2 / tmp
    return 3+1/tmp

for i in range(1,40):
    print(f'Przybliżenie {i} wynosi {pi_continued_fraction(i)}')