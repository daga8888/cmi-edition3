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

def check(sudoku_part):
    #sudoku_part = flatten(sudoku_part)
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

def generate_hints(sudoku):

    pass



sudoku = parse(sudoku_str)
print(is_solved(sudoku))

def generate_inserts(hints):
    pass

def insert_values(sudoku, inserts):
    pass

def solve_sudoku(sudoku_string : str):
    # konwersja na wewnetrzny typ sudoku
    sudoku = parse(sudoku_string)

    while not is_solved(sudoku):
        ## generujemy podpowiedzi
        ## na ich podstawie okreslamy liczby do wstawienia w tej iteracji
        ## i wstawiamy wartości do sudoku
        hints = generate_hints(sudoku)
        inserts = generate_inserts(hints)
        sudoku = insert_values(sudoku, inserts)
        if not is_correct(sudoku):
            return "Err 1", sudoku
    return sudoku