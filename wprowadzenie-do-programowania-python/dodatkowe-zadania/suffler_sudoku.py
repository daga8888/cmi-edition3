sudoku_str = """
180007950 
056302017
347009620 
000700000
000020005
031000290
004950000
293100506
008036709    
"""

def parse(sudoku_string : str):
    pass

def is_correct(sudoku):
    pass

def is_solved(sudoku):
    pass

def generate_hints(sudoku):
    pass

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