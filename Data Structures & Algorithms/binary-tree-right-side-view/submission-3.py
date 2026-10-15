# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        q = deque()

        if not root:
            return []

        q.append([root, 0])

        while q:
            node, depth = q.popleft()

            if len(res) == depth:
                res.append(node.val)
            
            if node.right:
                q.append([node.right, depth + 1])
            if node.left:
                q.append([node.left, depth + 1])
            
        return res