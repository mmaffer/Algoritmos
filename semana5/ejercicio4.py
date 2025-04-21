from collections import deque

def sliding_window_max(nums, k):
    if not nums or k <= 0:
        return []

    result = []
    window = deque()  # Guardará los índices, no los valores directamente

    for i in range(len(nums)):
        # Eliminar índices que ya no están dentro del rango de la ventana
        while window and window[0] <= i - k:
            window.popleft()

        # Eliminar del final los elementos menores que el actual
        while window and nums[window[-1]] < nums[i]:
            window.pop()

        # Agregar el índice actual
        window.append(i)

        # A partir de que la ventana se llena (i >= k - 1), agregar el máximo al resultado
        if i >= k - 1:
            result.append(nums[window[0]])

    return result

nums1 = [1, 3, -1, -3, 5, 3, 6, 7]
k1 = 3
print("Caso 1:", sliding_window_max(nums1, k1))  

# Caso 2: Ventana igual al tamaño del arreglo
nums2 = [2, 1, 3, 4]
k2 = 4
print("Caso 2:", sliding_window_max(nums2, k2))  

# Caso 3: Valores negativos
nums3 = [-4, -1, -5, -2, -3, -6]
k3 = 2
print("Caso 3:", sliding_window_max(nums3, k3))