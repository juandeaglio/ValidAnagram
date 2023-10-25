class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        equal = self.isCountEqual(s, t)
        return len(s) == len(t) and equal

    def isCountEqual(self, s, t):
        #more verbose and faster
        total_counts = 0
        original_length = len(s)

        # In total O(n^2)
        while total_counts < original_length:
            letter = s[0]
            # O(n) for .count as well, since we're only checking a 1 length character in the words.
            letter_count = s.count(letter)

            if letter_count != t.count(letter):
                return False

            # Since the strings are of equal length in an anagram, worst case is O(n) in .replace()
            # Seen in source: https://github.com/python/cpython/blob/main/Objects/unicodeobject.c#L10097
            s = s.replace(letter, "")
            total_counts += letter_count


        return True
