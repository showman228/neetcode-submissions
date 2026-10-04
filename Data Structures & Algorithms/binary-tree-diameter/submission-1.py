# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diametor = 0

        if not root:
            return 0

        def dfs(node: TreeNode):
            if not node:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            self.diametor = max(self.diametor, left_height + right_height)

            return 1 + max(left_height, right_height)

        dfs(root)
        
        return self.diametor