# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #        aExcellent question! If it's **not a BST** (just a regular binary tree), the problem changes significantly because you lose the ordering property. Let's compare:

# ## BST Solution (Your Current Code)
# ```python
# def lowestCommonAncestor(self, root, p, q):
#     if not root:
#         return None
    
#     # Use BST property: compare values
#     if p.val < root.val and q.val < root.val:
#         return self.lowestCommonAncestor(root.left, p, q)
#     if p.val > root.val and q.val > root.val:
#         return self.lowestCommonAncestor(root.right, p, q)
    
#     return root  # Split point found
# ```

# ## Regular Binary Tree Solution
# For a regular binary tree (no ordering), you need a different approach:

# ### Approach 1: Post-order DFS (Most Common)
# ```python
# def lowestCommonAncestor(self, root, p, q):
#     if not root:
#         return None
    
#     # Base case: if root is p or q, return root
#     if root == p or root == q:
#         return root
    
#     # Search in left and right subtrees
#     left = self.lowestCommonAncestor(root.left, p, q)
#     right = self.lowestCommonAncestor(root.right, p, q)
    
#     # If both left and right return non-null, root is LCA
#     if left and right:
#         return root
    
#     # Otherwise, return whichever is non-null
#     return left or right
# ```

# ### How This Works:
# 1. **Base cases**: 
#    - If `root` is `None`, return `None`
#    - If `root` is `p` or `q`, return `root` (we found one of the nodes)

# 2. **Recursive search**:
#    - Search left subtree for `p` or `q`
#    - Search right subtree for `p` or `q`

# 3. **LCA determination**:
#    - If **both** left and right return non-null values, `root` is the LCA
#    - If only **one** side returns non-null, that's the LCA (or path to it)
#    - If **neither** returns non-null, return `None`

# ### Example Walkthrough:
# ```
#        3
#       / \
#      5   1
#     / \ / \
#    6  2 0  8
#      / \
#     7   4
# ```
# Find LCA of nodes 5 and 1:
# - Start at 3: left finds 5, right finds 1 → both non-null → 3 is LCA

# Find LCA of nodes 5 and 4:
# - At 3: left finds path to both, right finds nothing
# - At 5: left finds 6 (not 4), right finds path to 4
# - At 2: left finds 7 (not 4), right finds 4
# - Since 5 has both left and right returning something (6 and path to 4), 5 is LCA

# ## Key Differences:

# | Aspect | BST Solution | Regular Binary Tree Solution |
# |--------|-------------|-----------------------------|
# | **Logic** | Use value comparisons | Use post-order DFS |
# | **Decision** | Go left/right based on values | Search both subtrees |
# | **Base Cases** | Just `None` check | `None` + `root == p or q` |
# | **Time Complexity** | O(h) | O(n) |
# | **Space Complexity** | O(h) | O(h) |

# ## Why the Regular Tree Solution is More General:
# 1. **No ordering**: Can't make decisions based on values
# 2. **Must search both sides**: Don't know which subtree contains the nodes
# 3. **Need to propagate found nodes upward**: Use return values to communicate

# ## Intuition Development:
# For **BST**: Think "navigation" - use values to decide direction.
# For **regular tree**: Think "search and report" - search everywhere and use return values to find where paths converge.

# Your BST intuition was correct! The regular tree version is actually more complex because you lose the helpful ordering property.a self.left = left
# #         self.right = right

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        
        if root.val == p.val or root.val == q.val:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        
        return left or right