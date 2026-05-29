# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True]

        def height(root):
            if not root:
                return 0
            
            l_height = height(root.left)
            if balanced[0] == False:
                return False

            r_height = height(root.right)

            if abs(l_height-r_height)>1:
                balanced[0] = False
                return False

            return max(l_height,r_height) + 1

        height(root)
        return balanced[0]