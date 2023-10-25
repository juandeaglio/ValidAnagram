import unittest

from main import Solution


class MyTestCase(unittest.TestCase):
    def test_anagram_is_anagram(self):
        self.assertTrue(Solution().isAnagram("anagram", "nagaram"))

    def test_rat_is_not_car_anagram(self):
        self.assertFalse(Solution().isAnagram("rat", "car"))

if __name__ == '__main__':
    unittest.main()
