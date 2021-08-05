sudoku = [
    [0,0,1,2,0,7,0,9,0],
    [0,9,0,0,0,8,0,4,0],
    [0,0,0,0,9,0,3,0,0],
    [0,0,9,1,0,0,4,0,0],
    [0,0,3,6,0,2,7,0,0],
    [0,0,8,0,0,4,2,0,0],
    [0,0,4,0,3,0,0,0,0],
    [0,2,0,4,0,0,0,6,0],
    [0,6,0,8,0,9,1,0,0]
]

def solve(su):
    find = find_empty(su)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(su, i, (row, col)):
            su[row][col] = i

            if solve(su):
                return True

            su[row][col] = 0

    return False


def valid(su, number, position):
    # Check row
    for i in range(len(su[0])):
        if su[position[0]][i] == number and position[1] != i:
            return False

    # Check column
    for i in range(len(su)):
        if su[i][position[1]] == number and position[0] != i:
            return False

    # Check box
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if su[i][j] == number and (i,j) != position:
                return False

    return True


def print_sudoku(su):
    for i in range(len(su)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(su[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(su[i][j])
            else:
                print(str(su[i][j]) + " ", end="")


def find_empty(su):
    for i in range(len(su)):
        for j in range(len(su[0])):
            if su[i][j] == 0:
                return (i, j)  # row, col

    return None

print_sudoku(sudoku)
solve(sudoku)
print("_______________________")
print("                       ")
print_sudoku(sudoku)