# 1.5 One Away: There are three types of edits that can be performed on strings: 
# insert a character, remove a character, or replace a character. Given two 
# strings, write a function to check if they are one edit (or zero edits) away.
# O(n)

import unittest

def one_away(string_a, string_b):
    if len(string_a) - len(string_b) == 0:
        return check_one_replace(string_a, string_b)
    if len(string_a) - len(string_b) == -1:
        return check_one_insert(string_a, string_b)
    if len(string_a) - len(string_b) == 1:
        return check_one_remove(string_a, string_b)
    return False

def check_one_replace(string_a, string_b):
    count = 0
    for i in range(0, len(string_a)):
        if string_a[i] != string_b[i]:
            count += 1
            if count > 1:
                return False
    return True

def check_one_insert(string_a,string_b):
    i_a = 0
    i_b = 0
    while i_a < len(string_a) and i_b < len(string_b):
        if string_a[i_a] != string_b[i_b]:
            if i_a == i_b:
                i_b += 1
            else:
                return False
        else: 
            i_a += 1
            i_b += 1
    return True

def check_one_remove(string_a, string_b):
    i_a = 0
    i_b = 0
    while i_a < len(string_a) and i_b < len(string_b):
        if string_a[i_a] != string_b[i_b]:
            if i_a == i_b:
                i_a += 1
            else:
                return False
        else: 
            i_a += 1
            i_b += 1
    return True

class Test(unittest.TestCase):

    def test_two_empty(self):
        a = ''
        b = ''
        self.assertEqual(one_away(a, b), True)

    def test_zero_edits(self):
        a = 'a'
        b = 'b'
        self.assertEqual(one_away(a, b), True)
    
    def test_more_edits(self):
        a = 'a'
        b = 'abc'
        self.assertEqual(one_away(a, b), False)

    def test_one_ins_true(self):
        a = 'aaa'
        b = 'aaab'
        self.assertEqual(one_away(a, b), True)

    def test_one_ins_false(self):
        a = 'aaa'
        b = 'abcd'
        self.assertEqual(one_away(a, b), False)

    def test_one_rep_true(self):
        a = 'aaa'
        b = 'aba'
        self.assertEqual(one_away(a, b), True)

    def test_one_rep_false(self):
        a = 'aaa'
        b = 'bba'
        self.assertEqual(one_away(a, b), False)

    def test_one_rem_true(self):
        a = 'aaa'
        b = 'aa'
        self.assertEqual(one_away(a, b), True)

    def test_one_rem_false(self):
        a = 'aaa'
        b = 'bb'
        self.assertEqual(one_away(a, b), False)

if __name__ == "__main__":
    unittest.main()
    