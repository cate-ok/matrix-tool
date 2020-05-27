from matrixTool import MatrixTool

print('Test changes')

# A = [
#   [0, 0, 1, 0],
#   [0, 2, 0, 2],
#   [3, 0, 3, 0],
#   [0, 4, 0, 4]
# ]

A = [[0, 1, 1, 1, 1, 1],
     [0, 1, 1, 2, 3, 2],
     [0, 2, 2, 1, 2, 1],
     [0, 4, 4, 4, 6, 4]]

mt = MatrixTool()
mt.echelon_form(A)

for row in A:
    print(row)