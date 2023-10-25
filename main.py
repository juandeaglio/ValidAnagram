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
        # uses a dictionary (which is just a hashmap) with O(1) lookup times
        total_counts = {}

        for char in s:
            total_counts[char] = total_counts.get(char, 0) + 1

        for char in t:
            if char not in total_counts:
                return False

            total_counts[char] -= 1
            if total_counts[char] == 0:
                del total_counts[char]

        return not total_counts

    def isCountEqualStrFunctions(self, s, t):
        #more verbose and faster
        total_counts = 0
        original_length = len(s)

        # Not sure on the Big O here, maybe O(n^2) worst case if we're dealing with a bunch of distinct characters, or all characters are distinct.
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
