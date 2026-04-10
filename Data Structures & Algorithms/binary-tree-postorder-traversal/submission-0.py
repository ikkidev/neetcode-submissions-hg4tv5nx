# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Recursive postorder
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], []
        cur = root
        self.dfs(cur, res)
        return res

    def dfs(self,cur,res):
        if cur is None:
            return

        self.dfs(cur.left,res)
        self.dfs(cur.right,res)
        res.append(cur.val)