class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        # Memoized dictionary to store then number of sequences that make that target
        self.memo = {0: 1}

        for i in range(1, target + 1):
            self.combinationSum4Helper(nums, i)

        return self.memo[target]

    def combinationSum4Helper(self, nums, target):
        target_set = set()
        total = 0

        # Loop through all numbers. Determine if a key in the memo will allow the current number and the key to meet the target
        # If the target is met, then add then number of instances the previous key's memo hit to this targets total
        for num in nums:
            key = target - num

            if key in self.memo:
                total += self.memo[key]

        self.memo[target] = total
        
