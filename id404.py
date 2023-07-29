class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def is_leaf(node):
            return node is not None and node.left is None and node.right is None
        
        def leftnode(node):
            if node is None:
                return 0
            
            sum_left = leftnode(node.left)
            sum_right = leftnode(node.right)
            
            if is_leaf(node.left):
                return node.left.val + sum_left + sum_right
            
            return sum_left + sum_right
        
        return leftnode(root)