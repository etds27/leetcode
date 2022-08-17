# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        self.counter = {}
        self.findFrequentTreeSumHelper(root)
        #print(self.counter)

        max_count = 0
        max_sum_vals = []
        for sum_val, count in self.counter.items():
            if count > max_count:
                max_count = count
                max_sum_vals = [sum_val]

            elif count == max_count:
                max_sum_vals.append(sum_val)

        return max_sum_vals

    def findFrequentTreeSumHelper(self, root):
        if not root.right and not root.left:
            self.counter.setdefault(root.val, 0)
            self.counter[root.val] += 1
            return root.val

        if root.left:
            left_sum = self.findFrequentTreeSumHelper(root.left)
        else:
            left_sum = 0

        if root.right:
            right_sum = self.findFrequentTreeSumHelper(root.right)
        else:
            right_sum = 0

        ret = root.val + left_sum + right_sum
        self.counter.setdefault(ret, 0)
        self.counter[ret] += 1
        return ret
