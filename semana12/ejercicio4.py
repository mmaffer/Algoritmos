class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # not strictly needed here but usual in AVL nodes

class AVLTree:
    def is_avl_balanced(self, root):
        """Check if the tree rooted at root is AVL balanced"""

        def check(node):
            # Base case: empty subtree
            if not node:
                return True, 0  # balanced, height 0

            # Check left subtree
            left_balanced, left_height = check(node.left)
            if not left_balanced:
                return False, 0  # no need to continue if left subtree is unbalanced

            # Check right subtree
            right_balanced, right_height = check(node.right)
            if not right_balanced:
                return False, 0  # no need to continue if right subtree is unbalanced

            # Compute current node balance factor
            balance = left_height - right_height

            # Check if current node is balanced
            if balance < -1 or balance > 1:
                return False, 0

            # Height of current node is max of children plus one
            current_height = 1 + max(left_height, right_height)

            return True, current_height

        balanced, _ = check(root)
        return balanced


# --- Test cases ---

def test_is_avl_balanced():
    avl = AVLTree()

    # Helper insert method to build tree for tests
    def insert(node, key):
        if not node:
            return AVLNode(key)
        if key < node.key:
            node.left = insert(node.left, key)
        else:
            node.right = insert(node.right, key)
        return node

    avl.insert = insert  # quick patch for insert to build trees

    root = None
    for val in [20, 10, 30]:
        root = avl.insert(root, val)
    print("🧪 Test 1:", avl.is_avl_balanced(root) == True)  # Balanced tree

    # Manually create unbalanced tree (right-right heavy)
    unbalanced = AVLNode(10)
    unbalanced.right = AVLNode(20)
    unbalanced.right.right = AVLNode(30)
    print("🧪 Test 2:", avl.is_avl_balanced(unbalanced) == False)  # Not balanced

    # Empty tree is balanced
    print("🧪 Test 3:", avl.is_avl_balanced(None) == True)

    # Deep imbalance example
    deep_unbalanced = AVLNode(10)
    deep_unbalanced.left = AVLNode(5)
    deep_unbalanced.left.left = AVLNode(2)
    deep_unbalanced.left.left.left = AVLNode(1)
    print("🧪 Test 4:", avl.is_avl_balanced(deep_unbalanced) == False)

    # Larger balanced tree
    root2 = None
    for val in [40, 20, 60, 10, 30, 50, 70]:
        root2 = avl.insert(root2, val)
    print("🧪 Test 5:", avl.is_avl_balanced(root2) == True)


test_is_avl_balanced()
