# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# The key insight is: to check if `subRoot` is a subtree of `root`, you need to:
# 1. Traverse through `root` (BFS or DFS)
# 2. For each node in `root`, check if the tree starting from that node is identical to `subRoot`

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        # BFS to traverse root
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            
            # Check if subtree starting at current node matches subRoot
            if self.isSameTree(node, subRoot):
                return True
            
            # Add children to continue BFS
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return False
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Helper function to check if two trees are identical
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


