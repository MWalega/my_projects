# 1.3 URLify: Write a method to replace all spaces in a string with '%20': You 
# may assume that the string has sufficient space at the end to hold the  
# additional characters, and that you are given the "true" length of the string.
# O(n) jeśli tyle zajmuje .replace()

import unittest

def URLify(string, a):
    new_str = string[:a]
    return new_str.replace(' ', '%20')

class Test(unittest.TestCase):

    def test_empty(self):
        str_a = ''
        a = 0
        self.assertEqual(URLify(str_a, a), '')

    def test_no_spaces(self):
        str_a = 'abc'
        a = 3
        self.assertEqual(URLify(str_a, a), 'abc')

    def test_no_spaces_in_word(self):
        str_a = 'abc   '
        a = 3
        self.assertEqual(URLify(str_a, a), 'abc')

    def test_one_space(self):
        str_a = 'a bc  '
        a = 4
        self.assertEqual(URLify(str_a, a), 'a%20bc')

    def test_many_spaces(self):
        str_a = 'ab cd e f   '
        a = 9
        self.assertEqual(URLify(str_a, a), 'ab%20cd%20e%20f')

if __name__ == "__main__":
    unittest.main()

    
