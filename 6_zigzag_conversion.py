class Solution:
    def convert(self, s: str, numRows: int) -> str:
        i = 0
        ns = ""

        if numRows == 1:
            return s

        mod = (numRows - 1) * 2

        for i in range(numRows):
            numElem = int(len(s) / mod + 1)
            # Calculate the idnices of the characters depending on the row
            # Each list of indices is on a periodic of the zig zag cycle length
            # Calculate 2 lists for middle rows because there should be 2 letters per row
            # Calculate one offset from the left and one offset from the right
            idxs_l = [idx * mod + i for idx in range(numElem)]
            idxs_r = [idx * mod - i for idx in range(1, numElem + 1)]


            if i != 0 and i != numRows - 1:
                for idx_l, idx_r in zip(idxs_l, idxs_r):
                    if idx_l < len(s):
                        ns += s[idx_l]
                    if idx_r < len(s):
                        ns += s[idx_r]
            else:
                for idx in idxs_l:
                    if idx < len(s):
                        ns += s[idx]



        return ns
