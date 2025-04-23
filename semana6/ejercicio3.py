import random

class SimpleQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)  # agrega al final

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)  # quita del frente

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)

class TrafficLane:
    def __init__(self, name):
        self.name = name
        self.queue = SimpleQueue()
        self.wait_times = []
        self.max_length = 0

    def add_vehicle(self, arrival_time):
        self.queue.enqueue(arrival_time)
        self.max_length = max(self.max_length, len(self.queue))

    def pass_vehicle(self, current_time):
        arrival = self.queue.dequeue()
        if arrival is not None:
            wait_time = current_time - arrival
            self.wait_times.append(wait_time)
            print(f"{self.name}: Passed after {wait_time} units")

    def get_average_wait(self):
        return sum(self.wait_times) / len(self.wait_times) if self.wait_times else 0

    def get_max_length(self):
        return self.max_length

class TrafficLightSimulation:
    def __init__(self, green_duration, total_time=10):
        self.north_south = TrafficLane("North-South")
        self.east_west = TrafficLane("East-West")
        self.green_duration = green_duration
        self.total_time = total_time

    def simulate(self):
        for time in range(self.total_time):
            print(f"\nTime: {time}")

            if random.random() < 0.5:
                self.north_south.add_vehicle(time)
                print("Arrived at North-South")
            if random.random() < 0.5:
                self.east_west.add_vehicle(time)
                print("Arrived at East-West")

            if (time // self.green_duration) % 2 == 0:
                print("Green: North-South")
                self.north_south.pass_vehicle(time)
            else:
                print("Green: East-West")
                self.east_west.pass_vehicle(time)

        print("\nResults:")
        print(f"North-South - Avg Wait: {self.north_south.get_average_wait():.2f}   , Max Queue: {self.north_south.get_max_length()}")
        print(f"East-West   - Avg Wait: {self.east_west.get_average_wait():.2f}, Max Queue: {self.east_west.get_max_length()}")

# ✅ Test run
sim = TrafficLightSimulation(green_duration=3, total_time=4)
sim.simulate()
