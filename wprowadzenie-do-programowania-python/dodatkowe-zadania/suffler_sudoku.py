sudoku_str = """
005000048
020000001
800410000
600702030
004900000
200000009
000001060
000350704
080000000
"""


def parse(sudoku_string : str):
    lines = sudoku_string.strip().replace(' ', '').split('\n')
    sudoku = []
    for line in lines:
        sudoku.append([char if char != '0' else None for char in line])
    return sudoku


def print_sudoku(sudoku):
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
    is_okey = True
    for i in range(1,9):
        count = sum([element for element in sudoku_part if element == i])
        if count > 1:
            is_okey = False
            break
    return is_okey


def is_correct(sudoku):
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
    is_okey = is_correct(sudoku)
    if not is_okey:
        return False
    list_of_Nones = [None for i in range(9) for j in range(9) if sudoku[i][j] is None]
    return len(list_of_Nones) == 0

import copy

# Ta funkcja ma wygenerowac wszystkie dopuszczalne liczby dla pol pustych
# To znaczy ze w danym polu moze byc kazda z liczb 1..9 za wyjatkiem tej ktora juz wystepuje w rzedzie, kolumnie lub
# kwadracie


def get_row(sudoku, row):
    return sudoku[row]


def get_col(sudoku, col):
    return [sudoku[x][col] for x in range(9)]


def get_sqr(sudoku, row, col):
    return [sudoku[x][y] for x in range(9) if x//3 == row//3 for y in range(9) if y//3 == col//3]


def generate_hints(sudoku):
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
    row_neighbours = [sudoku[row][y] for y in range(9) if y != col]
    col_neighbours = [sudoku[x][col] for x in range(9) if x != row]
    sqr_neighbours = [sudoku[x][y] for x in range(9) if x//3 == row//3 for y in range(9) if y//3 == col//3 if x!=row or y!=col]
    return row_neighbours, col_neighbours, sqr_neighbours


def union(arr):
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


def insert_values(hints):
    hints = copy.deepcopy(hints)
    return [ [ hints[i][j].pop() if len(hints[i][j]) == 1 else None for j in range(9)] for i in range(9)]


def solve_sudoku(sudoku_string : str, max_steps = 10):
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
        print(f'Hinty wygenerowane poczatkowo')
        print_hints(hints)
        print(f'Hinty uzyskane z unikalnych')
        hints = check_unique_values(hints)
        print_hints(hints)
        ## wygenerowanie sudoku na podstawie hints
        sudoku = insert_values(hints)
        if not is_correct(sudoku):
            print('Error - filling is incorrect')
            return sudoku, hints
        if step >= max_steps:
            print('Error - max step limit exceeded')
            return sudoku, hints
    return sudoku, hints


sudoku, hints = solve_sudoku(sudoku_str)
print_sudoku(sudoku)
print_hints(hints)
print('Good bye')