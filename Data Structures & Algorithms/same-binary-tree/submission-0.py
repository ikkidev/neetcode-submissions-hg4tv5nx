# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def dfs(self, p, q):
        if p is None and q is None:
            return True
        if p is None and q is not None:
            return False
        if q is None and p is not None:
            return False

        # Wrong we still need to check any children and see if their value doesn't match
        # Only return early if we find a node that are not equivalent
        # if p.val == q.val:
        #     return True
        if p.val != q.val:
            return False

        return self.dfs(p.right, q.right) and self.dfs(p.left,q.left)



    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.dfs(p,q)
        