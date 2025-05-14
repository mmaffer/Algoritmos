# Clase que representa un nodo del árbol de expresión
class ExpressionNode:
    def __init__(self, value):
        self.value = value         # 📌 Almacena el valor del nodo (número, variable u operador)
        self.left = None           # 👈 Referencia al hijo izquierdo
        self.right = None          # 👉 Referencia al hijo derecho

# Clase principal que construye el árbol desde notación infija
class ExpressionTree:
    def __init__(self):
        self.root = None           # 🌱 Raíz del árbol

    @classmethod
    def from_infix(cls, tokens):
        """Construye el árbol de expresión a partir de tokens en notación infija"""

        # Función que define precedencia de operadores
        def precedence(op):
            if op in ('+', '-'):
                return 1           # + y - tienen menor precedencia
            if op in ('*', '/'):
                return 2           # * y / tienen mayor precedencia
            return 0               # Otros (por ejemplo, paréntesis)

        output = []                # Lista de salida en notación postfix
        stack = []                 # Pila para operadores

        # 🔄 Convertir infijo a postfix (algoritmo Shunting Yard)
        for token in tokens:
            if token.isalnum():    # Si es número o letra
                output.append(token)
            elif token == '(':
                stack.append(token)         # Paréntesis de apertura
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())  # Vaciar hasta encontrar (
                stack.pop()                     # Eliminar el '('
            else:
                while stack and precedence(stack[-1]) >= precedence(token):
                    output.append(stack.pop())  # Extraer operadores con mayor o igual precedencia
                stack.append(token)             # Agregar operador actual

        while stack:
            output.append(stack.pop())  # Agregar operadores restantes

        # 🌱 Construir árbol desde notación postfix
        stack = []
        for token in output:
            node = ExpressionNode(token)
            if token in '+-*/':           # Si es operador
                node.right = stack.pop()  # Extrae nodo derecho primero
                node.left = stack.pop()   # Luego el izquierdo
            stack.append(node)            # Agrega el nuevo subárbol a la pila

        tree = cls()                      # Crear instancia de árbol
        tree.root = stack[0]              # El último elemento es la raíz
        return tree                       # Retornar el árbol construido

# Test 1: 2 + 3
tree1 = ExpressionTree.from_infix(['2', '+', '3'])
print(tree1.root.value == '+' and tree1.root.left.value == '2' and tree1.root.right.value == '3')  # True

# Test 2: 2 + 3 * 4
tree2 = ExpressionTree.from_infix(['2', '+', '3', '*', '4'])
print(tree2.root.value == '+' and tree2.root.right.value == '*')  # True

# Test 3: (2 + 3) * 4
tree3 = ExpressionTree.from_infix(['(', '2', '+', '3', ')', '*', '4'])
print(tree3.root.value == '*' and tree3.root.left.value == '+')  # True