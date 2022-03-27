def e_continued_fraction(n):
    tmp = n
    for i in reversed(range(1,n)):
        tmp = i + i / tmp
    return 2+1/tmp

for i in range(1,21):
    print(f'Przybliżenie {i} wynosi {e_continued_fraction(i)}')