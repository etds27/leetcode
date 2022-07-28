class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
            When creating this, I was unaware of the Counter class within python.
            What I do is manually create a counter dictionary for one string.
            Then loop through the second string and subtract 1 for each time a character is present
            The resulting "counter" should have 0 for all characters if it is an anagram

            This method only creates a singular counter and uses less space

            I also create the counter to use the shorter string to use less space
        """
        d = {}
        if len(s) > len(t):
            shorter = t
            longer = s
        else:
            shorter = s
            longer = t


        for c in shorter:
            d.setdefault(c, 0)
            d[c] += 1

        for c in longer:
            if c not in d:
                return False
            d[c] -= 1

        for v in d.values():
            if v:
                return False

        return True
        
