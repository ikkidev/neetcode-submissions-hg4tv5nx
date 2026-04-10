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
        self.dfs_inorder_iterative(root, res)
        return res

    def dfs_inorder(self, node, res) -> List[int]:
        # Base case, empty node    
        if node is None:
            return

        self.dfs_inorder(node.left, res)
        res.append(node.val)
        self.dfs_inorder(node.right, res)

    def dfs_inorder_iterative(self, node, res) -> List[int]:
        stack = collections.deque()
        cur = node 
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right

        