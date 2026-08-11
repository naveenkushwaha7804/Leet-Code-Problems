# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        if not root:
            return []
        Queue = deque([root])
        result = []
        while Queue:
            level = []
            for i in range(len(Queue)):
                node = Queue.popleft()
                level.append(node.val)
                if node.left:
                   Queue.append(node.left)
                if node.right:
                   Queue.append(node.right)
            result.append(level)
        return result[::-1]
            
        