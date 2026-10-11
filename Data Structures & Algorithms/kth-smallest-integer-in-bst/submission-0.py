# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        q = deque()
        q.append(root)

        while q:
            node = q.popleft()
            res.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            
        res.sort()

        return res[k - 1]
