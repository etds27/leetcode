# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        path1 = self._getNodePath(root, p)
        path2 = self._getNodePath(root, q)

        lca = root

        for n1, n2 in zip(path1, path2):
            print(n1.val, n2.val)
            if n1 != n2:
                break

            lca = n1

        return lca



    def _getNodePath(self, node, target):
        if node is None:
            return []

        if node.val == target.val:
            return [node]

        path = []
        left_path = self._getNodePath(node.left, target)
        right_path = self._getNodePath(node.right, target)

        if not len(left_path) and not(len(right_path)):
            return []

        if len(left_path):
            return [node] + left_path

        elif len(right_path):
            return [node] + right_path


        
