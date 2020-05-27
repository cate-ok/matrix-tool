

class MatrixTool:

    def __init__(self):
        pass

    def swap_rows(self, a, i1, i2):
        t_row = a[i1]
        a[i1] = a[i2]
        a[i2] = t_row

    def multiply_by_num(self, a, i, num):
        for j in range(len(a[i])):
            a[i][j] *= num

    def add_row_elements(self, a, row_to, row_from, k):
        for j in range(len(a[row_to])):
            a[row_to][j] += a[row_from][j] * k

    def print_matrix(self, a):
        for row in a:
            print(row)

    def echelon_form(self, a):
        rows_a = len(a)
        if rows_a == 0:
            return
        cols_a = len(a[0])

        def find_leading_element(row_num, col_num):
            for j in range(col_num, cols_a):
                for i in range(row_num, rows_a):
                    if a[i][j] != 0:
                        if i == row_num:
                            return j
                        else:
                            self.swap_rows(a, row_num, i)
                            return j
            return None

        j = 0
        for i in range(rows_a):
            # 1
            leading_elem_j = find_leading_element(i, j)
            print('1')
            self.print_matrix(a)

            # 2
            if leading_elem_j == None:
                print('Leading element is 0')
                return

            j = leading_elem_j
            leading_elem = a[i][j]
            self.multiply_by_num(a, i, 1 // leading_elem)

            print('2')
            self.print_matrix(a)

            if i == (rows_a - 1):
                print('Leading row is last row')
                return
            elif j == (cols_a - 1):
                print('Last column')
                return
            else:
                j += 1

            # 3
            for l in range(i + 1, rows_a):
                el1 = a[i][j]
                el2 = a[l][j]
                if el1 == 0:
                    continue
                k = (-1) * el2 // el1
                self.add_row_elements(a, l, i, k)

            print('3')
            self.print_matrix(a)

            # 4
            if i == (rows_a - 1) and j == (cols_a - 1):
                continue