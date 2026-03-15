# Make a 2D array (list of lists)
array_2d = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# Get an element (row 1, column 2)
element = array_2d[1][2]

# Change an element
array_2d[0][0] = 9

# Add a new row
array_2d.append([1, 2, 3, 4])

# Add a new column
for row in array_2d:
    row.append(5)

# Delete a row (row 1)
del array_2d[1]

# Delete a column (column 2)
for row in array_2d:
    del row[2]

# Print the array
for row in array_2d:
    print(row)
