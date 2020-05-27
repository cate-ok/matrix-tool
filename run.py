import matrixTool as mt

A = [
  [0, 0, 1, 0],
  [0, 2, 0, 2],
  [3, 0, 3, 0],
  [0, 4, 0, 4]
]
mt.echelon_form(A)
print(A)