import unittest
import numpy as np

from numpy import linalg as la
from matrixTool import MatrixTool

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.mt = MatrixTool()

    def test_add(self):
        def run(a1, b1):
            a2 = np.array(a1)
            b2 = np.array(b1)
            self.assertListEqual(self.mt.add(a1, b1), np.add(a2, b2).tolist())

        run([
            [1, 2],
            [3, 4],
            [5, 6]
        ], [
            [0, 2],
            [1, 0],
            [4, 7]
        ])
        run([
            [0, 2, 9],
            [-5, 1, 1]
        ], [
            [0, 2, 0],
            [1, 0, 3]
        ])

    def test_multiply(self):
        def run(a1, b1):
            a2 = np.array(a1)
            b2 = np.array(b1)
            self.assertListEqual(self.mt.multiply(a1, b1), a2.dot(b2).tolist())

        run([
            [1, 2, 1],
            [3, 4, 5]
        ], [
            [0, 2],
            [1, 0],
            [1, 5]
        ])
        run([
            [1, 2, 1],
            [3, 4, 5],
            [1, 0, 1],
            [-1, 0, 2]
        ], [
            [0, 2],
            [1, 0],
            [1, 5]
        ])

    def test_transpose(self):

        def run(a1):
            a2 = np.array(a1)
            self.assertListEqual(self.mt.transpose(a1), np.transpose(a2).tolist())
            self.assertListEqual(self.mt.transpose(a2), np.transpose(a2).tolist())
            self.assertListEqual(a1, self.mt.transpose(self.mt.transpose(a1)))

        run([
            [1, 0],
            [4, 1]
        ])
        run([
            [1, 2],
            [3, 4],
            [5, 6]
        ])

    def test_trace(self):

        def run(a1):
            a2 = np.array(a1)
            self.assertEqual(self.mt.trace(a1), a2.trace())     # a2.trace - from numpy

        run([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ])
        run([
            [1, 4],
            [4, 1]
        ])
        run([
            [1, 0, 1, 0],
            [0, 2, 0, 2],
            [3, 0, 3, 0],
            [0, 4, 0, 4]
        ])

    def test_echelon_form(self):
        pass


if __name__ == '__main__':
    unittest.main()