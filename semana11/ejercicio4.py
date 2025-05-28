class BinarySearchTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = BinarySearchTreeNode(val)
        else:
            self._insert(self.root, val)

    def _insert(self, node, val):
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
        for val in vals:
            self.insert(val)

    def kth_smallest(self, k):
        """📊 Find the kth smallest value in the BST"""

        self.count = 0       # To count how many nodes visited so far
        self.result = None   # To store kth smallest when found

        def inorder(node):
            if not node or self.result is not None:
                return  # Stop if node is None or kth smallest found

            inorder(node.left)  # Traverse left subtree

            self.count += 1     # Visit current node
            if self.count == k:  # Check if current is kth smallest
                self.result = node.val
                return

            inorder(node.right)  # Traverse right subtree

        inorder(self.root)
        return self.result


# 🧪 Test cases
def test_kth_smallest():
    bst1 = BinarySearchTree()
    bst1.build_from_list([3, 1, 4, 2])
    print("🧪 Test 1:", bst1.kth_smallest(2) == 2)  # 🎯

    bst2 = BinarySearchTree()
    bst2.build_from_list([5, 3, 7, 2, 4, 6, 8])
    print("🧪 Test 2:", bst2.kth_smallest(1) == 2)  # 📉 First (min)

    print("🧪 Test 3:", bst2.kth_smallest(7) == 8)  # 📈 Last (max)

    bst3 = BinarySearchTree()
    bst3.build_from_list([4, 2, 6, 1, 3, 5, 7])
    print("🧪 Test 4:", bst3.kth_smallest(4) == 4)  # 🔗 Middle

    bst4 = BinarySearchTree()
    bst4.build_from_list([10])
    print("🧪 Test 5:", bst4.kth_smallest(1) == 10)  # 🌱 Single node

# 🚀 Run tests
test_kth_smallest()
