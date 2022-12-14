def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left_nums = []
        right_nums = []
        middle_nums = []
        for i in arr:
            if i < pivot:
                left_nums.append(i)
            elif i > pivot:
                right_nums.append(i)
            else:
                middle_nums.append(i)
        return quick_sort(left_nums) + middle_nums + quick_sort(right_nums)


if __name__ == 'main':
    print(quick_sort([4, 8, 1, 9, 10, 3, 2, 5, 7, 6]))
