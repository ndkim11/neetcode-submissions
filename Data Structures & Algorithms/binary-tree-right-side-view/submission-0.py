# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Use BFS and pick the right most elements
        q = deque()
        rightEle = []
        # If root exists push into queue
        if root:
            q.append(root)

            # While queue is not empty
            while q:
                # valLevel = 0
                # For all elements in current level
                for i in range(len(q)):
                    node = q.popleft()
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                    
                rightEle.append(node.val)

            return rightEle
        
        return []