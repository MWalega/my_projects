solved_sudoku = [
                 [4,8,9,2,6,3,1,5,7],
                 [1,3,6,5,7,8,2,9,4],
                 [5,7,2,4,9,1,6,8,3],
                 [8,1,9,3,4,2,7,6,5],
                 [6,5,3,8,1,7,9,4,2],
                 [2,4,7,6,5,9,8,3,1],
                 [7,6,1,9,3,5,4,2,8],
                 [9,8,5,1,2,4,3,7,6],
                 [3,2,4,7,8,6,5,1,9]
                ]

def small_square_checker(sudoku, s_s, i) -> bool:
    small_square = set()
    for row in range(s_s[i][0][0], s_s[i][0][1]):
        for col in range(s_s[i][1][0], s_s[i][1][1]):
            small_square.add(sudoku[row][col])
    if len(small_square) == 9:
        return True
    return False

def full_rows_checked(sudoku) -> bool:
    full_row = set()
    for row in range(9):
        for col in range(9):
            full_row.add(sudoku[row][col])
        if len(full_row) != 9:
            return False
    return True

def full_cols_checked(sudoku) -> bool:
    full_col = set()
    for col in range(9):
        for row in range(9):
            full_col.add(sudoku[col][row])
        if len(full_col) != 9:
            return False
    return True

def row_and_col_checker(sudoku):
    if full_rows_checked(sudoku) and full_cols_checked(sudoku):
        return True
    return False

def sudoku_checker(sudoku) -> bool:
    checks = 0
    s_s = [[(0,3),(0,3)],
           [(0,3),(3,6)],
           [(0,3),(6,9)],
           [(3,6),(0,3)],
           [(3,6),(3,6)],
           [(3,6),(6,9)],
           [(6,9),(0,3)],
           [(6,9),(3,6)],
           [(6,9),(6,9)],
          ]
    
    # checking big square rows and cols
    if row_and_col_checker(sudoku):
        checks += 1

    # checking small squares
    for i in range(9):
        if small_square_checker(sudoku[s_s[i][0][0]:s_s[i][0][1]][s_s[i][1][0]:s_s[i][1][1]], s_s, i):
            checks += 1

    if checks == 10:
        return True
    return False
    
print(sudoku_checker(solved_sudoku))
