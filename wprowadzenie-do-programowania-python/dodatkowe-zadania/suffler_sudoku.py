sudoku_str = """180007950
056302017
347009620 
000700000
000020005
031000290
004950000
293100506
008036709"""

def parse(sudoku_string : str):
    lines = sudoku_string.replace(' ', '').split('\n')
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
            is_okey = is_okey and check([sudoku[i][j] for i in range(3) if i//3==ci for j in range(9) if j//3==cj])
    return is_okey

def is_solved(sudoku):
    is_okey = is_correct(sudoku)
    if not is_okey:
        return False
    list_of_Nones = [None for i in range(9) for j in range(9) if sudoku[i][j] is None]
    return len(list_of_Nones) == 0

import copy

def generate_hints(sudoku):
    hints = copy.deepcopy(sudoku)
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] is None:
                hint = {str(i) for i in range(1,10)}
                row = {element for element in sudoku[i] if element is not None}
                col = {element for element in [sudoku[x][j] for x in range(9)] if element is not None }
                sqr = {element for element in [sudoku[x][y] for x in range(3) if x//3 == i//3 for y in range(9) if y//3 == j//3] if element is not None}
                result =  hint.difference(row).difference(col).difference(sqr)
                hints[i][j] = result
    return hints

def insert_values(hints):
    return [ [ hints[i][j] if isinstance(hints[i][j],str) else hints[i][j].pop() if len(hints[i][j]) == 1 else None for j in range(9)] for i in range(9)]
    pass

def solve_sudoku(sudoku_string : str, max_steps = 20):
    # konwersja na wewnetrzny typ sudoku
    sudoku = parse(sudoku_string)
    step = 0
    while not is_solved(sudoku):
        step += 1
        ## generujemy podpowiedzi
        ## na ich podstawie okreslamy liczby do wstawienia w tej iteracji
        ## i wstawiamy wartości do sudoku
        hints = generate_hints(sudoku)
        sudoku = insert_values(hints)
        if not is_correct(sudoku):
            return sudoku, hints
        if step >= max_steps:
            return sudoku, hints
    return sudoku, hints

sudoku, hints = solve_sudoku(sudoku_str)
print_sudoku(sudoku)
print_hints(hints)