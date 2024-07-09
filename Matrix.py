##### MATRIX #####

# Matrix with values, used for pixels, signals
matrix = [[1, 2, 3], [4, 3, 4], [3, 4, 5]]

# Declaring Empty Matrix
matrix_dynamic = []

# Defining default matrix of size row * cols
rows = 3
cols = 3
default_matrix = [[0 for i in range(rows)] for i in range(cols)]
print(default_matrix)

### TRAVERSING MATRIX ###

## LOOPS
# Vertical Movement
for i in range(rows):
    # Horizontal Movement
    for j in range(cols):
        print(f"Element at {i}th row and {j}th column is: ", matrix[i][j])


## RECURSSION
def traverse(matrix, c_row, c_col):
    # Check if its end of matrix
    if c_row == rows - 1 and c_col == cols - 1:
        print(f"Recursively Element at {c_row}th row and {c_col}th column is: ", matrix[c_row][c_col])
        return
    if c_col < cols - 1:
        traverse(matrix, c_row, c_col + 1)
    elif c_row < rows - 1:
        traverse(matrix, c_row + 1, 0)


traverse(matrix, 0, 0)


### ROTATE - NESTED LOOPS ###
def rotatematrix(matrix):
    # Starting Row index
    top = 0

    # Ending Row Index
    bottom = len(matrix)

    # Start of Column
    left = 0

    # End of Column
    right = len(matrix[0])

    print(matrix[top+1][left])
    # Checking If we have reached end of row and cols
    while left < right and top < bottom:
        # Top Left Element Shift
        pass

rotatematrix(matrix)