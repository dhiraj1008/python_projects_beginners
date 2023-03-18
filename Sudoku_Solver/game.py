#by using backtracking algo and list
def find_next_empty(puzzle):
     for row in range(9):
         for col in range(9):
            if puzzle[row][col]==-1:
                return row,col
     return None,None

def is_validGuess(puzzle,row,col,guess):
    #row check
    row_list=puzzle[row]
    if guess in row_list:
        return False
    
    #column check
    col_list=[puzzle[i][col] for i in range(9)]
    if guess in col_list:
        return False

    #square check
    row_start=(row//3)*3 #(0//3)*3=0 ,(5//3)*3=3
    col_start=(col//3)*3

    for r in range(row_start,row_start+3):
        for c in range(col_start,col_start+3):
            if puzzle[r][c]==guess:
                return False

    return True


def solve_sudoku(puzzle):
    row,col=find_next_empty(puzzle)
    if row==None:#no square is empty then done are done we allowed valid input;
        return True

    for guess in range(1,10):
        if is_validGuess(puzzle,row,col,guess):
            puzzle[row][col]=guess

            if solve_sudoku(puzzle):
                return True
        
        #using backtracking :
        puzzle[row][col]=-1
    
    #if none of nuber we try work ,then puzzle is unsolvable..!
    return False

if __name__ == '__main__':
    puzzle=[ [3,9,-1,   -1,5,-1, -1,-1,-1],
             [-1,-1,-1,  2,-1,-1, -1,-1,5],
             [-1,-1,-1,  7,1,9,   -1,8,-1],

             [-1,5,-1,  -1,6,8,    -1,-1,-1],
             [2,-1,6,   -1,-1,3,   -1,-1,-1],
             [-1,-1,-1,  -1,-1,-1, -1,-1,4],
             
             [5,-1,-1, -1,-1,-1, -1,-1,-1],
             [6,7,-1,   1,-1,5,  -1,4,-1],
             [-1,-1,9,  -1,-1,-1,  2,-1,-1]
    ]

    print(solve_sudoku(puzzle))     
    print(puzzle)                               



"""
o/p->
True

[[3, 9, 1, 8, 5, 6, 4, 2, 7],
[8, 6, 7, 2, 3, 4, 9, 1, 5],
[4, 2, 5, 7, 1, 9, 6, 8, 3],
[7, 5, 4, 9, 6, 8, 1, 3, 2], 
[2, 1, 6, 4, 7, 3, 5, 9, 8],
[9, 3, 8, 5, 2, 1, 7, 6, 4],
[5, 4, 3, 6, 9, 2, 8, 7, 1],
[6, 7, 2, 1, 8, 5, 3, 4, 9],
[1, 8, 9, 3, 4, 7, 2, 5, 6]]
"""