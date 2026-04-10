# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node):
        
        cur = node

        if cur is None:
            return

        cur.left , cur.right = cur.right, cur.left

        self.dfs(cur.left)
        self.dfs(cur.right)


    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #Intuition traverse tree top down and swap left and right child
        self.dfs(root)
        return root
        