# 1.4 Palindrome Permutation: Given a string, write a function to check if it  
# is a permutation of a palindrome. A palindrome is a word or phrase that is the 
# same forwards and backwards. A permutation is a rearrangement of letters. 
# O(n)

import unittest
import string

def palindrome_permutation(string_a):
    if len(string_a) == 0:
        return 'This string is empty!'
    new_str = string_a.replace(' ', '').lower()
    letters = {letter: 0 for letter in string.ascii_lowercase}
    for letter in new_str:
        letters[letter] += 1
    if len(new_str) % 2 == 0:
        for num in letters.values():
            if num % 2 != 0:
                return False
        return True
    if len(new_str) % 2 != 0:
        count = 0
        for num in letters.values():
            if num % 2 != 0:
                count += 1
                if count > 1:
                    return False
        return True

class Test(unittest.TestCase):

    def test_empty(self):
        a = ''
        self.assertEqual(palindrome_permutation(a), 'This string is empty!')

    def test_one_char(self):
        a = 'a'
        self.assertEqual(palindrome_permutation(a), True)

    def test_even_len_true(self):
        a = 'Tact Coao'
        self.assertEqual(palindrome_permutation(a), True)

    def test_even_len_false(self):
        a = 'Toct Coao'
        self.assertEqual(palindrome_permutation(a), False)

    def test_odd_len_true(self):
        a = 'Tact Coa'
        self.assertEqual(palindrome_permutation(a), True)

    def test_odd_len_false(self):
        a = 'Taat Coa'
        self.assertEqual(palindrome_permutation(a), False)

if __name__ == "__main__":
    unittest.main()

