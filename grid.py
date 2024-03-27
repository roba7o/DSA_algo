grid = [
        [3, 9, 0,   0, 5, 0,   0, 0, 0],
        [0, 0, 0,   2, 0, 0,   0, 0, 5],
        [0, 0, 0,   7, 1, 9,   0, 8, 0],

        [0, 5, 0,   0, 6, 8,   0, 0, 0],
        [2, 0, 6,   0, 0, 3,   0, 0, 0],
        [0, 0, 0,   0, 0, 0,   0, 0, 4],

        [5, 0, 0,   0, 0, 0,   0, 0, 0],
        [6, 7, 0,   1, 0, 5,   0, 4, 0],
        [1, 0, 9,   0, 0, 0,   2, 0, 0]
    ]

# Replace 0 with -1 in the grid
new_grid = [[-1 if val == 0 else val for val in row] for row in grid]

# Write the modified grid to a new Python file
with open('modified_grid.py', 'w') as file:
    file.write("modified_grid = [\n")
    for row in new_grid:
        file.write(f"    {row},\n")
    file.write("]\n")

print("New grid written to modified_grid.py")