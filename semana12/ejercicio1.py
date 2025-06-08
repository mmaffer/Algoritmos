# Node class representing each node in the AVL Tree
class Node:
    def __init__(self, key):
        self.key = key       # Value of the node
        self.left = None     # Left child
        self.right = None    # Right child
        self.height = 1      # Height of the node (leaf nodes start at height 1)

# AVL Tree class that handles insertion and balancing
class AVLTree:

    # Helper function to get the height of a node
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    # Helper function to get the balance factor of a node
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # Right rotation (used in LL and LR cases)
    def rotate_right(self, y):
        x = y.left              # x becomes new root of subtree
        T2 = x.right            # store the subtree

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x  # return new root

    # Left rotation (used in RR and RL cases)
    def rotate_left(self, x):
        y = x.right             # y becomes new root of subtree
        T2 = y.left             # store the subtree

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y  # return new root

    # Recursive insert method with automatic balancing
    def insert(self, root, key):
        # Step 1: Perform normal BST insertion
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Step 2: Update the height of the ancestor node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Step 3: Get the balance factor to check if node is unbalanced
        balance = self.get_balance(root)

        # Step 4: Apply AVL rotations to balance the tree

        # Case 1 - Left Left (LL Rotation)
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)

        # Case 2 - Right Right (RR Rotation)
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)

        # Case 3 - Left Right (LR Rotation)
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # Case 4 - Right Left (RL Rotation)
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        # If the node is balanced, return it unchanged
        return root

    # Utility to check if the tree is balanced (used in testing)
    def is_balanced(self, root):
        if root is None:
            return True

        balance = self.get_balance(root)

        if abs(balance) > 1:
            return False

        return self.is_balanced(root.left) and self.is_balanced(root.right)

# ----------------------------
# ✅ Test Cases
# ----------------------------

# Function to test AVL Tree insertion and balance
def test_avl_insert():
    tree = AVLTree()

    # RR Rotation: Inserting [10, 20, 30]
    root = None
    for key in [10, 20, 30]:
        root = tree.insert(root, key)
    print(tree.is_balanced(root))  # True

    # LL Rotation: Inserting [30, 20, 10]
    root = None
    for key in [30, 20, 10]:
        root = tree.insert(root, key)
    print(tree.is_balanced(root))  # True

    # LR Rotation: Inserting [30, 10, 20]
    root = None
    for key in [30, 10, 20]:
        root = tree.insert(root, key)
    print(tree.is_balanced(root))  # True

    # RL Rotation: Inserting [10, 30, 20]
    root = None
    for key in [10, 30, 20]:
        root = tree.insert(root, key)
    print(tree.is_balanced(root))  # True

    # No rotation needed: Inserting [15, 10, 20, 25, 30]
    root = None
    for key in [15, 10, 20, 25, 30]:
        root = tree.insert(root, key)
    print(tree.is_balanced(root))  # True

# Run all test cases
test_avl_insert()
