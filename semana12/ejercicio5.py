# 🌱 Clase para nodos del árbol AVL
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

# 🌳 Clase para el árbol AVL
class AVLTree:
    def get_height(self, node):
        return node.height if node else 0

    def insert(self, root, key):
        if not root:
            return AVLNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_height(root.left) - self.get_height(root.right)

        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

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

    def print_level_order(self, root):
        if not root:
            return

        queue = [root]  # ✅ usamos una lista en lugar de deque
        while queue:
            level_size = len(queue)
            level = []
            for i in range(level_size):
                node = queue.pop(0)  # 👈 quitamos el primero como una cola
                level.append(f"{node.key}(h{node.height})")
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print(" ".join(level))

# 🧪 Test cases
def test_level_order_heights():
    avl = AVLTree()

    # ✅ Test 1: Árbol con 3 niveles
    root = None
    for val in [10, 5, 15, 2, 7]:
        root = avl.insert(root, val)
    print(" Test 1:")
    avl.print_level_order(root)

    # ✅ Test 2: Árbol con 1 nodo
    root = avl.insert(None, 42)
    print("\n Test 2:")
    avl.print_level_order(root)

    # ✅ Test 3: Inserciones que causan rotaciones
    root = None
    for val in [1, 2, 3, 4]:
        root = avl.insert(root, val)
    print("\n Test 3:")
    avl.print_level_order(root)

# 🚀 Ejecutar pruebas
test_level_order_heights()
