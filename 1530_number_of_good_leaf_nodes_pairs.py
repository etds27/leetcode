# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.good_pairs = 0
        self.distance = distance

        self.findChildrenLength(root)
        return self.good_pairs

    def findChildrenLength(self, root):
        if not root.left and not root.right:
            return [1]

        if root.left:
            left_children = self.findChildrenLength(root.left)
        else:
            left_children = []
        if root.right:
            right_children = self.findChildrenLength(root.right)
        else:
            right_children = []


        for l_child in left_children:
            for r_child in right_children:
                if l_child + r_child <= self.distance:
                    self.good_pairs += 1

        return [lc + 1 for lc in left_children] + [rc + 1 for rc in right_children]
