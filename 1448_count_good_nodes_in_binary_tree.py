# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return  self.goodNodesHelper(root, max_num=-100000)

    def goodNodesHelper(self, root, max_num):
        count = 1 if root.val >= max_num else 0

        if not root.left and not root.right:
            return count

        # print(root, max(max_num, root.val))
        if root.left:
            count += self.goodNodesHelper(root.left, max(max_num, root.val))

        if root.right:
            count += self.goodNodesHelper(root.right, max(max_num, root.val))

        return count
            
