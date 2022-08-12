# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTHelper(root, None, None)

    def isValidBSTHelper(self, root, min_val, max_val):
        #print(root)
        if root.left is None and root.right is None:
            return True


        if root.left is not None:
            if (min_val is None or root.left.val > min_val) and root.val > root.left.val:
                #print("min", min_val, root.left.val, root.val, "max", max_val)
                ret = self.isValidBSTHelper(root.left, min_val, root.val)
            else:
                return False

            if not ret:
                return ret
        #print("Left side good")
        if root.right is not None:
            if (max_val is None or root.right.val < max_val) and root.val < root.right.val:
                #print(min_val, root.right.val, root.val, max_val)

                ret = self.isValidBSTHelper(root.right, root.val, max_val)
            else:
                return False

        return ret
