def bin_search(arr, num):
    low = 0
    high = len(arr) - 1
    while low <= high:
        middle = (low + high) // 2
        if arr[middle] == num:
            return middle
        elif arr[middle] > num:
            high = middle - 1
        else:
            low = middle + 1
    return -1


print(bin_search([1, 3, 7, 9, 10, 12, 14, 23, 45], 14))
