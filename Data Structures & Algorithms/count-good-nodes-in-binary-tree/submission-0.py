# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        numGood = 0
        # Make a stack and push nodes and maxVal until that point 
        # in each path DFS
        stack = [[root,root.val]]

        while stack:
            node, maxVal = stack.pop()

            if node.val >= maxVal: # Update maximum value
                maxVal = node.val
                numGood += 1

            if node.left:
                stack.append([node.left, maxVal])
            if node.right:
                stack.append([node.right, maxVal])

        return numGood