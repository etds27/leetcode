class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_counter = 0
        current_substr = set()

        i = 0
        j = 0


        while i < len(s):
            l = s[i]

            while s[i] in current_substr:
                max_counter = max(len(current_substr), max_counter)

                current_substr.remove(s[j])

                j += 1

            current_substr.add(s[i])
            i += 1


        max_counter = max(len(current_substr), max_counter)
        return max_counter
        
