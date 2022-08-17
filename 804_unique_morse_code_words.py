class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        abc = "abcdefghijklmnopqrstuvwxyz"
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        morse_map = {a: m for a, m in zip(abc, morse)}
        transformations = set()
        for word in words:
            trans = "".join([morse_map[c] for c in word])
            transformations.add(trans)

        return len(transformations)
