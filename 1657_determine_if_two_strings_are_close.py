class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counter1 = {}
        counter2 = {}

        for letter in word1:
            counter1.setdefault(letter, 0)
            counter1[letter] += 1
        for letter in word2:
            counter2.setdefault(letter, 0)
            counter2[letter] += 1

        if not len(counter1) == len(counter2):
            return False

        #print(counter1, counter2)


        for kv1, kv2 in zip(sorted(counter1.items(), key=lambda kv: (kv[1], kv[0])), \
                    sorted(counter2.items(), key=lambda kv: (kv[1], kv[0]))):
            #print(kv1, kv2)
            if kv1[0] != kv2[0]:




                if kv1[0] not in counter2:
                    return False

                counter2[kv1[0]], counter2[kv2[0]] = counter2[kv2[0]], counter2[kv1[0]]
                #print(counter2)


            if not kv1[1] == kv2[1]:
                return False

        return True
        #print(counter1, counter2)
