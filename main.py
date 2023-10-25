from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if len(s) > 10000000000:
            equal = self.isCountEqualDictionary(s, t)
        else:
            equal = self.isCountEqualStrFunctions(s, t)
        return len(s) == len(t) and equal

    def isCountEqualDictionary(self, s, t):
        # uses a default dictionary, better than {} because it does not do a check for the key.
        total_counts = defaultdict(int)

        for char in s:
            total_counts[char] += 1

        for char in t:
            if total_counts == 0:
                return False
            else:
                total_counts[char] -= 1

        # make sure all values in total_counts == 0
        return all(value == 0 for value in total_counts.values())

    def isCountEqualStrFunctions(self, s, t):
        # more verbose and faster for smaller strings because no dictionary is used.
        total_counts = 0
        original_length = len(s)

        # Not sure on the Big O here, maybe O(n^2)
        # worst case if we're dealing with a bunch of distinct characters, or all characters are distinct.
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
