def find_paths(path, row, col, rows, cols):
    if row == rows - 1 and col == cols - 1:
        print(path)
        return

    if row < rows - 1:
        find_paths(path + 'd', row + 1, col, rows, cols)

    if col < cols - 1:
        find_paths(path + 'r', row, col + 1, rows, cols)

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Possible paths:")
find_paths("", 0, 0, rows, cols)