# Definition for a binary tree node.
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def minValue(root):
    if root.left is None:
        return root.value
    else:
        return minValue(root.left)

def findInorderSucc(root, node):
    if node.right is not None:
        return minValue(node.right)
    else:
        if root.value == node.value:
            return None

        if node.value > root.value:
            return findInorderSucc(root.right, node)
        elif node.value < root.value:
            return findInorderSucc(root.left, node)
        else:
            # Root and node's value are equal
            return None


root = TreeNode(20)

root.left = TreeNode(8)
root.right = TreeNode(22)

root.left.left = TreeNode(4)
root.left.right = TreeNode(12)

root.left.right.left = TreeNode(10)
root.left.right.right = TreeNode(14)


print(minValue(root))
print(findInorderSucc(root, root.left.right.right))
