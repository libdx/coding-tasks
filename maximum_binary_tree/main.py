# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        
        max_num = max(nums)
        max_at = nums.index(max_num)
        
        node = TreeNode(max_num)
        node.left = self.constructMaximumBinaryTree(nums[:max_at])
        node.right = self.constructMaximumBinaryTree(nums[max_at + 1:])
        
        return node
        
