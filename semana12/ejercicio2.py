class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def get_height(self, node):
        return node.height if node else 0

    def rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def rotate_right(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y


def test_rotations():
    tree = AVLTree()

    # ✅ Test 1: Left Rotation on [10, 20, 30]
    z = AVLNode(10)
    z.right = AVLNode(20)
    z.right.right = AVLNode(30)
    z = tree.rotate_left(z)
    print(" Test 1:", z.key == 20)  # Expected: True

    # ✅ Test 2: Right Rotation on [30, 20, 10]
    z = AVLNode(30)
    z.left = AVLNode(20)
    z.left.left = AVLNode(10)
    z = tree.rotate_right(z)
    print(" Test 2:", z.key == 20)  # Expected: True

    # ✅ Test 3: Heights after left rotation
    z = AVLNode(5)
    z.right = AVLNode(10)
    z.right.right = AVLNode(15)
    z = tree.rotate_left(z)
    print(" Test 3:", z.height == 2 and z.left.height == 1 and z.right.height == 1)  # Expected: True

test_rotations()
