def direct_sort(arr):
    for i in range(len(arr)):
        min_pos = i
        for j in range(i + 1, len(arr)):
            if arr[min_pos] > arr[j]:
                min_pos = j
        if min_pos != i:
            arr[i], arr[min_pos] = arr[min_pos], arr[i]
    return arr


if __name__ == 'main':
    print(direct_sort([4, 8, 1, 9, 10, 3, 2, 5, 7, 6]))
