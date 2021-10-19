import copy
from itertools import chain, combinations



def parse(sudoku_string : str):
    """
    celem funkcji jest przyjecie wielolinijkowego sudoku w postaci 9 linijek postaci
    123000789,
    gdzie liczby oznaczaja konkretne wartosc a 0 wartosci puste
    zwracana jest wewnetrzna reprezentacja takiego sudoku jako tablica 2 wymiarowa
    """
    lines = sudoku_string.strip().replace(' ', '').split('\n')
    sudoku = []
    for line in lines:
        sudoku.append([char if char != '0' else None for char in line])
    return sudoku


def print_sudoku(sudoku):
    """
    powoduje wypisanie na ekranie obiektu sudoku w reprezentacji pakietu
    """
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] is not None:
                print(sudoku[i][j], sep='', end='')
            else:
                print(' ', sep='', end='')
            if j % 3 == 2:
                print("|", sep='', end='')
        print('',sep='',end='\n')
        if i % 3 == 2:
            print("---+---+---")


def print_hints(hints):
    """
    jak print_sudoku ale tu wypisany jest obiekt hintsow - opisu pol i dostepnych dla nich wartosci
    czyli takich ktore nie naurszaja porzadku wierszy, kolumn i kwadratow
    """
    for i in range(9):
        for j in range(9):
            print('[',sep='',end='')
            for k in range(1,10):
                if str(k) in hints[i][j]:
                    print(k,sep='',end='')
                else:
                    print(' ', sep='', end='')
            print(']',sep='', end='')
        print('',sep='',end='\n')


def check(sudoku_part):
    """
    fukcja do sprawdzania czy dana linia lub kwadrat nie posiadaja wiecej niz 1 takiej samej wartosci
    """
    is_okey = True
    for i in range(1,9):
        count = sum([element for element in sudoku_part if element == i])
        if count > 1:
            is_okey = False
            break
    return is_okey


