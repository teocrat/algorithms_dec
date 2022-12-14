def bubble_sort(arr):
    flag = True
    while flag:
        flag = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                flag = True
    return arr


if __name__ == 'main':
    print(bubble_sort([4, 8, 1, 9, 10, 3, 2, 5, 7, 6]))
