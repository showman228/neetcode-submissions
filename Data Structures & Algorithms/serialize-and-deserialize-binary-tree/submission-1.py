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

        self.res = []

        def dfs(node: TreeNode):
            if not node:
                self.res.append("#")
                return
            
            self.res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return ",".join(self.res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        
        vals = iter(data.split(","))

        def dfs():
            val = next(vals)
            if val == "#":
                return None

            node = TreeNode(val)
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()






