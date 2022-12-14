def insertion_sort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


if __name__ == 'main':
    print(insertion_sort([4, 8, 1, 9, 10, 3, 2, 5, 7, 6]))
