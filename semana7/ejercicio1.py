# Definition of the TreeNode class and tree_height function with the original test cases translated to English

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def tree_height(node):
    """Calculate the height of a binary tree."""
    if node is None:
        return -1
    return 1 + max(tree_height(node.left), tree_height(node.right))


def test_tree_height():
    # Test Case 1: Right-skewed tree
    right_skewed = TreeNode(1)
    right_skewed.right = TreeNode(2)
    right_skewed.right.right = TreeNode(3)
    right_skewed.right.right.right = TreeNode(4)
    print(tree_height(right_skewed))  # Expected output: 3

    # Test Case 2: Tree with a large balanced structure
    balanced = TreeNode(1)
    balanced.left = TreeNode(2)
    balanced.right = TreeNode(3)
    balanced.left.left = TreeNode(4)
    balanced.left.right = TreeNode(5)
    balanced.right.left = TreeNode(6)
    balanced.right.right = TreeNode(7)
    balanced.left.left.left = TreeNode(8)
    balanced.left.left.right = TreeNode(9)
    print(tree_height(balanced))  # Expected output: 3

    # Test Case 3: Tree with only one child per node
    single_child = TreeNode(1)
    single_child.left = TreeNode(2)
    single_child.left.left = TreeNode(3)
    single_child.left.left.left = TreeNode(4)
    single_child.left.left.left.left = TreeNode(5)
    print(tree_height(single_child))  # Expected output: 4

# Run the tests
test_tree_height()