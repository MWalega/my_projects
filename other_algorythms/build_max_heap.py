import unittest

def build_max_heap(A):
    for i in range(len(A)//2, -1, -1):
        max_heapify(A, i)
    return A

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

    def test_even_num(self):  
        A = [1,11,19,24,25,3,16,5,2,5]
        self.assertEqual(build_max_heap(A), [25, 24, 19, 5, 11, 3, 16, 1, 2, 5])

    def test_negative_num(self):
        A = [5,3,2,-1,0,-3,-2,-6,-8]
        self.assertEqual(build_max_heap(A), [5, 3, 2, -1, 0, -3, -2, -6, -8])

    def test_empty(self):
        A = []
        self.assertEqual(build_max_heap(A), [])

    def test_float(self):
        A = [2.1,3.5,5,0]
        self.assertEqual(build_max_heap(A), [5, 3.5, 2.1, 0])

if __name__ == '__main__':
    unittest.main()


