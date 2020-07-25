import unittest

def binary_search(A, x):
    s_ind = 0
    e_ind = len(A)-1
    while s_ind <= e_ind:
        m_ind = (s_ind + e_ind)//2
        if A[m_ind] == x:
            return m_ind
        elif A[m_ind] > x:
            e_ind = m_ind-1
        else:
            s_ind = m_ind+1

class Test(unittest.TestCase):

    def test_even_length(self):
        A = [1,2,3,4,5,6]
        x = 3
        self.assertEqual(binary_search(A, x), 2)

    def test_odd_length(self):
        A = [1,2,3,4,5]
        x = 4
        self.assertEqual(binary_search(A, x), 3)

    def test_float_num(self):
        A = [1.5,1.9,2.3,4,5.5]
        x = 1.9
        self.assertEqual(binary_search(A, x), 1)

    def test_negative_num(self):
        A = [-2,-1,3,4]
        x = -2
        self.assertEqual(binary_search(A, x), 0)

    def test_empty_list(self):
        A = []
        x = 6
        self.assertEqual(binary_search(A, x), None)

if __name__ == '__main__':
    unittest.main()


    