def e_ciagiem(n):
    return (1.0+1.0/n)**n

for i in range(1,40):
    print(f'Przybliżenie {i} wynosi {e_ciagiem(i)}')