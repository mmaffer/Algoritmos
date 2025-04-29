class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
def count_leaves(node):
    if node is None:
        return 0  # Árbol vacío o subárbol nulo
    
    if node.left is None and node.right is None:
        return 1  # Es una hoja
    
    # Llamada recursiva a izquierda y derecha
    return count_leaves(node.left) + count_leaves(node.right)



def test_count_leaves():
    # Test Case 1: Árbol con solo hijos izquierdos
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.left.left = TreeNode(3)
    root4.left.left.left = TreeNode(4)
    resultado4 = count_leaves(root4) #oupt
    print(resultado4) #Expected output: 1

    # Test Case 2: Árbol con solo hijos derechos
    root5 = TreeNode(1)
    root5.right = TreeNode(2)
    root5.right.right = TreeNode(3)
    root5.right.right.right = TreeNode(4)
    resultado5 = count_leaves(root5)
    print(resultado5) #Expected output: 1

    # Test Case 3: Árbol lleno hasta el segundo nivel
    root6 = TreeNode(1)
    root6.left = TreeNode(2)
    root6.right = TreeNode(3)
    root6.left.left = TreeNode(4)
    root6.left.right = TreeNode(5)
    root6.right.left = TreeNode(6)
    root6.right.right = TreeNode(7)
    resultado6 = count_leaves(root6)
    print(resultado6) #Expected output: 4

# Ejecutar tests con resultados visibles
test_count_leaves()