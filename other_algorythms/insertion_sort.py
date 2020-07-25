import unittest

def insertion_sort(A):
    for i in range(1, len(A)):
        while A[i-1] > A[i] and i >= 1:
            A[i-1], A[i] = A[i], A[i-1]
            i = i-1
    return A

class Test(unittest.TestCase):
    
    def test_even_length(self):
        A = [2,3,1,4,6,5]
        self.assertEqual(insertion_sort(A), [1,2,3,4,5,6])

    def test_odd_length(self):
        A = [3,1,4,5,2]
        self.assertEqual(insertion_sort(A), [1,2,3,4,5])

    def test_float_num(self):
        A = [1.5,0.2,0.9]
        self.assertEqual(insertion_sort(A), [0.2,0.9,1.5])

    def test_negative_num(self):
        A = [-3,-6,-8,0]
        self.assertEqual(insertion_sort(A), [-8,-6,-3,0])

    def test_empty_list(self):
        A = []
        self.assertEqual(insertion_sort(A), [])

if __name__ == '__main__':
    unittest.main()
