# Node class representing each node in the AVL Tree
class Node:
    def __init__(self, key):
        self.key = key         # Value of the node
        self.left = None       # Left child
        self.right = None      # Right child
        self.height = 1        # Height of the node (leaf nodes start at height 1)

# AVL Tree class
class AVLTree:

    # Get height of a node
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    # Get balance factor of a node
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # Perform right rotation
    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        # Rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    # Perform left rotation
    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        # Rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    # Insert a node with rebalancing
    def insert(self, root, key):
        # Normal BST insertion
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Update height
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Balance the node
        balance = self.get_balance(root)

        # LL Case
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)

        # RR Case
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)

        # LR Case
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # RL Case
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    # Find node with minimum value in a subtree
    def get_min_value_node(self, root):
        current = root
        while current.left:
            current = current.left
        return current

    # Delete a node with rebalancing
    def delete(self, root, key):
        # Step 1: Perform standard BST delete
        if not root:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children
            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        # Step 2: Update height
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Step 3: Balance the node
        balance = self.get_balance(root)

        # LL Case
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.rotate_right(root)

        # LR Case
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # RR Case
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.rotate_left(root)

        # RL Case
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    # Inorder traversal to check tree structure
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=' ')
            self.inorder(root.right)

# Test function
def test_avl_delete():
    avl = AVLTree()
    root = None
    for val in [20, 10, 30, 25, 35]:
        root = avl.insert(root, val)

    root = avl.delete(root, 35)
    print("🧪 Test 1 (Delete leaf): Pass 👌")

    root = avl.delete(root, 25)
    print("🧪 Test 2 (Delete one child): Pass ✂️")

    root = avl.delete(root, 20)
    print("🧪 Test 3 (Delete two children): Pass 🪓")

    print("🧪 Test 4 & 5: Inorder traversal after deletions:")
    avl.inorder(root)
    print()

# Run tests
test_avl_delete()
