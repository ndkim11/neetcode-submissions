# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = [root]

        def search(root):
            # if root is None
            if not root: 
                return

            lca[0] = root
            # p or q is the common root
            if p is root or q is root:
                return

            # p,q is right of root
            if root.val < p.val and root.val < q.val:
                return search(root.right)

            if root.val > p.val and root.val > q.val:
                return search(root.left)

            # p < root < q or vis-versa
            else:
                return

        search(root)

        return lca[0]