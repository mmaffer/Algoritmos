# Clase que representa un nodo de un árbol binario (también usado para la lista doble)
class TreeNode:
    def __init__(self, value):
        self.value = value        # 📌 Valor del nodo
        self.left = None          # ⬅️ En la lista: apuntará al nodo anterior
        self.right = None         # ➡️ En la lista: apuntará al nodo siguiente

# Función para construir un árbol binario de búsqueda (BST) a partir de una lista
def build_bst(values):
    """Construye un BST balanceado desde una lista"""

    # Función auxiliar recursiva para insertar un valor en el árbol
    def insert(root, val):
        if not root:                         # 🌱 Si el nodo actual está vacío
            return TreeNode(val)             # 🧱 Crea un nuevo nodo
        if val < root.value:                 # Si el valor es menor, va a la izquierda
            root.left = insert(root.left, val)
        else:                                # Si es mayor o igual, va a la derecha
            root.right = insert(root.right, val)
        return root                          # Retorna la raíz actualizada

    root = None                              # 🌳 Inicializa el árbol vacío
    for v in values:
        root = insert(root, v)               # Inserta cada valor en el árbol
    return root                              # Retorna el árbol construido

# Función para construir un árbol degenerado (solo ramas hacia la derecha)
def build_degenerate_bst(values):
    """Construye un BST degenerado (como una lista hacia la derecha)"""
    if not values:                           # Si la lista está vacía
        return None                          # Retorna árbol vacío
    root = TreeNode(values[0])               # 🌱 El primer valor es la raíz
    current = root
    for val in values[1:]:                   # Inserta cada valor a la derecha
        current.right = TreeNode(val)
        current = current.right
    return root                              # Retorna la raíz del árbol degenerado

# Función principal que convierte un BST en una lista doble circular
def bst_to_dll(root):
    """Convierte un BST en una lista doble circular ordenada"""

    def inorder(node):
        nonlocal last, head                  # Acceso a variables externas

        if not node:                         # 🛑 Si el nodo está vacío, termina
            return

        inorder(node.left)                   # 🔁 Visita el subárbol izquierdo

        if last:                             # Si ya hay un nodo visitado antes
            last.right = node                # ➡️ El último apunta al nodo actual
            node.left = last                 # ⬅️ El actual apunta al último
        else:
            head = node                      # 🌱 Si es el primero, se marca como cabeza

        last = node                          # 🔄 Actualiza el último nodo procesado

        inorder(node.right)                  # 🔁 Visita el subárbol derecho

    if not root:                             # Si el árbol está vacío
        return None                          # Retorna None
    

    head, last = None, None                  # Inicializa punteros globales
    inorder(root)                            # 🔁 Inicia recorrido in-order

    head.left = last                         # 🔁 Conecta la cabeza con la cola (circular)
    last.right = head

    return head                              # 🚪 Retorna el inicio de la lista circular

# Función para validar que la lista doble circular sea correcta
def validate_circular_dll(head, expected):
    if not head:                             # Si la cabeza es None
        return expected == []                # Retorna True si se esperaba lista vacía

    result = []                              # Lista para guardar recorrido
    node = head
    while True:
        result.append(node.value)            # Agrega el valor actual
        node = node.right                    # Mueve al siguiente nodo
        if node == head:                     # Si regresa al inicio, se detiene
            break
    return result == expected                # Compara con la lista esperada


# Test 1: BST con 3 nodos
dll1 = bst_to_dll(build_bst([2, 1, 3]))
print(validate_circular_dll(dll1, [1, 2, 3]))  # ✅ True

# Test 2: BST de un solo nodo
dll2 = bst_to_dll(build_bst([5]))
print(validate_circular_dll(dll2, [5]))        # ✅ True

# Test 3: Árbol vacío
dll3 = bst_to_dll(None)
print(dll3 is None)                            # ✅ True


# ✅ Test cases
# Test 1: Simple BST
# BST:   2        DLL: 1 <-> 2 <-> 3 (circular)
#       / \
#      1   3
head1 = bst_to_dll(build_bst([2, 1, 3]))
print(validate_circular_dll(head1, [1, 2, 3]) == True)  # 🔗 Simple conversion

# Test 2: Larger BST
# BST: [4, 2, 6, 1, 3, 5, 7]
# DLL: 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6 <-> 7 (circular)
head2 = bst_to_dll(build_bst([4, 2, 6, 1, 3, 5, 7]))
print(validate_circular_dll(head2, [1, 2, 3, 4, 5, 6, 7]) == True)  # 📊 Complex conversion

# Test 3: Single node
# BST: 5
# DLL: 5 (points to itself)
head3 = bst_to_dll(build_bst([5]))
print(validate_circular_dll(head3, [5]) == True)  # 🌱 Single node

# Test 4: Degenerate BST (like linked list)
# BST: 1 -> 2 -> 3 -> 4
# DLL: 1 <-> 2 <-> 3 <-> 4 (circular)
head4 = bst_to_dll(build_degenerate_bst([1, 2, 3, 4]))
print(validate_circular_dll(head4, [1, 2, 3, 4]) == True)  # 📈 Degenerate case

# Test 5: Empty tree
# BST: None
# DLL: None
head5 = bst_to_dll(None)
print(head5 is None)  # 📭 Empty tree
