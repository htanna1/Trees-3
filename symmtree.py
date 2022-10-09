#time complexity: O(n) going th all the elements in worst case
#space complexity: o(1), only 1 extra variable
#passed all cases on LeetCode:yes
#difficulty faced:
# comments: in the code

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: 'Optional[TreeNode]') -> bool:

        self.issym = True

        def dfs(left,right):

            if left == None and right == None:
                return 
            if left == None or right == None or left.val != right.val:
                self.issym = False
                return 

        
            dfs(left.left,right.right)
            dfs(left.right,right.left)

        dfs(root.left,root.right)
        return self.issym
