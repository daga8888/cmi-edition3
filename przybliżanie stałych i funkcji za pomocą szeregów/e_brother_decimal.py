from decimal import *
getcontext().prec = 50

def e_brother_formula_decimal(n):
    sum = Decimal(1)
    temp_factorial = Decimal(1)
    for i in range(1,n):
        temp_factorial *= Decimal(2*i)
        temp_factorial *= Decimal(2*i+1)
        sum += Decimal(i+1) / temp_factorial
    return Decimal(2)*sum

for i in range(1,21):
    print(f'Przybliżenie {i} wynosi {e_brother_formula_decimal(i)}')