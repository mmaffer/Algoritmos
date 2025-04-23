import random  

class SimpleQueue:
    def __init__(self):
        self.items = []  # Lista que almacenará los elementos en la cola

    def enqueue(self, item):
        self.items.append(item)  # Agrega un elemento al final de la cola

    def dequeue(self):
        if self.is_empty():
            return None  # Si la cola está vacía, no se puede sacar nada
        return self.items.pop(0)  

    def is_empty(self):
        return len(self.items) == 0  

    def __len__(self):
        return len(self.items)  # obtener el número de elementos

class TrafficLane:
    def __init__(self, name):
        self.name = name  # Nombre del carril
        self.queue = SimpleQueue()  # Cola asociada al carril
        self.wait_times = []  # Lista para guardar los tiempos de espera de los vehículos
        self.max_length = 0  # Valor máximo alcanzado por la longitud de la cola

    def add_vehicle(self, arrival_time):
        self.queue.enqueue(arrival_time)  # Añade un vehículo con su hora de llegada
        self.max_length = max(self.max_length, len(self.queue))  # Actualiza el tamaño máximo de la cola

    def pass_vehicle(self, current_time):
        arrival = self.queue.dequeue()  # Saca al primer vehículo en la cola
        if arrival is not None:
            wait_time = current_time - arrival  # Calcula el tiempo de espera
            self.wait_times.append(wait_time)  # Guarda el tiempo de espera
            print(f"{self.name}: Passed after {wait_time} units")  # Muestra en pantalla el paso del vehículo

    def get_average_wait(self):
        # Calcula y devuelve el promedio de espera
        return sum(self.wait_times) / len(self.wait_times) if self.wait_times else 0

    def get_max_length(self):
        return self.max_length  # Devuelve el tamaño máximo que tuvo la cola


class TrafficLightSimulation:
    def __init__(self, green_duration, total_time=10):
        self.north_south = TrafficLane("North-South")  # Carril Norte-Sur
        self.east_west = TrafficLane("East-West")  # Carril Este-Oeste
        self.green_duration = green_duration  # Tiempo que dura el semáforo en verde para cada dirección
        self.total_time = total_time  

    def simulate(self):
        for time in range(self.total_time):  # Recorre cada unidad de tiempo
            print(f"\nTime: {time}")  # Muestra el tiempo actual en la simulación

            # Con 50% de probabilidad, llega un vehículo a North-South
            if random.random() < 0.5:
                self.north_south.add_vehicle(time)
                print("Arrived at North-South")

            # Con 50% de probabilidad, llega un vehículo a East-West
            if random.random() < 0.5:
                self.east_west.add_vehicle(time)
                print("Arrived at East-West")

            # Alterna el semáforo: si se cumple la condición, es turno de North-South
            if (time // self.green_duration) % 2 == 0:
                print("Green: North-South")
                self.north_south.pass_vehicle(time)  # Vehículo de North-South puede pasar
            else:
                print("Green: East-West")
                self.east_west.pass_vehicle(time)  # Vehículo de East-West puede pasar

        # Muestra los resultados al final de la simulación
        print("\nResults:")
        print(f"North-South - Avg Wait: {self.north_south.get_average_wait():.2f}   , Max Queue: {self.north_south.get_max_length()}")
        print(f"East-West   - Avg Wait: {self.east_west.get_average_wait():.2f}, Max Queue: {self.east_west.get_max_length()}")

# Casos de prueba
sim = TrafficLightSimulation(green_duration=3, total_time=4)
sim.simulate()
