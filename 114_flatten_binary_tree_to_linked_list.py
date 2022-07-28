# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return []
        self.flattenHelper(root)

    def flattenHelper(self, root, parent=None, depth=0):
        #print(root, depth)
        if root.left is None and root.right is None:
            #print("Found leaf", root.val)
            return root


        temp_left = root.left
        temp_right = root.right
        attach_point = root
        bottom = root
        if root.left is not None:
            left_bottom = self.flattenHelper(root.left, depth=depth+1)
            root.right = root.left
            root.left = None
            attach_point = left_bottom
            bottom = left_bottom

        if temp_right is not None:
            right_bottom = self.flattenHelper(temp_right, depth=depth+1)
            attach_point.right = temp_right
            bottom = right_bottom



        #print(root, depth)
        return bottom
        
