import unittest

def quick_sort(A):
    if len(A) <= 1:
        return A
    pivot = A.pop()
    left, right = [], []
    for i in A:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)
    return quick_sort(left) + [pivot] + quick_sort(right)

class Test(unittest.TestCase):

    def test_even_length(self):
        A = [1,4,3,2]
        self.assertEqual(quick_sort(A), [1,2,3,4])

    def test_odd_length(self):
        A = [2,4,5,1,3]
        self.assertEqual(quick_sort(A), [1,2,3,4,5])

    def test_float_num(self):
        A = [1.5,0.2,1.9]
        self.assertEqual(quick_sort(A), [0.2,1.5,1.9])

    def test_negative_num(self):
        A = [-3,-6,1,-2]
        self.assertEqual(quick_sort(A), [-6,-3,-2,1])

if __name__ == '__main__':
    unittest.main()
