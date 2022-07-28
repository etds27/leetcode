class Solution:
    def myAtoi(self, s: str) -> int:
        str_ints = {"0": 0,
                    "1": 1,
                    "2": 2,
                    "3": 3,
                    "4": 4,
                    "5": 5,
                    "6": 6,
                    "7": 7,
                    "8": 8,
                    "9": 9
                   }
        s = s.strip()

        if not len(s):
            return 0

        if s[0] == "-":
            neg = True
            start_idx = 1
        elif s[0] == "+":
            neg = False
            start_idx = 1
        else:
            neg = False
            start_idx = 0

        ns = ""

        for i in range(start_idx, len(s)):
            if s[i] in str_ints:
                ns += s[i]
            else:
                break

        # print(ns)
        total = 0
        for i in range(len(ns)):
            total += str_ints[ns[i]] * 10 ** (len(ns) - i - 1)

        total = total if not neg else -total
        # print(-2 ** 31, total,  total < 2 ** 31)
        if total < -2 ** 31:
            return -2 ** 31
        elif total > 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return total
        
