class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        valid_replace = []
        for word in words:
            word_map = {}
            existing_values = set()
            valid = True
            for i, char in enumerate(word):
                if char not in word_map:
                    word_map[char] = pattern[i]
                    if pattern[i] in existing_values:
                        valid = False
                        break
                    existing_values.add(pattern[i])

                # print(char, word_map[char], pattern[i], word_map)
                if not pattern[i] == word_map[char]:
                    # print("Invalid")
                    valid = False
                    break

            if valid:
                valid_replace.append(word)

            # print(valid, valid_replace)
        return valid_replace

        
