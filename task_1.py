import random
import timeit

arr = [random.randint(1,1000) for _ in range(10000)]

def merge_sort_test():
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        return merge(merge_sort(left_half), merge_sort(right_half))
    merge_sort(arr)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def insertion_sort_test():
    def insertion_sort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while j >=0 and key < arr[j] :
                    arr[j+1] = arr[j]
                    j -= 1
            arr[j+1] = key 
        return arr
    insertion_sort(arr)


insertion_time = timeit.timeit(stmt = insertion_sort_test,number=1000) 
merge_time = timeit.timeit(stmt = merge_sort_test, number=1000)

print(f"\nВремя выполнения методом вставки: {insertion_time:.6f} секунд")
print(f"\nВремя выполнения методом слияния: {merge_time:.6f} секунд")