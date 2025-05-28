class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # Initialize a tree node with a value, and optional left and right children
        self.val = val
        self.left = left
        self.right = right

def insert_into_bst(root, val):
    # Insert a value into the BST and return the (possibly new) root
    if not root:
        # If current node is empty, create a new node with val
        return TreeNode(val)
    if val < root.val:
        # If val is less than current node, insert into left subtree
        root.left = insert_into_bst(root.left, val)
    else:
        # Otherwise, insert into right subtree
        root.right = insert_into_bst(root.right, val)
    return root

def build_bst(values):
    # Build a BST by inserting values one by one
    root = None
    for v in values:
        root = insert_into_bst(root, v)
    return root

def range_query(root, min_val, max_val):
    """Find all values in BST within the given range [min_val, max_val]"""
    result = []

    def inorder(node):
        if not node:
            # Base case: if node is None, return immediately
            return
        # If current node's value is greater than min_val, explore left subtree
        if node.val > min_val:
            inorder(node.left)
        # If current node's value is within [min_val, max_val], add it to result
        if min_val <= node.val <= max_val:
            result.append(node.val)
        # If current node's value is less than max_val, explore right subtree
        if node.val < max_val:
            inorder(node.right)

    inorder(root)
    return result

# ✅ Test cases to verify correctness
print(range_query(build_bst([7, 3, 11, 1, 5, 9, 13]), 5, 10) == [5, 7, 9])  # True: Normal range
print(range_query(build_bst([6, 4, 8, 2]), 1, 10) == [2, 4, 6, 8])          # True: Full range
print(range_query(build_bst([20, 10, 30]), 1, 5) == [])                     # True: No values in range
print(range_query(build_bst([15]), 10, 20) == [15])                         # True: Single node in range
print(range_query(build_bst([15, 10, 20, 5, 25]), 10, 20) == [10, 15, 20]) # True: Include boundaries
