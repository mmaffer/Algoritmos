# Implementación del Sliding Window Maximum SIN usar deque.
# En su lugar, crearemos una cola circular manual con una lista y dos punteros.

class ColaCircularMax:
    def __init__(self, tamaño):
        self.tamaño = tamaño
        self.cola = [0] * tamaño  # Guarda índices
        self.inicio = 0
        self.fin = 0
        self.count = 0

    def esta_vacia(self):
        return self.count == 0

    def esta_llena(self):
        return self.count == self.tamaño

    def agregar_final(self, valor):
        if not self.esta_llena():
            self.cola[self.fin] = valor
            self.fin = (self.fin + 1) % self.tamaño
            self.count += 1

    def quitar_inicio(self):
        if not self.esta_vacia():
            valor = self.cola[self.inicio]
            self.inicio = (self.inicio + 1) % self.tamaño
            self.count -= 1
            return valor

    def final_valor(self):
        return self.cola[(self.fin - 1 + self.tamaño) % self.tamaño]

    def frente_valor(self):
        return self.cola[self.inicio]

    def recorrer(self):
        res = []
        i = self.inicio
        for _ in range(self.count):
            res.append(self.cola[i])
            i = (i + 1) % self.tamaño
        return res

def sliding_window_max_sin_deque(nums, k):
    if not nums or k == 0:
        return []

    n = len(nums)
    maximos = []
    cola = ColaCircularMax(n)  # Cola circular del mismo tamaño que nums

    for i in range(n):
        # Quitar los índices fuera del rango de la ventana
        if not cola.esta_vacia() and cola.frente_valor() < i - k + 1:
            cola.quitar_inicio()

        # Quitar del final los elementos menores que nums[i]
        while not cola.esta_vacia() and nums[cola.final_valor()] < nums[i]:
            cola.fin = (cola.fin - 1 + cola.tamaño) % cola.tamaño
            cola.count -= 1

        # Agregar el índice actual
        cola.agregar_final(i)

        # Guardar el máximo si ya hay ventana completa
        if i >= k - 1:
            maximos.append(nums[cola.frente_valor()])

    return maximos

# Probar con el ejemplo dado
nums = [3,5,3,5,7,3,2,4]
k = 4
print(sliding_window_max_sin_deque(nums, k))