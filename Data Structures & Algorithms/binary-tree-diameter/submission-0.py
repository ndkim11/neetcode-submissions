# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter of subtree = depth(root.left) + depth(root.right)
        q = deque()
        max_diameter = [0]
        
        def depth(root):
            if root is None:
                return 0
            l_depth, r_depth = depth(root.left),depth(root.right)
            
            diameter = l_depth+r_depth
            max_diameter[0] = max(diameter, max_diameter[0])
            return max(l_depth, r_depth)+1

        depth(root)
        return max_diameter[0]