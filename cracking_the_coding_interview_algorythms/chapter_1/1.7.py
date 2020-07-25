# 1.7 Rotate Matrix: Given an image represented by an NxN matrix, where each 
# pixel in the image is 4 bytes, write a method to rotate the image by 90 
# degrees. Can you do this in place?
# O(n2)

# sposób 1 (moim zdaniem czytelniejszy)

def rotate_matrix1(matrix):
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - 1 - i):
            # save the top
            top = matrix[i][j]
            # move left to top
            matrix[i][j] = matrix[n - 1 - j][i]
            # move bottom to left
            matrix[n - 1 - j][i] = matrix[n - i - 1][n - j - 1]
            # move right to bottom
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
            # move top to right
            matrix[j][n - i - 1] = top
    return matrix

# sposób 2 (ciężej na niego wpaść)

def rotate_matrix2(matrix):
    if matrix == [[]]:
        return matrix
    n = len(matrix)
    # transpose
    for i in range(n):
        for j in range(i, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    # reverse each row
    for i in range(n):
        start = 0
        end = n - 1
        while start < end:
            temp = matrix[i][start]
            matrix[i][start] = matrix[i][end]
            matrix[i][end] = temp
            start += 1
            end -= 1
    return matrix

import unittest

class Test(unittest.TestCase):

    def test_empty1(self):
        a = [[]]
        self.assertEqual(rotate_matrix1(a), [[]])

    def test_one_ele1(self):
        a = [[1]]
        self.assertEqual(rotate_matrix1(a), [[1]])

    def test_two_ele1(self):
        a = [[1,2],[3,4]]
        self.assertEqual(rotate_matrix1(a), [[3,1],[4,2]])

    def test_three_ele1(self):
        a = [[1,2,3],[4,5,6],[7,8,9]]
        self.assertEqual(rotate_matrix1(a), [[7,4,1],[8,5,2],[9,6,3]])

    def test_empty2(self):
        a = [[]]
        self.assertEqual(rotate_matrix2(a), [[]])

    def test_one_ele2(self):
        a = [[1]]
        self.assertEqual(rotate_matrix2(a), [[1]])

    def test_two_ele2(self):
        a = [[1,2],[3,4]]
        self.assertEqual(rotate_matrix2(a), [[3,1],[4,2]])

    def test_three_ele2(self):
        a = [[1,2,3],[4,5,6],[7,8,9]]
        self.assertEqual(rotate_matrix2(a), [[7,4,1],[8,5,2],[9,6,3]])

if __name__ == "__main__":
    unittest.main()