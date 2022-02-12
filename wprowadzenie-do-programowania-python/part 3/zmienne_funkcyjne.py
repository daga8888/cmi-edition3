
#
# def f(x):
#     return x + 1
#
# g = f
#
# print(g(2))

## Mozna funkcje (jako zmienna) przekazac przez parametr do wnetrza innej funkcji

def podwajanie(x):
    return 2*x

print(podwajanie(8))

## chciałbym mieć funkcje ktora bierze jako parametr tablice liczb oraz
## pewien sposob jej modyfikowania i zmienia te tablice odpowiednio

def zmien_tablice(funkcja, tablica):
    wynik = []
    for element in tablica:
        wynik.append(funkcja(element))
    return wynik

print(zmien_tablice(podwajanie, [1,4,7,14]))
