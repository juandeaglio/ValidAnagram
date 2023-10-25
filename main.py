class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first_word_letter_counts = self.getCounts(s)
        seconds_word_letter_counts = self.getCounts(t)
        return len(s) == len(t) and first_word_letter_counts == seconds_word_letter_counts

    def getCounts(self, s):
        total_counts = 0
        counts = {}
        while total_counts <= len(s):
            letter = s[0]
            counts[letter] = s.count(letter)
            s = s.replace(letter, "")
            total_counts += counts[letter]

        return counts
