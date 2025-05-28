# Definition for a binary search tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val          # Value of the node
        self.left = left        # Left child
        self.right = right      # Right child

# Helper function to insert values into BST
def insert_into_bst(root, val):
    if not root:
        return TreeNode(val)    # If the tree is empty, create a new node
    if val < root.val:
        root.left = insert_into_bst(root.left, val)   # Insert into left subtree
    else:
        root.right = insert_into_bst(root.right, val) # Insert into right subtree
    return root

# Helper function to build a BST from a list of values
def build_bst(values):
    root = None
    for v in values:
        root = insert_into_bst(root, v)  # Insert each value into the BST
    return root

# Main function to find the kth smallest element in the BST
def kth_smallest(root, k):
    """Find kth smallest element in BST"""
    count = 0       # Counter to track the number of nodes visited
    result = None   # To store the kth smallest value once found

    # In-order traversal helper function (left -> root -> right)
    def inorder(node):
        nonlocal count, result
        if node is None or result is not None:
            return  # Stop if node is null or if we've already found the result

        inorder(node.left)   # Visit left subtree first

        count += 1           # Increment count after visiting a node
        if count == k:
            result = node.val  # Found the kth smallest node
            return

        inorder(node.right)  # Visit right subtree if needed

    inorder(root)            # Start in-order traversal from the root
    return result            # Return the result found


print(kth_smallest(build_bst([3, 1, 4, 2]), 2) == 2)  # 🎯 Second smallest
print(kth_smallest(build_bst([5, 3, 7, 2, 4, 6, 8]), 1) == 2)  # 📊 Minimum value
print(kth_smallest(build_bst([5, 3, 7, 2, 4, 6, 8]), 7) == 8)  # 📈 Maximum value
print(kth_smallest(build_bst([4, 2, 6, 1, 3, 5, 7]), 4) == 4)  # 🔗 Middle element
print(kth_smallest(build_bst([10]), 1) == 10)  # 🌱 Single node
