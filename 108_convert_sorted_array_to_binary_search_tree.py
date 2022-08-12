# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.sortedArrayToBSTHelper(nums, 0, len(nums) - 1)


    def sortedArrayToBSTHelper(self, nums, start, end):
        #print(start, end, (start + end) // 2)
        if end - start == 1:
            c = TreeNode(nums[start])
            n = TreeNode(nums[end], c)
            return n

        if start == end:
            #print(start)
            #print(TreeNode(nums[start]))
            return TreeNode(nums[start])

        mid = (start + end + 1) // 2
        mid_node = TreeNode(nums[mid])

        #print(start, mid, end, nums[mid])
        mid_node.left = self.sortedArrayToBSTHelper(nums, start, mid - 1)
        mid_node.right = self.sortedArrayToBSTHelper(nums, mid + 1, end)
        #print()
        #print(mid_node)
        #print()
        return mid_node
        
