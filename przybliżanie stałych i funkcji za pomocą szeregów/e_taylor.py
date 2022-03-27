
def e_taylor_series(n):
    sum = 0
    temp_factorial =1;
    for i in range(1,n):
        temp_factorial *= i
        sum += 1/temp_factorial
    return sum+1

for i in range(1,21):
    print(f'Przybliżenie {i} wynosi {e_taylor_series(i)}')
