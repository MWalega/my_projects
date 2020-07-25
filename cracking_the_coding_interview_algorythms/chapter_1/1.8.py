# 1.8 Zero Matrix: Write an algorithm such that if an element in an MxN matrix 
# is 0, its entire row and column are set to 0. 
# O(MN)

import unittest

def zero_matrix(matrix):
    M = len(matrix)
    N = len(matrix[0])
    rows = []
    columns = []
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 0:
                rows.append(i)
                columns.append(j)
    for row in rows:
        for j in range(N):
            matrix[row][j] = 0
    for column in columns:
        for i in range(M):
            matrix[i][column] = 0
    return matrix

class Test(unittest.TestCase):

    def test_empty(self):
        a = [[]]
        self.assertEqual(zero_matrix(a), [[]])

    def test_one_ele(self):
        a = [[1]]
        self.assertEqual(zero_matrix(a), [[1]])

    def test_one_zero(self):
        a = [[0]]
        self.assertEqual(zero_matrix(a), [[0]])

    def test_no_zero(self):
        a = [[1,2,3],[4,5,6],[6,7,8]]
        self.assertEqual(zero_matrix(a), a)

    def test_zeros(self):
        a = [[1,2,3,0],[0,6,7,8],[9,1,2,3]]
        self.assertEqual(zero_matrix(a), [[0,0,0,0],[0,0,0,0],[0,1,2,0]])

if __name__ == "__main__":
    unittest.main()
    