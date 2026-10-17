# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root or root is None:
            return ""

        self.preorder = []
        self.inorder = []

        def preorder(node: TreeNode):
            if not node:
                return 0
            
            self.preorder.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        
        def inorder(node: TreeNode):
            if not node:
                return 0

            inorder(node.left)
            self.inorder.append(str(node.val))
            inorder(node.right)    
        
        preorder(root)
        inorder(root)

        res = "".join(self.preorder) + "." + "".join(self.inorder)

        return res

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        
        sp = data.split(".")
        self.preorder = [int(num) for num in sp[0]]
        self.inorder = [int(num) for num in sp[-1]]

        indices = {val: idx for idx, val in enumerate(self.inorder)}

        self.pre_idx = 0
        def dfs(left, right):
            if left > right:
                return None

            root_val = self.preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            mid = indices[root_val]
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)
            return root

        return dfs(0, len(self.inorder) - 1)








