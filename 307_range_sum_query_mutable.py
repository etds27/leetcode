import math

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        len_nums_st = math.ceil(math.log2(len(nums)))
        # print(len_nums_st)
        self.nums_st = [0] * (2 * 2 ** len_nums_st - 1)

        self.constructNumArray(0, len(self.nums) - 1, 0)

    def constructNumArray(self, start, end, i):
        if start == end:
            # print(start, end, i, self.nums)
            self.nums_st[i] = self.nums[start]
            return self.nums_st[i]

        mid = (start + end) // 2
        # print(start, end, mid, i, self.nums)
        self.nums_st[i] = self.constructNumArray(start, mid, i * 2 + 1) + \
                          self.constructNumArray(mid + 1, end, i * 2 + 2)
        # print(self.nums_st)
        return self.nums_st[i]

    def sumRangeHelper(self, start, end, query_start, query_end, i):
        # print(start, end, query_start, query_end, i)
        if query_start <= start and query_end >= end:
            # print("Returning %i" % self.nums_st[i])
            return self.nums_st[i]

        if end < query_start or start > query_end:
            # print("ooo", start, query_start, end, query_end)
            return 0

        mid = (start + end) // 2

        ret = self.sumRangeHelper(start, mid, query_start, query_end, 2 * i + 1) + \
              self.sumRangeHelper(mid + 1, end, query_start, query_end, 2 * i + 2)
        # print("Returning comb %i" % ret)
        return ret

    def updateHelper(self, start, end, i, delta, si):
        if i < start or i > end:
            return 0

        # print("Updating ", start, end, i, delta, si, self.nums_st)


        if not start == end:
            mid = (start + end) // 2
            self.updateHelper(start, mid, i, delta, 2 * si + 1)
            self.updateHelper(mid + 1, end, i, delta, 2 * si + 2)
        self.nums_st[si] += delta


    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        self.updateHelper(0, len(self.nums) - 1, index, delta, 0)


    def sumRange(self, left: int, right: int) -> int:
        # print(self.nums_st)
        return self.sumRangeHelper(0, len(self.nums) - 1, left, right, 0)



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
