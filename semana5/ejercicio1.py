class ColaConDosPilas:
    def __init__(self):
        self.stack_in = []  
        self.stack_out = []  


    def encolar(self, elemento):
        self.stack_in.append(elemento)


    def retirar(self):
        if self.esta_vacia():
            raise Exception("La cola está vacía")
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()


    def revisar(self):
        if self.esta_vacia():
            raise Exception("La cola está vacía")
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]


    def esta_vacia(self):
        return not self.stack_in and not self.stack_out


cola = ColaConDosPilas()
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)


print(cola.revisar())  
print(cola.retirar())  
print(cola.retirar())  
print(cola.esta_vacia())  
print(cola.retirar())  
print(cola.esta_vacia())