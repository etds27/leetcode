class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        dec = None
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue

            if dec is None:
                dec = nums[i] - nums[i + 1] >= 0

            if not nums[i] == nums[i + 1] and (nums[i] - nums[i + 1] >= 0) is not dec:
                return False


        return True

        
