import time
import unittest

from main import Solution


class MyTestCase(unittest.TestCase):
    def test_anagram_is_anagram(self):
        self.assertTrue(Solution().isAnagram("anagram", "nagaram"))

    def test_rat_is_not_car_anagram(self):
        self.assertFalse(Solution().isAnagram("rat", "car"))

    def test_performance_on_10000_characters(self):
        first_word = "a" * 1000000 + "b"
        second_word = "b" + "a" * 1000000
        start = time.time()
        Solution().isAnagram(first_word, second_word)
        end = time.time()
        # 30 ms
        self.assertLess(end - start, 0.03)

    def test_trivial_case(self):
        first_word = "ab"
        second_word = "ba"

        self.assertTrue(Solution().isAnagram(first_word, second_word))

    def test_anagram_with_different_letter_ordering(self):
        first_word = "dgqztusjuu"
        second_word = "dqugjzutsu"

        self.assertTrue(Solution().isAnagram(first_word, second_word))

    def test_edge_case(self):
        first_word = "aacc"
        second_word = "ccac"

        self.assertFalse(Solution().isAnagram(first_word, second_word))


if __name__ == '__main__':
    unittest.main()
