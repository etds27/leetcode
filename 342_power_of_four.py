class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n  >= 0:
            bin_str = bin(n)[2:]
        else:
            return False
        # print(bin_str, bin_str.count("1"), )
        if len(bin_str) % 2 and bin_str.count("1") == 1:
            return True
        return False
