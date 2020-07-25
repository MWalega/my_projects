# 1.6 String Compression: Implement a method to perform basic string compression 
# using the counts of repeated characters. For example, the string aabcccccaaa
# would become a2blc5a3. If the "compressed" string would not become smaller 
# than the original string, your method should return the original string. 
# You can assume the string has only uppercase and lowercase letters (a - z).
# O(n)

import unittest

def string_compression(string_a):
    res = []
    new_str = string_a + ' '
    count = 0
    for i in range(0, len(new_str) - 1):
        if new_str[i] == new_str[i + 1]:
            count += 1
        else:
            count += 1
            res.append(new_str[i] + str(count))
            count = 0
    comp = ''.join(res)
    if len(comp) < len(string_a):
        return comp
    return string_a

class Test(unittest.TestCase):

    def test_empty(self):
        a = ''
        self.assertEqual(string_compression(a), a)

    def test_short_string(self):
        a = 'a'
        self.assertEqual(string_compression(a), a)

    def test_even_len(self):
        a = 'aaabbb'
        self.assertEqual(string_compression(a), 'a3b3')

    def test_odd_len(self):
        a = 'aaabb'
        self.assertEqual(string_compression(a), 'a3b2')

if __name__ == "__main__":
    unittest.main()
    