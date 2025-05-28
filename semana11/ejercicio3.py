# Define a class to represent each node in the binary tree
class TreeNode:
    # Constructor initializes the node with a value and optional left and right children
    def __init__(self, val, left=None, right=None):
        self.val = val      # Store the node's value
        self.left = left    # Reference to the left child node
        self.right = right  # Reference to the right child node

# Function to determine whether a binary tree is a valid BST
def is_valid_bst(root):
    # Inner helper function that validates the tree using a range [low, high]
    def validate(node, low=float('-inf'), high=float('inf')):
        if not node:
            return True  # An empty node is valid by definition
        
        # Check if the current node's value violates the BST rules
        if not (low < node.val < high):
            return False
        
        # Recursively validate left and right subtrees with updated bounds
        return (validate(node.left, low, node.val) and
                validate(node.right, node.val, high))

    # Start validation from the root with initial full range
    return validate(root)

# Function to build a binary tree from a list of values (level-order insertion)
def build_tree(values):
    if not values:
        return None  # Return None for an empty list
    
    # Create list of TreeNode objects or None based on values
    nodes = [TreeNode(val) if val is not None else None for val in values]
    child_idx = 1  # Index to keep track of children to assign
    
    # Loop through each node and assign left and right children
    for i in range(len(nodes)):
        if nodes[i] is not None:
            if child_idx < len(nodes):
                nodes[i].left = nodes[child_idx]
                child_idx += 1
            if child_idx < len(nodes):
                nodes[i].right = nodes[child_idx]
                child_idx += 1

    return nodes[0]  # Return the root node of the tree

# Function to build an invalid BST where the left child is greater than the root
def build_invalid_tree1():
    # Manually build a tree:
    #     5
    #    / \
    #   6   7   <-- Invalid BST: 6 is on the left but greater than 5
    root = TreeNode(5)
    root.left = TreeNode(6)
    root.right = TreeNode(7)
    return root

# Function to build an invalid BST where the right child is less than the root
def build_invalid_tree2():
    # Manually build a tree:
    #     5
    #    / \
    #   3   4   <-- Invalid BST: 4 is on the right but less than 5
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(4)
    return root

# ✅ Test cases
# Test 1: Valid BST
# Tree:    5
#         / \
#        3   7
#       / \ / \
#      2  4 6  8
print(is_valid_bst(build_tree([5, 3, 7, 2, 4, 6, 8])) == True)  # ✅ Valid BST

# Test 2: Invalid BST - left violation
# Tree:    5
#         / \
#        6   7  (6 > 5, violates BST)
print(is_valid_bst(build_invalid_tree1()) == False)  # ❌ Left violation

# Test 3: Invalid BST - right violation
# Tree:    5
#         / \
#        3   4  (4 < 5, violates BST)
print(is_valid_bst(build_invalid_tree2()) == False)  # ❌ Right violation

# Test 4: Single node
# Tree: 42
print(is_valid_bst(build_tree([42])) == True)  # 🌱 Single node valid

# Test 5: Empty tree
# Tree: None
print(is_valid_bst(None) == True)  # 📭 Empty tree valid

