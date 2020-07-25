# 1.2 Check Permutation: Given two strings, write a method to decide if one is 
# a permutation of the other. 

import unittest

# 1 sposób O(nlogn)--> przyjmując, że sorted ma taką złożoność

def check_permutation1(string_a, string_b):
    if len(string_a) == 0 and len(string_b) == 0:
        return 'These strings are empty!'
    if len(string_a) != len(string_b):
        return False
    return sorted(string_a) == sorted(string_b)

# 2 sposób O(n)

import string

def check_permutation2(string_a, string_b):
    if len(string_a) == 0 and len(string_b) == 0:
        return 'These strings are empty!'
    if len(string_a) != len(string_b):
        return False
    chars = {letter: 0 for letter in string.printable}
    for char in string_a:
        chars[char] += 1
    for char in string_b:
        chars[char] -= 1
        if chars[char] < 0:
            return False
    return True

class Test(unittest.TestCase):

    def test_two_empty1(self):
        a = ''
        b = ''
        self.assertEqual(check_permutation1(a, b), 'These strings are empty!')

    def test_diff_len1(self):
        a = ''
        b = 'a'
        self.assertEqual(check_permutation1(a, b), False)

    def test_is_perm1(self):
        a = 'abcd'
        b = 'bcad'
        self.assertEqual(check_permutation1(a, b), True)

    def test_is_not_perm1(self):
        a = 'abcd'
        b = 'dbba'
        self.assertEqual(check_permutation1(a, b), False)

    def test_two_empty2(self):
        a = ''
        b = ''
        self.assertEqual(check_permutation2(a, b), 'These strings are empty!')

    def test_diff_len2(self):
        a = ''
        b = 'a'
        self.assertEqual(check_permutation2(a, b), False)

    def test_is_perm2(self):
        a = 'abcd'
        b = 'bcad'
        self.assertEqual(check_permutation2(a, b), True)

    def test_is_not_perm2(self):
        a = 'abcd'
        b = 'dbba'
        self.assertEqual(check_permutation2(a, b), False)

if __name__ == "__main__":
    unittest.main()
