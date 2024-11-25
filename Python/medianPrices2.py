from datetime import datetime, timedelta
from statistics import median, mean, stdev
import random
import timeit
import heapq
from memory_profiler import profile
import psutil
import os


def memory_usage():
    process = psutil.Process(os.getpid())
    memory_info = process.memory_info()
    return memory_info.rss  # Returns memory usage in bytes


"""
PLAN:
1. Function to return median of sorted list
2. the most recommended function to achieve median 
3. function to generate huge unordered lists
4. tests for function1 and function2
5. creating other solutions theoretically less efficient
6. testing other solutions
7. final tests
8. descriptions
"""

expenses = {
    "2023-01": {
        "01": {
            "food": [22.11, 43, 11.72, 2.2, 36.29, 2.5, 19],
            "fuel": [210.22]
        },
        "09": {
            "food": [11.9],
            "fuel": [190.22]
        }
    },
    "2023-03": {
        "07": {
            "food": [20, 11.9, 30.20, 11.9]
        },
        "04": {
            "food": [10.20, 11.50, 2.5],
            "fuel": []
        }
    },
    "2023-04": {}
}


def first_sunday(year, month):
    first_day = datetime(year, month, 1)
    sunday = first_day + timedelta(days=(6 - first_day.weekday()))
    sunday_as_day_of_month = sunday.day
    return sunday_as_day_of_month

def sunday_by_key(date):
    year, month = date.split('-')
    return first_sunday(int(year), int(month))

