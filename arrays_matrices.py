# Implement an array
array = ['a','1','b','2','c','3']

# Print all values, in order, with index
for i, val in enumerate(array):
    print(i, val)

# Print values in descending list order
for val in array[::-1]:
    print(val)

# Print the middle 4 values of the array
print(array[1:5])

# Create an array of integers from 1-10, inclusive
a = [x for x in range(1,11)]

# Implement a matrix
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

# Print all values in matrix, in order, from left to right
for row in matrix:
    for value in row:
        print(value)

# Print the first and last columns of the matrix
for row in matrix:
    print(row[0], row[-1])

# Re-create the matrix above using list comprehension
matrix = [[x,x+1,x+2] for x in [1,4,7]]

print(matrix)