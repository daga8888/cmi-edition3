from decimal import *
getcontext().prec = 50


def e_continued_fraction_decimal(n):
    tmp = Decimal(n)
    for i in reversed(range(1,n)):
        tmp = Decimal(i) + Decimal(i) / tmp
    return 2+1/tmp

for i in range(1,21):
    print(f'Przybliżenie {i} wynosi {e_continued_fraction_decimal(i)}')