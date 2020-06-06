

class MatrixTool:

    def __init__(self):
        pass

    def add(self, a, b):
        len_a = len(a)
        len_b = len(b)

        if len_a != len_b:
            raise ValueError('matrices should have the same size')

        c = []
        if len_a == 0:
            return c

        len_row_a = len(a[0])
        len_row_b = len(b[0])
        if len_row_a != len_row_b:
            raise ValueError('matrices should have the same size')

        for i in range(len_a):
            c.append([])
            for j in range(len_row_a):
                c[i].append(a[i][j] + b[i][j])
        return c

    def multiply(self, a, b):
        """
        :param a: matrix A (m x p)
        :param b: matrix B (p x n)
        :return: A * B
        """
        c = []
        rows_a = len(a)
        rows_b = len(b)
        if rows_a == 0 or rows_b == 0:
            return c
        cols_a = len(a[0])
        cols_b = len(b[0])
        if cols_a != rows_b:
            raise ValueError("matrices don't match")

        for i in range(rows_a):
            c.append([])
            for j in range(cols_b):
                res = 0
                for k in range(cols_a):
                    res += a[i][k] * b[k][j]
                c[i].append(res)
        return c

    def transpose(self, a):
        c = []
        rows_a = len(a)
        cols_a = len(a[0])

        for i in range(cols_a):
            res = []
            for j in range(rows_a):
                res.append(a[j][i])
            c.append(res)
        return c

    def trace(self, a):
        result = 0
        rows_a = len(a)
        if rows_a == 0:
            return result
        cols_a = len(a[0])
        if cols_a != rows_a:
            raise ValueError("matrix must be square")
        k = 0
        for i in range(rows_a):
            result += a[i][k]
            k += 1
        return result

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