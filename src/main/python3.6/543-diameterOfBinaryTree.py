# -*- coding: UTF-8 -*-
# 开发团队： xx科技
# 开发人员： lee
# 创建时间： 3/10/20 11:08 AM
# 文件名称： 543-.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # 直径最大值
        self.max_diameter = 0

        def maxDepth(node):
            if not node: return 0
            # 左孩子为根的子树深度
            L = maxDepth(node.left)
            # 右孩子为根的子树深度
            R = maxDepth(node.right)
            self.max_diameter = max(self.max_diameter, L + R)
            # 返回该节点为根的子树深度
            return max(L, R) + 1

        maxDepth(root)
        return self.max_diameter


list = [1, 2, 3, 4, 5, 9, 7, 6, 8]
root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)
node9 = TreeNode(9)
root.left = node2
root.right = node3
node2.left = node4
node2.right = node5
node4.left = node9
node5.left = node7
node5.right = node6
node7.left = node8

solution = Solution()
print(solution.diameterOfBinaryTree(root))