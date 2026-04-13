# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True
            
        low = float("-inf")
        high = float("inf")
        queue = deque([(root,low,high)])


        while queue:
            size = len(queue)
            for _ in range(size):
                cur, low, high = queue.popleft()
                if not(low < cur.val < high):
                    return False
                if cur.left:
                    queue.append((cur.left,low,cur.val))
                if cur.right:
                    queue.append((cur.right,cur.val,high))

        return True
        