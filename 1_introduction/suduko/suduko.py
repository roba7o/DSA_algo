import numpy as np

def find_next_empty(puzzle):
    #We will linearly search by row then column (row index).
    #it will return first empty (represented by -1) as row, col and None, None if there is no empty (solved)

    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r,c
            
    return None,None

def is_valid(puzzle, guess, row, col):
    #returns true if valid (doesnt exist in row, col and 3x3 matrix)

    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
    #each row belongs to a set of 3 rows
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start,row_start+3):
        for c in range(col_start,col_start+3):
            if puzzle[r][c] == guess:
                return False
            
    #passes tests
    return True
    


def solve_suduko(puzzle):
    """
    solve sudoku using backtracking
    puzzle is a list of lists -> each inner list is a row
    return whether solution exists
    mutates puzzle to be solution as strings are mutable
    """

    #Step 1 - Choose somewhere on the puzzle to make a guess (any open space)
    row,col = find_next_empty(puzzle)
    #only need to check oen of them
    if row is None:
        return True
    
    #Step 2: if there is a space. Make guess 1-9
    for guess in range(1,10):
        #step 3 - check if valid guess
        if is_valid(puzzle, guess, row, col):
            #step 3.1 - if valid then place guess (mutating array)
            puzzle[row][col] = guess
            #step 4 - now recurse
            if solve_suduko(puzzle):
                return True
            
        #step 5 - if not valid or guess doesnt solve puzze
        #need to backtrack
        puzzle[row][col] = -1

        """ 
        It will parse through every single position. As when 1-9 is exhausted it resets the parent guess and then it goes to next range value. if thats exhausted it keeps going back
        -> this is how it backtracks through multiple levels!!
        every value is searched. unless it reaches the correct value of range before then -> given its solvable.
        """
            
    #step 6 -> no solution as all has been tried
    return False

if __name__ == "__main__":
    grid = [
    [3, 9, -1, -1, 5, -1, -1, -1, -1],
    [-1, -1, -1, 2, -1, -1, -1, -1, 5],
    [-1, -1, -1, 7, 1, 9, -1, 8, -1],
    [-1, 5, -1, -1, 6, 8, -1, -1, -1],
    [2, -1, 6, -1, -1, 3, -1, -1, -1]
    [-1, -1, -1, -1, -1, -1, -1, -1, 4],
    [5, -1, -1, -1, -1, -1, -1, -1, -1],
    [6, 7, -1, 1, -1, 5, -1, 4, -1],
    [1, -1, 9, -1, -1, -1, 2, -1, -1],
    ]

    print(np.matrix(grid))
    print("")

    solve_suduko(grid)
    print(np.matrix(grid))

