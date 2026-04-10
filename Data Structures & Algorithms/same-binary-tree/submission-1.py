# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        queue1, queue2 = deque(), deque()
        queue1.append(p)
        queue2.append(q)
        
        while queue1 and queue2:
            cur_p, cur_q = queue1.popleft(), queue2.popleft()

            #Need to skip adding to queue if both nodes are empty
            if not cur_p and not cur_q:
               # Do nothing
                continue
            elif cur_p and cur_q and cur_p.val == cur_q.val:
                queue1.append(cur_p.left)
                queue2.append(cur_q.left)
                queue1.append(cur_p.right)
                queue2.append(cur_q.right)
            else:
                return False

        return True
        