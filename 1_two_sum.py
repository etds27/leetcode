class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # O(n)
        d2 = {value: idx for idx, value in enumerate(nums)}

        # O(n)
        for idx, value in enumerate(nums):
            if target - value in d2:

                # O(1)
                idx2 = d2[target - value]

                # Make sure the same element isnt being used twice
                if idx2 == idx:
                    continue

                # O(1)
                return idx, d2[target - value]
