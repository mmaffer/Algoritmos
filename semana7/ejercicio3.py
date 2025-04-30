# Definition of the TreeNode class
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
# Function to mirror the binary tree
def mirror_tree(node):
    """Mirror a binary tree by recursively swapping left and right children."""
    if node is None:
        return None

    # Recursively mirror right and left subtrees
    left_mirrored = mirror_tree(node.right)
    right_mirrored = mirror_tree(node.left)
    node.left = left_mirrored
    node.right = right_mirrored
    return node

# Function for inorder traversal (Left - Data - Right)
def inorder_traversal(node):
    """Return in-order traversal of the tree as a list."""
    if node is None:
        return []
    return inorder_traversal(node.left) + [node.value] + inorder_traversal(node.right)


# Test cases for mirror_tree function
def test_mirror_tree():
    # Test Case 1: Normal tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print("Test Case 1 - Normal Tree")
    print("Original inorder:", inorder_traversal(root))  # [4, 2, 5, 1, 3]
    mirror_tree(root)
    print("Mirrored inorder:", inorder_traversal(root))  # [3, 1, 5, 2, 4]
    print()

    # Test Case 2: Empty tree
    empty_tree = None
    print("Test Case 2 - Empty Tree")
    mirrored_empty = mirror_tree(empty_tree)
    print("Mirrored inorder:", inorder_traversal(mirrored_empty))  # []
    print()

    # Test Case 3: Single node tree
    single_node = TreeNode(10)
    print("Test Case 3 - Single Node")
    print("Original inorder:", inorder_traversal(single_node))  # [10]
    mirror_tree(single_node)
    print("Mirrored inorder:", inorder_traversal(single_node))  # [10]
    print()

# Run all test cases
test_mirror_tree()
