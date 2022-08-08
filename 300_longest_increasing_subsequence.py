class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        store = []
        for num in nums:
            if not len(store) or num > store[-1]:
                store.append(num)
            else:
                idx = self.binarySearch(store, 0, len(store), num)
                store[idx] = num

            #print(store)
        return len(store)
        #print(self.binarySearch(sorted(nums), 0, len(nums), 4))


    def binarySearch(self, nums, l, r, target):

        if l == r:
            return l

        mid = (l + r) // 2
        #print(nums, mid, l, r)
        if nums[mid] == target:
            return mid

        elif nums[mid] > target:
            return self.binarySearch(nums, l, mid, target)
        else:
            return self.binarySearch(nums, mid + 1, r, target)
        
