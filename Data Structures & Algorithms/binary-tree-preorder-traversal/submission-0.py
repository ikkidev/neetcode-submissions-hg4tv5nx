# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Recursive implementation
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.dfs(root, res)
        return res

    def dfs(self, cur, res):
        #Base case reached terminal node
        if cur is None:
            return
        res.append(cur.val)
        self.dfs(cur.left, res)
        self.dfs(cur.right, res)
        