# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root)

        while q:
            node = q.popleft()

            if node.left and node.right:
                if (node.left.val > node.right.val) or (node.val > node.right.val) or (node.val < node.left.val):
                    return False

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        
        return True