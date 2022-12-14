from bubble_sort import bubble_sort
from direct_sort import direct_sort
from insertion_sort import insertion_sort
from quick_sort import quick_sort
from heap_sort import heap_sort
from random import randint
import time

arr = [randint(1, 10000) for i in range(10000)]

start = time.perf_counter()
bubble_sort(arr)
print(f'bubble_sort: {time.perf_counter() - start:.3f} c')

start_1 = time.perf_counter()
direct_sort(arr)
print(f'direct_sort: {time.perf_counter() - start_1:.3f} c')

start_2 = time.perf_counter()
insertion_sort(arr)
print(f'insertion_sort: {time.perf_counter() - start_2:.3f} c')

start_3 = time.perf_counter()
quick_sort(arr)
print(f'quick_sort: {time.perf_counter() - start_3:.3f} c')

