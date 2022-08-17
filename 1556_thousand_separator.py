class Solution:
    def thousandSeparator(self, n: int) -> str:
        l = []
        while n >= 1000:
            l.append("%03i" % (n % 1000))
            n = n // 1000
        l.append(str(n))

        return ".".join(l[::-1])
