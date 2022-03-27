from decimal import *
getcontext().prec = 50

def e_taylor_series_decimal(n):
    sum = Decimal(0)
    temp_factorial = Decimal(1);
    for i in range(1,n):
        temp_factorial *= Decimal(i)
        sum += Decimal(1)/temp_factorial
    return sum+1

for i in range(1,21):
    print(f'Przybliżenie {i} wynosi {e_taylor_series_decimal(i)}')