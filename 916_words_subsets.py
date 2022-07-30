class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        univ_subset = {}
        good_words = set(words1)

        # Build a universale character counter
        # Stores the maximum occurance of a specific character from each sequence in words 2
        for word in words2:
            word_counter = {}
            for char in word:
                word_counter.setdefault(char, 0)
                word_counter[char] += 1

            for char, count in word_counter.items():
                univ_subset.setdefault(char, 0)
                univ_subset[char] = max(univ_subset[char], count)

        # Build a counter for each word
        # Make sure that each char in univ subset is found in the word and the number of occurances of each character in the word is greater than universal subset
        for word in words1:
            word_counter = {}
            for char in word:
                word_counter.setdefault(char, 0)
                word_counter[char] += 1


            #print(word_counter, univ_subset)
            for char, count in univ_subset.items():
                if char not in word_counter or word_counter[char] < count:
                    #print("Removing %s" % word)
                    good_words.remove(word)
                    break

        return good_words
        
