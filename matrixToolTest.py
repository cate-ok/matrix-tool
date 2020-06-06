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

    def test_multiply(selfself):
        def run(a1, b1):
            pass


if __name__ == '__main__':
    unittest.main()