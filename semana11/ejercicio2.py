# Clase para representar un nodo del árbol BST
class TreeNode:
    def __init__(self, value):
        self.value = value        # 📌 Valor del nodo
        self.left = None          # 👈 Referencia al subárbol izquierdo
        self.right = None         # 👉 Referencia al subárbol derecho

# Función que encuentra el Ancestro Común Más Bajo (LCA) en un BST
def find_lca(root, val1, val2):
    """Encuentra el ancestro común más bajo entre dos valores en un BST"""

    while root:  # 🔁 Mientras no lleguemos a un nodo nulo
        if val1 < root.value and val2 < root.value:
            root = root.left     # 👈 Si ambos valores son menores, ir a la izquierda
        elif val1 > root.value and val2 > root.value:
            root = root.right    # 👉 Si ambos valores son mayores, ir a la derecha
        else:
            return root.value    # 🎯 Si están en lados opuestos o uno es el actual, este es el LCA

# Función para construir un árbol binario de búsqueda (BST) a partir de una lista
def build_bst(values):
    """Construye un BST a partir de una lista de valores"""
    def insert(root, val):
        if not root:                         # Si el nodo actual está vacío
            return TreeNode(val)             # Crea un nuevo nodo con el valor
        if val < root.value:                 # Si el valor es menor, insertamos a la izquierda
            root.left = insert(root.left, val)
        else:                                # Si el valor es mayor o igual, insertamos a la derecha
            root.right = insert(root.right, val)
        return root                          # Retorna la raíz después de insertar

    root = None                              # Inicializa el árbol vacío
    for v in values:
        root = insert(root, v)               # Inserta cada valor en el árbol
    return root                              # Retorna el árbol completo construido

# ✅ Test cases
# Test 1: Values in different subtrees
# BST: [6, 2, 8, 0, 4, 7, 9, 3, 5]
# Values: 2, 8
# Expected: 6
print(find_lca(build_bst([6, 2, 8, 0, 4, 7, 9, 3, 5]), 2, 8) == 6)  # 🌲 Root as LCA

# Test 2: Values in same subtree
# BST: [6, 2, 8, 0, 4, 7, 9, 3, 5]
# Values: 0, 4
# Expected: 2
print(find_lca(build_bst([6, 2, 8, 0, 4, 7, 9, 3, 5]), 0, 4) == 2)  # 📊 Subtree LCA

# Test 3: One value is ancestor of other
# BST: [6, 2, 8, 0, 4, 7, 9, 3, 5]
# Values: 2, 3
# Expected: 2
print(find_lca(build_bst([6, 2, 8, 0, 4, 7, 9, 3, 5]), 2, 3) == 2)  # 🔗 Ancestor relationship

# Test 4: Same values
# BST: [5, 3, 7]
# Values: 5, 5
# Expected: 5
print(find_lca(build_bst([5, 3, 7]), 5, 5) == 5)  # 🎯 Same node

# Test 5: Values at leaf level
# BST: [4, 2, 6, 1, 3, 5, 7]
# Values: 1, 3
# Expected: 2
print(find_lca(build_bst([4, 2, 6, 1, 3, 5, 7]), 1, 3) == 2)  # 🌱 Leaf nodes
