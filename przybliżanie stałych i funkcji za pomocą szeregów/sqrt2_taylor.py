def sqrt2_taylor_euler(n):
    result = 0.5
    k2p1 = 1
    two_power = 2
    kp2 = 1
    for i in range(1,n):
        k2p1 *= (2*i) * (2*i+1)
        kp2 *= i*i
        two_power *= 8
        result += k2p1/kp2/two_power
    return result

for i in range(1,25):
    print(f'Przybliżenie {i} wynosi {sqrt2_taylor_euler(i)}')

