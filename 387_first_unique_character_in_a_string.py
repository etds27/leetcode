class Solution:
    def firstUniqChar(self, s: str) -> int:
        letter_counter = {}
        for letter in s:
            letter_counter.setdefault(letter, 0)
            letter_counter[letter] += 1

        for i, letter in enumerate(s):
            if letter_counter[letter] == 1:
                return i
        return -1

        
