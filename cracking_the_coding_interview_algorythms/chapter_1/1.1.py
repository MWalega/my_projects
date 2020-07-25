# 1.1 Is Unique: Implement an algorithm to determine if a string has all unique 
# characters. What if you cannot use additional data structures?

# 1 sposób O(n)

import unittest
import string

def is_unique1(str_a):
    if len(str_a) == 0:
        return "This string is empty!"
    if len(str_a) > 128:
        return False
    prev = {char: 0 for char in string.printable}
    for char in str_a:
        prev[char] += 1
        if prev[char] > 1:
            return False
    return True

class Test(unittest.TestCase):

    def test_empty(self):
        a = ""
        self.assertEqual(is_unique1(a), "This string is empty!")

    def test_one_element(self):
        a = "a"
        self.assertEqual(is_unique1(a), True)

    def test_even_num(self):
        a = "abcd"
        self.assertEqual(is_unique1(a), True)

    def test_odd_num(self):
        a = "abcde"
        self.assertEqual(is_unique1(a), True)

    def test_not_unique(self):
        a = "abad"
        self.assertEqual(is_unique1(a), False)

if __name__ == '__main__':
    unittest.main()

# 2 sposób jeśli nie można użyć dict: O(nlogn)
# Najpierw merge sort na stringu, a potem funkcja z loopem porównującym czy
# wartości obok siebie są identyczne, jeśli tak --> False