def median_from_sorted_list(sorted_list):
    if not sorted_list:
        return None
    if len(sorted_list) % 2 == 0:
        return (sorted_list[len(sorted_list)//2-1] + sorted_list[len(sorted_list)//2])/2
    else:
        return sorted_list[len(sorted_list)//2]
    
def median_from_unsorted_list(unsorted_list):
    sorted_list = sorted(unsorted_list)
    return median_from_sorted_list(sorted_list)

@profile
def solution1(expenses):

    sublists = []


    for month in expenses:
        for day in expenses[month]:
            if int(day) <= sunday_by_key(month):
                for cathegory in expenses[month][day]:
                    sublists.append(expenses[month][day][cathegory])

    expenses_flattened = []

    for sublist in sublists:
        for expense in sublist:
            expenses_flattened.append(expense)
    
    ordered=sorted(expenses_flattened)
    return median_from_sorted_list(ordered)


def solution2(expenses):

    sublists = [expenses[month][day][cathegory] for month in expenses for day in expenses[month] if int(
        day) <= sunday_by_key(month) for cathegory in expenses[month][day]]
    total = sorted((expense for sublist in sublists for expense in sublist))
    return median_from_sorted_list(total)


def solution_optimized(expenses):
    # Flatten the data using a generator expression
    total = (expense for month in expenses
             for day in expenses[month]
             if int(day) <= sunday_by_key(month)
             for cathegory in expenses[month][day]
             for expense in expenses[month][day][cathegory])

    # Convert generator to list to avoid multiple iterations over the same data
    total_list = list(total)

    if not total_list:
        raise ValueError("No expenses found")

    # Sort the flattened list (we can sort once here)
    sorted_expenses = sorted(total_list)

    # Calculate the median
    total_expenses = len(sorted_expenses)
    middle = total_expenses // 2

    # If the number of elements is odd, return the middle element
    if total_expenses % 2 == 1:
        return sorted_expenses[middle]
    # If the number of elements is even, return the average of the two middle elements
    else:
        return (sorted_expenses[middle - 1] + sorted_expenses[middle]) / 2
    

@profile
def solution_optimized2(expenses):
    # Step 1: Flatten the data using a generator expression
    total = (expense for month in expenses
             for day in expenses[month]
             if int(day) <= sunday_by_key(month)
             for cathegory in expenses[month][day]
             for expense in expenses[month][day][cathegory])

    # Step 2: Sort the flattened list using sorted()
    sorted_expenses = sorted(total)

    # Step 3: Find the median
    total_expenses = len(sorted_expenses)
    middle = total_expenses // 2

    # If the number of elements is odd, return the middle element
    if total_expenses % 2 == 1:
        return sorted_expenses[middle]
    # If the number of elements is even, return the average of the two middle elements
    else:
        return (sorted_expenses[middle - 1] + sorted_expenses[middle]) / 2


def solution22(expenses):

    sublists= [expenses[month][day][cathegory] for month in expenses for day in expenses[month] if int(day) <= sunday_by_key(month) for cathegory in expenses[month][day]]
    total = sorted((expense for sublist in sublists for expense in sublist))
    return median_from_sorted_list(total)


def generate_random_unordered_list(length, start, end):
    """
    Generates a list of random floats with specified length, minimum value, and maximum value.
    
    Parameters:
        length (int): The number of floats to generate.
        start (float): The minimum value for the floats.
        end (float): The maximum value for the floats.
    
    Returns:
        List[float]: A list of random floats with precision of two decimal points.
    """
    random_floats = [round(random.uniform(start, end), 2)
                     for _ in range(length)]
    return random_floats

def generate_random_ordered_list(length, start, end):
    """
    Generates a list of random floats with specified length, minimum value, and maximum value.
    
    Parameters:
        length (int): The number of floats to generate.
        start (float): The minimum value for the floats.
        end (float): The maximum value for the floats.
    
    Returns:
        List[float]: A list of random floats with precision of two decimal points.
    """
    random_floats = generate_random_unordered_list(length, start, end)
    random_floats.sort()
    return random_floats


def quickselect(arr, k):
    """
    Find the k-th smallest element in the list arr.
    
    :param arr: List of elements
    :param k: Index (0-based) of the k-th smallest element to find
    :return: The k-th smallest element
    """
    if len(arr) == 1:
        return arr[0]

    pivot = random.choice(arr)

    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]

    if k < len(lows):
        return quickselect(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots))


def find_median_quickselect(arr):
    n = len(arr)
    if n % 2 == 1:
        return quickselect(arr, n // 2)
    else:
        return (quickselect(arr, n // 2 - 1) + quickselect(arr, n // 2)) / 2

def find_median_priorityqueque(arr):
    min_heap = []
    max_heap = []
    n = len(arr)

    for num in arr:
        heapq.heappush(max_heap, -heapq.heappushpop(min_heap, num))
        if len(min_heap) < len(max_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

    if n % 2 == 1:
        return float(min_heap[0])
    else:
        return (min_heap[0] - max_heap[0]) / 2


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)


def find_median_quicksort(arr):
    # Sort the array using quicksort
    sorted_arr = quicksort(arr)
    n = len(sorted_arr)
    if n % 2 == 1:
        # If odd, return the middle element
        return sorted_arr[n // 2]
    else:
        # If even, return the average of the two middle elements
        left_middle = sorted_arr[n // 2 - 1]
        right_middle = sorted_arr[n // 2]
        return (left_middle + right_middle) / 2


def find_median_with_nsmallest(arr):
    n = len(arr)
    if n % 2 == 1:
        # For odd length, find the middle element
        return heapq.nsmallest(n // 2 + 1, arr)[-1]
    else:
        # For even length, find the two middle elements and return their average
        lower_mid = heapq.nsmallest(n // 2, arr)[-1]
        upper_mid = heapq.nsmallest(n // 2 + 1, arr)[-1]
        return (lower_mid + upper_mid) / 2


def partition(arr, pivot):
    low = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    high = [x for x in arr if x > pivot]
    return low, equal, high


def select(arr, k):
    if len(arr) <= 5:
        # If the list is small, sort and return the k-th element
        return sorted(arr)[k]

    # Step 1: Divide the list into groups of 5
    chunks = [arr[i:i + 5] for i in range(0, len(arr), 5)]

    # Step 2: Find the median of each group
    medians = [sorted(chunk)[len(chunk) // 2] for chunk in chunks]

    # Step 3: Find the median of the medians
    pivot = select(medians, len(medians) // 2)

    # Step 4: Partition the list
    low, equal, high = partition(arr, pivot)

    # Step 5: Recursively select the k-th smallest element
    if k < len(low):
        return select(low, k)
    elif k < len(low) + len(equal):
        return pivot  # The pivot is the k-th smallest element
    else:
        return select(high, k - len(low) - len(equal))


def find_median_with_rt(arr):
    n = len(arr)
    if n % 2 == 1:
        return select(arr, n // 2)
    else:
        return (select(arr, n // 2 - 1) + select(arr, n // 2)) / 2





def create_wrapper(func, *args, **kwargs):
    def wrapper():
        return func(*args, **kwargs)
    return wrapper

def compare_functions(functions, args, kwargs=None, number=10, repeat=5):
    if kwargs is None:
        kwargs = {}

    results = {}

    for func in functions:
        wrapper = create_wrapper(func, *args, **kwargs)
        times = timeit.repeat(wrapper, number=number, repeat=repeat)
        results[func.__name__] = times

    # Step 4: Calculate and print statistics
    for func_name, times in results.items():
        avg_time = mean(times)
        min_time = min(times)
        max_time = max(times)
        std_dev = stdev(times)

        print(f"Function '{func_name}':")
        print(f"  Average Time: {avg_time:.5f} seconds")
        print(f"  Minimum Time: {min_time:.5f} seconds")
        print(f"  Maximum Time: {max_time:.5f} seconds")
        print(f"  Standard Deviation: {std_dev:.5f} seconds")
        print()


assert first_sunday(1970, 1) == 4,"Test case 1 failed"
assert first_sunday(1988, 8) == 7,"Test case 2 failed"
assert first_sunday(1997, 6) == 1,"Test case 3 failed"
assert first_sunday(2008, 3) == 2,"Test case 4 failed"
assert first_sunday(2016, 5) == 1,"Test case 5 failed"
assert first_sunday(2024, 11) == 3,"Test case 6 failed"

assert sunday_by_key("2023-01") == 1,"Test case 7 failed"
assert sunday_by_key("2023-03") == 5,"Test case 8 failed"
assert sunday_by_key("2023-04") == 2,"Test case 9 failed"

ex = [5]
assert median_from_sorted_list(ex) == median(ex)==find_median_quickselect(ex),"Test case 10 failed"



big_list = generate_random_unordered_list(1000000, 0.15, 500)
big_list2=iter(big_list)

expenses2 = {
    "2023-01": {
        "01": {
            "food": big_list,
            "fuel": [210.22]
        },
        "09": {
            "food": [11.9],
            "fuel": [190.22]
        }
    },
    "2023-03": {
        "07": {
            "food": [20, 11.9, 30.20, 11.9]
        },
        "04": {
            "food": [10.20, 11.50, 2.5],
            "fuel": []
        }
    },
    "2023-04": {}
}


to_compare = [median_from_unsorted_list, median, find_median_quickselect, find_median_priorityqueque, find_median_quicksort, find_median_with_nsmallest, find_median_with_rt]
to_compare2 = [solution1, solution2,solution_optimized, solution_optimized2]
#compare_functions(to_compare2, [expenses2])

@profile
def solution4(expenses):
    # Step 1: Flatten the data using a generator expression
    try:
        total = (expense for month in expenses
                 for day in expenses[month]
                 if int(day) <= sunday_by_key(month)
                 for cathegory in expenses[month][day]
                 for expense in expenses[month][day][cathegory])
    except TypeError('wrong data'):
        return None

    if not total:
        return None

    # Step 2: Sort the flattened list using sorted()
    return median(total)

print(f"Memory usage before function: {memory_usage()} bytes")
solution4(expenses2)
print(f"Memory usage after function: {memory_usage()} bytes")
