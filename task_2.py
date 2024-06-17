import timeit
import random

numbers = list((random.randint(1,300)) for _ in range(10000))

def sort_test():
    numbers1 = numbers.copy()
    numbers1.sort()

def sorted_test():
    array = numbers.copy()
    data = sorted(array)
    return data
    


sort_time = timeit.timeit(sort_test, number=1000)
sorted_time = timeit.timeit(sorted_test, number=1000)

print(f"\nВремя sort = {sort_time:.6f} секунд")
print(f"\nВремя sorted = {sorted_time:.6f} секунд")