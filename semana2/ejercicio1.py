def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Casos de prueba
print("fibonacci(0) =", fibonacci(0))     # 0
print("fibonacci(1) =", fibonacci(1))     # 1
print("fibonacci(2) =", fibonacci(2))     # 1
