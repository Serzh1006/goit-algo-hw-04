import timeit
import random
from prettytable import PrettyTable

mysetup = """
from __main__ import sort_test
from __main__ import sorted_test
from __main__ import test_data
from __main__ import merge_sort
from __main__ import insertion_sort
"""

# Create a PrettyTable object
table = PrettyTable()

test_data = {
    's':list((random.randint(1,900)) for _ in range(100)),
    'm':list((random.randint(1,900)) for _ in range(1000)),
    'l':list((random.randint(1,900)) for _ in range(10000))
}

def sort_test(data):
    new_data = data.copy()
    new_data.sort()

def sorted_test(data):
    new_data = data.copy()
    result = sorted(new_data)
    return result

def merge_sort(arr):
    new_arr = arr.copy()
    if len(new_arr) <= 1:
        return new_arr
    mid = len(new_arr) // 2
    left_half = new_arr[:mid]
    right_half = new_arr[mid:]
    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1


    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def insertion_sort(arr):
    new_arr = arr.copy()
    for i in range(1, len(new_arr)):
        key = new_arr[i]
        j = i-1
        while j >=0 and key < new_arr[j] :
                new_arr[j+1] = new_arr[j]
                j -= 1
        new_arr[j+1] = key 
    return new_arr


insertion_time_small = timeit.timeit(stmt = "insertion_sort(test_data['s'])",setup=mysetup,number=50)
insertion_time_medium = timeit.timeit(stmt = "insertion_sort(test_data['m'])",setup=mysetup,number=50)
insertion_time_large = timeit.timeit(stmt = "insertion_sort(test_data['l'])",setup=mysetup,number=50)

merge_time_small = timeit.timeit(stmt = "merge_sort(test_data['s'])", setup=mysetup,number=50)
merge_time_medium = timeit.timeit(stmt = "merge_sort(test_data['m'])", setup=mysetup,number=50)
merge_time_large = timeit.timeit(stmt = "merge_sort(test_data['l'])", setup=mysetup,number=50)


sort_time_small = timeit.timeit(stmt="sort_test(test_data['s'])", setup=mysetup, number=50)
sort_time_medium = timeit.timeit(stmt="sort_test(test_data['m'])", setup=mysetup, number=50)
sort_time_large = timeit.timeit(stmt="sort_test(test_data['l'])", setup=mysetup, number=50)

sorted_time_small = timeit.timeit(stmt="sorted_test(test_data['s'])", setup=mysetup, number=50)
sorted_time_medium = timeit.timeit(stmt="sorted_test(test_data['m'])", setup=mysetup, number=50)
sorted_time_large = timeit.timeit(stmt="sorted_test(test_data['l'])", setup=mysetup, number=50)

# Define the columns
table.field_names = ["Method", "small", "medium", "large"]
# Add rows to the table
table.add_row(["Sort", f"{sort_time_small:.6f}", f"{sort_time_medium:.6f}",f"{sort_time_large:.6f}"])
table.add_row(["Sorted", f"{sorted_time_small:.6f}", f"{sorted_time_medium:.6f}", f"{sorted_time_large:.6f}"])
table.add_row(["Merge", f"{merge_time_small:.6f}", f"{merge_time_medium:.6f}", f"{merge_time_large:.6f}"])
table.add_row(["Insertion", f"{insertion_time_small:.6f}", f"{insertion_time_medium:.6f}", f"{insertion_time_large:.6f}"])
print(table)