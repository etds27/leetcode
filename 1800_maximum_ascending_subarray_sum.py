class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_total = 0
        if len(nums) == 1:
            return nums[0]

        prev = nums[0]
        total = nums[0]
        for item in nums[1::]:
            if item > prev:
                total += item
            else:
                max_total = max(max_total, total)
                total = item
            prev  = item
            # print(item)

        max_total = max(max_total, total)
        return max_total
        
