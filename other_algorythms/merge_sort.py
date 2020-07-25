import unittest

def merge_sort(A):
    if len(A) <= 1:
        return A
    left, right = merge_sort(A[:int(len(A)/2)]), merge_sort(A[int(len(A)/2):])
    return merge(left, right)

def merge(a, b):
    c = []
    a_ind, b_ind = 0, 0
    while a_ind < len(a) and b_ind < len(b):
        if a[a_ind] < b[b_ind]:
            c.append(a[a_ind])
            a_ind += 1
        else:
            c.append(b[b_ind])
            b_ind += 1
    if a_ind == len(a):
        c.extend(b[b_ind:])
    else:
        c.extend(a[a_ind:])
    return c


class Test(unittest.TestCase):

    def test_even_length(self):
        A = [2,3,1,4,6,5]
        self.assertEqual(merge_sort(A), [1,2,3,4,5,6])

    def test_odd_length(self):
        A = [3,1,4,5,2]
        self.assertEqual(merge_sort(A), [1,2,3,4,5])

    def test_float_num(self):
        A = [1.5,0.2,0.9]
        self.assertEqual(merge_sort(A), [0.2,0.9,1.5])

    def test_negative_num(self):
        A = [-3,-6,-8,0]
        self.assertEqual(merge_sort(A), [-8,-6,-3,0])

    def test_empty_list(self):
        A = []
        self.assertEqual(merge_sort(A), [])

if __name__ == '__main__':
    unittest.main()
