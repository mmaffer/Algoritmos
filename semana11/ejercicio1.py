class BinarySearchTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        # Insert a value into the BST
        if not self.root:
            self.root = BinarySearchTreeNode(val)
        else:
            self._insert(self.root, val)

    def _insert(self, node, val):
        # Recursive insertion in left or right subtree depending on value
        if val < node.val:
            if node.left:
                self._insert(node.left, val)
            else:
                node.left = BinarySearchTreeNode(val)
        else:
            if node.right:
                self._insert(node.right, val)
            else:
                node.right = BinarySearchTreeNode(val)

    def build_from_list(self, vals):
        # Builds the BST from a list by inserting values one by one
        for val in vals:
            self.insert(val)

    def range_query(self, min_val, max_val):
        """🎯 Find all values in the BST within the range [min_val, max_val]"""

        result = []  # List to store values within the range

        def inorder(node):
            if not node:
                return  # Base case: empty node, stop recursion

            # Only traverse left subtree if current node's value is greater than min_val
            # because smaller values are in the left subtree
            if node.val > min_val:
                inorder(node.left)

            # Add current node's value if it lies within the range
            if min_val <= node.val <= max_val:
                result.append(node.val)

            # Only traverse right subtree if current node's value is less than max_val
            # because larger values are in the right subtree
            if node.val < max_val:
                inorder(node.right)

        inorder(self.root)  # Start inorder traversal from root
        return result  # Return the list of values found


# 🧪 Test cases
def test_range_query():
    bst1 = BinarySearchTree()
    bst1.build_from_list([7, 3, 11, 1, 5, 9, 13])
    print("🧪 Test 1:", bst1.range_query(5, 10) == [5, 7, 9])  # ✅

    bst2 = BinarySearchTree()
    bst2.build_from_list([6, 4, 8, 2])
    print("🧪 Test 2:", bst2.range_query(1, 10) == [2, 4, 6, 8])  # ✅

    bst3 = BinarySearchTree()
    bst3.build_from_list([20, 10, 30])
    print("🧪 Test 3:", bst3.range_query(1, 5) == [])  # ✅

    bst4 = BinarySearchTree()
    bst4.build_from_list([15])
    print("🧪 Test 4:", bst4.range_query(10, 20) == [15])  # ✅

    bst5 = BinarySearchTree()
    bst5.build_from_list([15, 10, 20, 5, 25])
    print("🧪 Test 5:", bst5.range_query(10, 20) == [10, 15, 20])  # ✅

# 🚀 Run tests
test_range_query()
