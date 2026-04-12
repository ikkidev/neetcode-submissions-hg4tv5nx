# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfsValidHelper(root, float('-inf'), float('inf'))

    def dfsValidHelper(self, cur, low, high) -> bool:

        if cur is None:
            return True

        if not (low < cur.val < high):
            return False

        return (self.dfsValidHelper(cur.left, low, cur.val) and 
            self.dfsValidHelper(cur.right, cur.val, high))
        