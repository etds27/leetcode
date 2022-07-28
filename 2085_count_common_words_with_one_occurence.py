class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        word_count1 = {}
        word_count2 = {}

        for word in words1:
            word_count1.setdefault(word, 0)
            word_count1[word] += 1

        for word in words2:
            word_count2.setdefault(word, 0)
            word_count2[word] += 1

        occurances = 0
        for word, count in word_count1.items():
            if count == 1 and word in word_count2 and word_count2[word] == 1:
                occurances += 1
        return occurances
