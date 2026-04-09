# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res = []
        self.dfs(root, res)
        return res

    def dfs(self, node, res) -> List[int]:
        # Base case, empty node    
        if node is None:
            return

        self.dfs(node.left, res)
        res.append(node.val)
        self.dfs(node.right, res)

        