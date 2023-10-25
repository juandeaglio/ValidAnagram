class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first_word = sorted(s)
        second_word = sorted(t)
        return len(s) == len(t) and first_word == second_word
