import time
from copy import copy, deepcopy


def getLive(grid, i, j):
    if i<0 or j<0 or i>= len(grid) or j >=len(grid):
        return False
    else:
        return grid[i][j]
def life(grid):
    """
    Implement the game of Life.  Given an input matrix, the rules of Life are:
    1. Any live cell with fewer than two live neighbors dies, as if by under population.
    2. Any live cell with two or three live neighbors lives on to the next generation.
    3. Any live cell with more than three live neighbors dies, as if by overpopulation.
    4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
    :param grid: Input matrix: list of lists of boolean.  True means the cell is alive; False means it is dead.
        The input matrix will always be square. DO NOT MODIFY THE INPUT MATRIX.
    :return: A new matrix after running the game of Life one round.
    """
    if len(grid) == 1:
        return [[False]]
    results = deepcopy(grid)
    for i in range(len(grid)):
        for j in range(len(grid)):
            cell = grid[i][j]
            neighbors = 0
            for _i in range(3): # 0,1,2 => -1,0,1
                for _j in range(3):
                    if not (_i == 1 and _j == 1):
                        neighbors+= int(getLive(grid,i+_i-1,j+_j -1))
            #1
            if neighbors < 2 and cell:
                results[i][j] = False
            #2
            if cell and (neighbors == 2 or neighbors == 3):
                results[i][j] = True
            #3
            if cell and (neighbors > 3 ):
                results[i][j] = False
            #4
            if not cell and (neighbors == 3):
                results[i][j] = True

    return results


def input_grid(s):
    """
    Convert an input string into a Life matrix.  The input is a string representing a square matrix as a set of lines.
    On each line, the character 'o' represents a dead cell and the character 'O' represents a live cell.  For example:
    'ooo\n' +
    'oOo\n' +
    'ooO\n'
    Would represent:
    [[False, False, False],
     [False, True,  False],
     [False, False, True ]]
    :param s: Input string in the format described above.
    :return: List of lists of boolean representing the Life grid.
    :raises: Exception if the input is not valid (do not assume the input is valid).
    """
    mat = []
    temp_arr = []
    for _char in s:
        if _char != "o" and _char != "O" and _char != "\n":
            raise Exception("Invalid input")
        if _char == "o":
            temp_arr.append(False)
        if _char == "O":
            temp_arr.append(True)
        if _char == "\n":
            if len(mat) >0 and len(temp_arr)!= len(mat[0]):
                raise Exception("Not a matrix")
            mat.append(temp_arr)
            temp_arr = []
    if _char != "\n":
        raise Exception("Not finished with n")
    if len(temp_arr) > 0:
        mat.append(temp_arr)
    return mat


def output_grid(grid):
    """
    Opposite of input_grid - given a Life matrix, return a string representation of it in the same format as input_grid.
    :param grid: List of lists of boolean representing the Life grid.
    :return: String in the format described in input_grid.
    """
    string = ""
    for array in grid:
        for cell in array:
            if cell:
                string+= "O"
            else:
                string+="o"
        string+="\n"


    return string



def main():
    blinker1 = input_grid('ooooo\n'
                          'ooOoo\n'
                          'ooOoo\n'
                          'ooOoo\n'
                          'ooooo\n')
    #print(output_grid(blinker1))
    blinker2 = input_grid('ooooo\n'
                          'ooooo\n'
                          'oOOOo\n'
                          'ooooo\n'
                          'ooooo\n')
    # print(output_grid(blinker2))
    print (life(blinker1))
    # assert life(blinker1) == blinker2
    # assert life(blinker2) == blinker1

    grid = blinker1
    while True:
        print(output_grid(grid))
        grid = life(grid)
        time.sleep(1)

if __name__ == '__main__':
    main()