def is_correct(sudoku):
    """
    funkcja sprawdza czy obiekt sudoku nie jest sprzeczny (te same elementy na wykluczajacych polach)
    """
    # sprawdz linie
    is_okey = True
    for i in range(9):
        is_okey = is_okey and check( sudoku[i] )
    # sprawdz piony
    for j in range(9):
        is_okey = is_okey and check([sudoku[i][j] for i in range(9)])
    # sprawdz kwadraty
    for ci in range(3):
        for cj in range(3):
            is_okey = is_okey and check([sudoku[i][j] for i in range(9) if i//3 == ci for j in range(9) if j//3 == cj])
    return is_okey


def is_solved(sudoku):
    """
    funkcja sprawdza czy sudoku nie jest juz wypelnione
    """
    is_okey = is_correct(sudoku)
    if not is_okey:
        return False
    list_of_Nones = [None for i in range(9) for j in range(9) if sudoku[i][j] is None]
    return len(list_of_Nones) == 0


def get_row(sudoku, row):
    """zwraca odpowiedni wiersz z sudoku"""
    return sudoku[row]


def get_col(sudoku, col):
    """zwraca odpowiednia kolumne z sudoku"""
    return [sudoku[x][col] for x in range(9)]


def get_sqr(sudoku, row, col):
    """zwraca kwadrat 3x3 zawierajacy pole (row,col)"""
    return [sudoku[x][y] for x in range(9) if x//3 == row//3 for y in range(9) if y//3 == col//3]


def generate_hints(sudoku):
    """
    Ta funkcja ma wygenerowac wszystkie dopuszczalne liczby dla pol pustych
    To znaczy ze w danym polu moze byc kazda z liczb 1..9 za wyjatkiem tej ktora juz wystepuje w rzedzie, kolumnie lub
    kwadracie. Sa to tzw hints lub olowek
    """
    hints = copy.deepcopy(sudoku)
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] is None:
                hint = {str(i) for i in range(1,10)}
                row = {element for element in get_row(sudoku, i) if element is not None}
                col = {element for element in get_col(sudoku, j) if element is not None }
                sqr = {element for element in get_sqr(sudoku, i, j) if element is not None}
                result =  hint.difference(row).difference(col).difference(sqr)
                hints[i][j] = result
            else:
                hints[i][j] = {sudoku[i][j]}
    return hints


def get_neighbours(sudoku, row, col):
    """Funkcja zwraca 3 listy sasiadow danego pola, czyli np. wiersz tego pola, ale bez samego pola"""
    row_neighbours = [sudoku[row][y] for y in range(9) if y != col]
    col_neighbours = [sudoku[x][col] for x in range(9) if x != row]
    sqr_neighbours = [sudoku[x][y] for x in range(9) if x//3 == row//3 for y in range(9) if y//3 == col//3 if x!=row or y!=col]
    return row_neighbours, col_neighbours, sqr_neighbours


def union(arr):
    """arr jest lista obiektow zbiorow (set). Funkcja zwraca ich laczna sume mnogosciowa"""
    return set().union(*arr)


def check_unique_values(hints):
    """
    Metoda przeszukuje hints aby sprawdzić czy nie wystepuja unikatowe wartosci w wierszach, kolumnach, kwadratach
    """
    for i in range(9):
        for j in range(9):
            neighbourhoods = get_neighbours(hints, i, j)
            for neighbourhood in neighbourhoods:
                all_unique = hints[i][j].difference(union(neighbourhood))
                if len(all_unique) == 1:
                    hints[i][j] = all_unique
                    break
    return hints




def powerset(iterable):
    """powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"""
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def search_cycles(hints):
    """
    Metoda poszukuje cykli w hintach np trzech pól {2,3,4}. Wtedy można poznać ktore elementy nie znajduja w
    pozostalych hintach.
    Warunkiem do sprawdzenia jest czy suma mnogosciowa n pol ma n roznych wartosci.
    Problemem jest jednak przejrzenie wszystkich wyborow elementow do cyklu ktorych jest 2^9 dla kazdego wiersza kolumny
    Drugim problemem jest usuniecie wykrytego cyklu z hintow
    """
    permutation_source = [x for x in range(9)]

    for row in range(9):
        for combination in powerset(permutation_source):
            if len(combination) == 0 or len(combination) == 1:
                continue
            # ignorujmy combinacje gdzie są 1elementowe hinty
            lengths = [ len(hints[row][x]) for x in combination]
            if 1 in lengths:
                continue
            # sprawdzamy warunek cyklu
            cycle_union = union([hints[row][x] for x in combination])
            if len(cycle_union) != len(combination):
                continue
            # usuwamy cykl z innych elementow wiersza
            for y in range(9):
                if y not in combination:
                    hints[row][y] = hints[row][y].difference(cycle_union)
    for column in range(9):
        for combination in powerset(permutation_source):
            if len(combination) == 0 or len(combination) == 1:
                continue
            # ignorujmy combinacje gdzie są 1elementowe hinty
            lengths = [ len(hints[x][column]) for x in combination]
            if 1 in lengths:
                continue
            # sprawdzamy warunek cyklu
            cycle_union = union([hints[x][column] for x in combination])
            if len(cycle_union) != len(combination):
                continue
            # usuwamy cykl z innych elementow wiersza
            for y in range(9):
                if y not in combination:
                    hints[y][column] = hints[y][column].difference(cycle_union)
        for row in range(0,9,3):
            for column in range(0,9,3):
                index_set =  [(r, c) for r in range(row, row + 3) for c in range(column, column + 3)]
                for combination in powerset(index_set):
                    if len(combination) == 0 or len(combination) == 1:
                        continue
                    # ignorujmy combinacje gdzie są 1elementowe hinty
                    lengths = [len(hints[x][y]) for x, y in combination]
                    if 1 in lengths:
                        continue
                    # sprawdzamy warunek cyklu
                    cycle_union = union([hints[x][y] for x, y in combination])
                    if len(cycle_union) != len(combination):
                        continue
                    # usuwamy cykl z innych elementow wiersza
                    for x,y in index_set:
                        if (x,y) not in combination:
                            hints[x][y] = hints[x][y].difference(cycle_union)
    return hints


def insert_values(hints):
    """Funkcja generuje stan rozwiazania sudoku na podstawie hints wstawiajac wartosci gdzie tylko jest to pewne"""
    hints = copy.deepcopy(hints)
    return [ [ hints[i][j].pop() if len(hints[i][j]) == 1 else None for j in range(9)] for i in range(9)]


def solve_sudoku(sudoku_string : str, max_steps = 50):
    """Funkcja poszukujaca rozwiazania sudoku przez okreslona liczbe iteracji.
    Na wejsciu przyjmuje sudoku w postaci tekstu, konwersja na obiekt sudoku nastepuje
    juz we wnetrzu kodu"""
    # konwersja na wewnetrzny typ sudoku
    sudoku = parse(sudoku_string)
    step = 0
    while not is_solved(sudoku):
        step += 1
        ## generujemy podpowiedzi
        ## na ich podstawie okreslamy liczby do wstawienia w tej iteracji
        ## i wstawiamy wartości do sudoku
        hints = generate_hints(sudoku)
        ## na podstawie hintsow mozemy sprawdzic juz wiele wskazowek do wstawienia wartosci
        hints = search_cycles(hints)
        # cykle nalezy sprawdzic pierwsze - bo choc trudniejsze obliczeniowo, to dzieki nim moze uda sie wiecej
        # unikatow wstawic do tresci
        hints = check_unique_values(hints)
        ## wygenerowanie sudoku na podstawie hints
        sudoku = insert_values(hints)
        if not is_correct(sudoku):
            print('Error - filling is incorrect')
            return sudoku, hints
        if step >= max_steps:
            print('Error - max step limit exceeded')
            return sudoku, hints
    return sudoku, hints

