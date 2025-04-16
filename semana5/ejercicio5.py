from collections import deque


def maxSlidingWindow(nums, k):
    if not nums:
        return []
   
    n = len(nums)
    result = []
    dq = deque()  # Guarda índices, no valores directamente


    for i in range(n):
        # Elimina índices que están fuera de la ventana
        while dq and dq[0] < i - k + 1:
            dq.popleft()


        # Elimina elementos más pequeños que nums[i] desde el final
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()


        dq.append(i)


        # Agrega el máximo actual al resultado (cuando ya hay al menos k elementos)
        if i >= k - 1:
            result.append(nums[dq[0]])


    return result


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(maxSlidingWindow(nums, k))  # ➡️ [3, 3, 5, 5, 6, 7]




