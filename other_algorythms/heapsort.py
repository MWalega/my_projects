import unittest

def heapsort(A):
    build_max_heap(A)
    result = []
    while len(A) > 1:
        A[0], A[-1] = A[-1], A[0]
        result.append(A.pop())
        max_heapify(A, 0)
    result.append(A[0])
    return result

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
    
    def test_even_length(self):
        A = [2,3,1,4,5,6]
        self.assertEqual(heapsort(A), [6,5,4,3,2,1])

    def test_odd_length(self):
        A = [2,3,4,1,6]
        self.assertEqual(heapsort(A), [6,4,3,2,1])

    def test_negative_num(self):
        A = [-2,3,1,-4,-7]
        self.assertEqual(heapsort(A), [3,1,-2,-4,-7])

    def test_float_num(self):
        A = [2.5,1,3.2,3.7,4]
        self.assertEqual(heapsort(A), [4,3.7,3.2,2.5,1])

if __name__ == '__main__':
    unittest.main()



