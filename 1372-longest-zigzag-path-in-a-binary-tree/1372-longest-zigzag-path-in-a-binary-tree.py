# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestZigZag(self, root):
        self.ans = 0

        def dfs(node, left_len, right_len):
            if not node:
                return

            self.ans = max(self.ans, left_len, right_len)

            # Move Left
            dfs(node.left, right_len + 1, 0)

            # Move Right
            dfs(node.right, 0, left_len + 1)

        dfs(root, 0, 0)

        return self.ans