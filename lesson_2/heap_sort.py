def heapify(arr, a, b):
    largest = b
    l = 2 * b + 1
    r = 2 * b + 2
    if l < a and arr[b] < arr[l]:
        largest = l
    if r < a and arr[largest] < arr[r]:
        largest = r
    if largest != b:
        arr[b], arr[largest] = arr[largest], arr[b]
        heapify(arr, a, largest)


def heap_sort(arr):
    a = len(arr)
    for b in range(a // 2 - 1, -1, -1):
        heapify(arr, a, b)
    for b in range(a - 1, 0, -1):
        arr[b], arr[0] = arr[0], arr[b]
        heapify(arr, b, 0)


arr = [4, 8, 1, 9, 10, 3, 2, 5, 7, 6]
heap_sort(arr)
print(arr)
