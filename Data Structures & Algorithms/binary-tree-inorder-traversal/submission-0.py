# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs(node, res):
    if node is None:
        return
    dfs(node.left, res)
    res.append(node.val)
    dfs(node.right, res)

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        dfs(root, res)
        return res