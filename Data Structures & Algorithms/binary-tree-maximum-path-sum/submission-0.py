# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        def path_sm(node):
            nonlocal res
            if not node:
                return 0 
            left  = max(path_sm(node.left), 0)
            right = max(path_sm(node.right), 0)
            sm = left + right + node.val
            res = max(sm, res)
            return max(left, right) + node.val
        path_sm(root)
        return res



        