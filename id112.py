class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        if not root.left and not root.right: 
            return targetSum == root.val

        l = self.hasPathSum(root.left, targetSum - root.val)
        r = self.hasPathSum(root.right, targetSum - root.val)

        return l or r