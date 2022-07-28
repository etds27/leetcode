# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        trees = self.delNodesHelper(root, to_delete)
        if root.val not in to_delete:
            trees += [root]


        return trees

    def delNodesHelper(self, root, to_delete, parent=None, parent_side=None):
        if root is None:
            return []
        #print(root, root.val in to_delete)
        trees = []
        if root.val in to_delete:
            # print("Deleting %i" % root.val)
            if parent is not None:
                # True = left
                if parent_side:
                    parent.left = None
                else:
                    parent.right = None

            if root.left is not None and root.left.val not in to_delete:
                trees.append(root.left)
            if root.right is not None and root.right.val not in to_delete:
                trees.append(root.right)
            # print("New trees starting at %s" % [n.val for n in trees if n is not None])

        trees += self.delNodesHelper(root.left, to_delete, parent=root, parent_side=True) + self.delNodesHelper(root.right, to_delete, parent=root, parent_side=False)


        return trees
        
