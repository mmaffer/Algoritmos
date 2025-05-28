# ✅ Clase Node con encapsulamiento
class _Node:
    def __init__(self, value):
        self.__value = value          # 🔐 Valor del nodo (privado)
        self.__left = None            # 🔐 Hijo izquierdo (privado)
        self.__right = None           # 🔐 Hijo derecho (privado)

    def get_value(self):
        return self.__value           # ✅ Devuelve el valor del nodo

    def get_left(self):
        return self.__left            # ✅ Devuelve el hijo izquierdo

    def get_right(self):
        return self.__right           # ✅ Devuelve el hijo derecho

    def set_left(self, node):
        self.__left = node           # ✅ Asigna un nuevo hijo izquierdo

    def set_right(self, node):
        self.__right = node          # ✅ Asigna un nuevo hijo derecho


# ✅ Clase BinarySearchTree con encapsulamiento
class BinarySearchTree:
    def __init__(self):
        self.__root = None           # 🔐 Raíz del árbol (privado)

    def insert(self, value):
        if self.__root is None:
            self.__root = _Node(value)         # 🌱 Si el árbol está vacío, insertamos en la raíz
        else:
            self.__insert(self.__root, value)  # 🔁 Llamada recursiva para insertar en la posición correcta

    def __insert(self, node, value):
        if value < node.get_value():                     # 👈 Si el valor es menor, va al subárbol izquierdo
            if node.get_left() is None:
                node.set_left(_Node(value))              # 🌿 Insertamos como nuevo hijo izquierdo
            else:
                self.__insert(node.get_left(), value)    # 🔁 Repetimos con el hijo izquierdo
        else:
            if node.get_right() is None:
                node.set_right(_Node(value))             # 🌿 Insertamos como nuevo hijo derecho
            else:
                self.__insert(node.get_right(), value)   # 🔁 Repetimos con el hijo derecho

    def build_from_list(self, values):
        for val in values:
            self.insert(val)           # 🔁 Inserta cada valor de la lista en el árbol

    # ✅ Challenge 2: Lowest Common Ancestor
    def find_lca(self, val1, val2):
        """
        🧬 Encuentra el ancestro común más bajo (Lowest Common Ancestor) de dos valores en el BST

        Ejemplo cotidiano: Imagínate que val1 y val2 son dos personas de una familia.
        Este método busca cuál es su ancestro en común más cercano, como si fuera su abuelo más directo en un árbol genealógico.
        """
        node = self.__root  # 👨‍👧 Punto de partida desde la raíz del árbol

        while node:  # 🔁 Mientras existan nodos por explorar
            val = node.get_value()  # 📌 Obtenemos el valor del nodo actual

            if val1 < val and val2 < val:
                node = node.get_left()  # 👈 Ambos valores están en el subárbol izquierdo
            elif val1 > val and val2 > val:
                node = node.get_right() # 👉 Ambos valores están en el subárbol derecho
            else:
                return val  # 🎯 Si están en lados distintos o uno es igual al nodo actual, este es el LCA

        return None  # ❌ No se encontró (caso raro si los valores están en el árbol)


# ✅ Función validadora para lista doblemente enlazada circular

def validate_circular_dll(head, expected_values):
    if not head:
        return expected_values == []  # 📭 Si la lista está vacía, debe coincidir con lista vacía esperada
    values = []
    current = head
    while True:
        values.append(current.get_value())         # 📥 Guardamos el valor actual
        current = current.get_right()              # ➡️ Avanzamos al siguiente
        if current == head:
            break                                  # 🔁 Si volvemos al inicio, se completa el ciclo
    return values == expected_values               # ✅ Comparamos con los valores esperados


# ✅ Función auxiliar para crear un árbol desde una lista

def build_bst(values):
    bst = BinarySearchTree()           # 🌳 Creamos una nueva instancia de árbol
    bst.build_from_list(values)       # 🧱 Construimos el árbol desde la lista
    return bst                         # 🔁 Lo retornamos para usarlo en pruebas


# ✅ Casos de prueba para el Challenge 2 (Lowest Common Ancestor)
print("Test 1:", build_bst([6, 2, 8, 0, 4, 7, 9, 3, 5]).find_lca(2, 8) == 6)  # 🌲 Raíz como LCA
print("Test 2:", build_bst([6, 2, 8, 0, 4, 7, 9, 3, 5]).find_lca(0, 4) == 2)  # 📊 Subárbol izquierdo como LCA
print("Test 3:", build_bst([6, 2, 8, 0, 4, 7, 9, 3, 5]).find_lca(2, 3) == 2)  # 🔗 Uno es ancestro directo del otro
print("Test 4:", build_bst([5, 3, 7]).find_lca(5, 5) == 5)                    # 🎯 Mismo nodo como LCA
print("Test 5:", build_bst([4, 2, 6, 1, 3, 5, 7]).find_lca(1, 3) == 2)         # 🌱 Hojas con ancestro común
