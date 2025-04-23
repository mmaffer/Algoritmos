class CircularBuffer:
    def __init__(self, size):
        self.buffer = [None] * size         # Arreglo fijo
        self.max_size = size                # Tamaño máximo del buffer
        self.start = 0                      # Índice de inicio (el más antiguo)
        self.count = 0                      # Número actual de elementos

    def add(self, value):
        # Calcula la posición donde insertar
        index = (self.start + self.count) % self.max_size
        if self.count == self.max_size:
            # El buffer está lleno: sobrescribe el dato más antiguo
            self.start = (self.start + 1) % self.max_size
        else:
            self.count += 1
        self.buffer[index] = value

    def get_latest(self):
        # Devuelve los elementos en orden correcto (más antiguos a más nuevos)
        result = []
        for i in range(self.count):
            index = (self.start + i) % self.max_size
            result.append(self.buffer[index])
        return result

    def calculate_average(self):
        # Calcula promedio ignorando valores None
        if self.count == 0:
            return 0
        return sum(self.get_latest()) / self.count


# =======================
# Prueba del CircularBuffer
# =======================

cb = CircularBuffer(5)

cb.add(10)
cb.add(20)
cb.add(30)
print(cb.get_latest())           # [10, 20, 30]
print(cb.calculate_average())    # 20.0

cb.add(40)
cb.add(50)
cb.add(60)  # Sobrescribe el 10
print(cb.get_latest())           # [20, 30, 40, 50, 60]
print(cb.calculate_average())    # 40.0

# --- Prueba 1: Buffer lleno, múltiples sobrescrituras ---
cb.add(70)
cb.add(80)
print(cb.get_latest())           # [40, 50, 60, 70, 80]
print(cb.calculate_average())    # 60.0

# --- Prueba 2: Buffer con solo 1 elemento ---
cb2 = CircularBuffer(3)
cb2.add(99)
print(cb2.get_latest())          # [99]
print(cb2.calculate_average())   # 99.0

# --- Prueba 3: Buffer vacío (sin agregar nada) ---
cb3 = CircularBuffer(4)
print(cb3.get_latest())          # []
print(cb3.calculate_average())   # 0