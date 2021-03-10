"""
You are given a binary tree. You need to write a function that can determine if
it is a valid binary search tree.

The rules for a valid binary search tree are:

- The node's left subtree only contains nodes with values less than the node's
value.
- The node's right subtree only contains nodes with values greater than the
node's value.
- Both the left and right subtrees must also be valid binary search trees.

Example 1:
Input:

    5
   / \
  3   7

Output: True

Example 2:
Input:

    10
   / \
  2   8
     / \
    6  12

Output: False
Explanation: The root node's value is 10 but its right child's value is 8.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_valid_BST(root):
    # Your code here
    if root.left is None and root.right is None:
        return True

    if root.left is not None:
        if root.value < root.left.value:
            return False

    if root.right is not None:
        if root.value > root.right.value:
            return False
    
    leftValid = is_valid_BST(root.left)
    rightValid = is_valid_BST(root.right)

    if (leftValid and rightValid):
        return True

rootValidTree = TreeNode(5)
rootValidTree.left = TreeNode(3)
rootValidTree.right = TreeNode(7)

rootInvalidTree = TreeNode(10)
rootInvalidTree.left = TreeNode(2)
rootInvalidTree.right = TreeNode(8)
rootInvalidTree.right.left = TreeNode(6)
rootInvalidTree.right.right = TreeNode(12)

print(is_valid_BST(rootValidTree))
print(is_valid_BST(rootInvalidTree))
