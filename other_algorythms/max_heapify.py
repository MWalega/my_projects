import unittest

def max_heapify(A, i):
    l = 2*i+1
    r = l+1
    if l <= len(A)-1 and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= len(A)-1 and A[r] > A[largest]:
        largest = r
    if i != largest:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)
    return A

class Test(unittest.TestCase):

    def test_even_length(self):
        A = [16,4,10,14,7,9,3,2,8,1]
        self.assertEqual(max_heapify(A, 1), [16,14,10,8,7,9,3,2,4,1])
    
    def test_odd_length(self):
        A = [16,4,10,14,7,9,3,2,8,1,0]
        self.assertEqual(max_heapify(A, 1), [16,14,10,8,7,9,3,2,4,1,0])

    def test_empty(self):
        A = []
        self.assertEqual(max_heapify(A, 6), [])

    def test_negative(self):
        A = [5,-1,2,3,0,-3,-2,-6,-8]
        self.assertEqual(max_heapify(A, 1), [5,3,2,-1,0,-3,-2,-6,-8])

    def test_float(self):
        A = [16,4.5,10,14.2,7,9,3,2,8,1]
        self.assertEqual(max_heapify(A, 1), [16,14.2,10,8,7,9,3,2,4.5,1])

if __name__ == '__main__':
    unittest.main()

