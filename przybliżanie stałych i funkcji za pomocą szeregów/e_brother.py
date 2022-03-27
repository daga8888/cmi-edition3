def e_brother_formula(n):
    sum = 1
    temp_factorial = 1
    for i in range(1,n):
        temp_factorial *= 2*i
        temp_factorial *= (2*i+1)
        sum += (i+1) / temp_factorial
    return 2*sum

for i in range(1,21):
    print(f'Przybliżenie {i} wynosi {e_brother_formula(i)}')