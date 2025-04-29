# Definition of the TreeNode class and mirror_tree function with test cases in English
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def mirror_tree(node):
    """Mirror a binary tree by swapping left and right children of every node."""
    if node is None:
        return None

    # Recursively mirror left and right subtrees
    left_mirrored = mirror_tree(node.right)
    right_mirrored = mirror_tree(node.left)
    node.left = left_mirrored
    node.right = right_mirrored
    return node

def inorder_traversal(node):
    """In-order traversal to verify the structure of the mirrored tree."""
    if node is None:
        return []
    return inorder_traversal(node.left) + [node.value] + inorder_traversal(node.right)


def test_mirror_tree():
    # Test Case 1: Normal binary tree
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    print("Before mirroring:", inorder_traversal(root1))  # [4, 2, 5, 1, 3]
    mirror_tree(root1)
    print("After mirroring:", inorder_traversal(root1))   # [3, 1, 5, 2, 4]

    # Test Case 2: Single node tree
    root2 = TreeNode(42)
    print("Before mirroring:", inorder_traversal(root2))  # [42]
    mirror_tree(root2)
    print("After mirroring:", inorder_traversal(root2))   # [42]

    # Test Case 3: Empty tree
    root3 = None
    mirrored = mirror_tree(root3)
    print("After mirroring:", inorder_traversal(mirrored))  # []

# Run the tests
test_mirror_tree()
