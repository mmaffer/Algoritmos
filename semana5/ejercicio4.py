from collections import deque


class Tarea:
    def __init__(self, nombre, tiempo, prioridad):
        self.nombre = nombre
        self.tiempo_restante = tiempo
        self.tiempo_total = tiempo
        self.prioridad = prioridad
        self.tiempo_espera = 0
        self.tiempo_respuesta = None


def programador_round_robin(tareas, quantum):
    cola = deque(sorted(tareas, key=lambda t: t.prioridad))  # Prioridad más baja = más urgente
    tiempo_actual = 0
    completadas = []


    while cola:
        tarea = cola.popleft()


        # Si es la primera vez que se ejecuta, calculamos el tiempo de respuesta
        if tarea.tiempo_respuesta is None:
            tarea.tiempo_respuesta = tiempo_actual
       


        tiempo_ejecucion = min(quantum, tarea.tiempo_restante)
        tarea.tiempo_restante -= tiempo_ejecucion
        tiempo_actual += tiempo_ejecucion


        # Aumentamos el tiempo de espera para otras tareas en la cola
        for t in cola:
            t.tiempo_espera += tiempo_ejecucion


        if tarea.tiempo_restante > 0:
            cola.append(tarea)
        else:
            completadas.append(tarea)


    # Cálculos finales
    tiempo_total = tiempo_actual
    promedio_espera = sum(t.tiempo_espera for t in completadas) / len(completadas)
    promedio_respuesta = sum(t.tiempo_respuesta for t in completadas) / len(completadas)


    print(f"Tiempo total de ejecución: {tiempo_total}")
    print(f"Tiempo promedio de espera: {promedio_espera:.2f}")
    print(f"Tiempo promedio de respuesta: {promedio_respuesta:.2f}")
    print("\nDetalles por tarea:")
    for t in completadas:
        print(f"Tarea {t.nombre}: Espera={t.tiempo_espera}, Respuesta={t.tiempo_respuesta}, Duración={t.tiempo_total}")


# 🔽 Ejemplo de uso
if __name__ == "__main__":
    tareas = [
        Tarea("Tarea A", tiempo=6, prioridad=2),
        Tarea("Tarea B", tiempo=8, prioridad=1),
        Tarea("Tarea C", tiempo=7, prioridad=3)
    ]
    quantum = 3
    programador_round_robin(tareas, quantum)

