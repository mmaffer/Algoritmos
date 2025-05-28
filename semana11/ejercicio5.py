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

    # ✅ Challenge 5: Convertir BST a Lista Doblemente Enlazada Circular
    def bst_to_dll(self):
        """
        🔄 Convierte el BST en una lista doblemente enlazada circular en orden ascendente.

        Ejemplo cotidiano: Es como recorrer un álbum de fotos en orden y luego unir la primera y última foto para
        que puedas navegar infinitamente hacia adelante o hacia atrás.
        """
        if not self.__root:
            return None  # 📭 Si el árbol está vacío, devolvemos None

        self.__prev = None  # 🔁 Apuntador al nodo anterior en el recorrido
        self.__head = None  # 🎯 Referencia al primer nodo (inicio de la lista)

        def inorder(node):
            if not node:
                return
            inorder(node.get_left())  # ⬅️ Recorremos subárbol izquierdo primero

            if self.__prev:
                self.__prev.set_right(node)  # ➡️ Enlazamos nodo anterior con el actual (derecha)
                node.set_left(self.__prev)  # ⬅️ Enlazamos actual con el anterior (izquierda)
            else:
                self.__head = node  # 🎯 Guardamos el primer nodo como cabeza

            self.__prev = node  # 📌 Actualizamos el nodo anterior al actual

            inorder(node.get_right())  # ➡️ Recorremos subárbol derecho

        inorder(self.__root)  # 🚀 Iniciamos el recorrido inorden desde la raíz

        # 🔗 Cerramos la lista: conectamos cabeza y último nodo
        self.__head.set_left(self.__prev)
        self.__prev.set_right(self.__head)

        return self.__head  # 🎉 Retornamos el inicio de la lista circular


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


# ✅ Casos de prueba para Challenge 5 (Conversión a lista doblemente enlazada)
bst1 = build_bst([2, 1, 3])
head1 = bst1.bst_to_dll()
print("Test 1:", validate_circular_dll(head1, [1, 2, 3]))  # 🔗 Lista ordenada pequeña

bst2 = build_bst([4, 2, 6, 1, 3, 5, 7])
head2 = bst2.bst_to_dll()
print("Test 2:", validate_circular_dll(head2, [1, 2, 3, 4, 5, 6, 7]))  # 🌳 Lista completa

bst3 = build_bst([5])
head3 = bst3.bst_to_dll()
print("Test 3:", validate_circular_dll(head3, [5]))  # 🌱 Árbol con un solo nodo

bst4 = build_bst([1, 2, 3, 4])
head4 = bst4.bst_to_dll()
print("Test 4:", validate_circular_dll(head4, [1, 2, 3, 4]))  # 📈 Árbol degenerado tipo lista

bst5 = build_bst([])
head5 = bst5.bst_to_dll()
print("Test 5:", head5 is None)  # 📭 Árbol vacío