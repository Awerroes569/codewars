from datetime import datetime, timedelta

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
    """
    Calculate the day of the month for the first Sunday of a given month and year.
    
    Parameters:
    year (int): The year in which to find the first Sunday.
    month (int): The month in which to find the first Sunday.
    
    Returns:
    int: The day of the month of the first Sunday.
    """
    first_day = datetime(year, month, 1)
    sunday = first_day + timedelta(days=(6 - first_day.weekday()))
    sunday_as_day_of_month = sunday.day
    return sunday_as_day_of_month

def sunday_by_key(date):
    """
    Calculate the day of the month for the first Sunday of a given month and year
    extracted from a date string in the format 'YYYY-MM'.

    Parameters:
    date (str): The date string in the format 'YYYY-MM'.

    Returns:
    int: The day of the month of the first Sunday.
    """
    year, month = date.split('-')
    return first_sunday(int(year), int(month))

def median_from_sorted_list(sorted_list):
    """
    Calculate the median value from a sorted list of numbers.

    Parameters:
    sorted_list (list): A list of numbers sorted in ascending order.

    Returns:
    float: The median value of the list. Returns None if the list is empty.
    """
    if not sorted_list:
        return None
    if len(sorted_list) % 2 == 0:
        return (sorted_list[len(sorted_list) // 2 - 1] + sorted_list[len(sorted_list) // 2]) / 2
    else:
        return sorted_list[len(sorted_list) // 2]

def median_from_unsorted_list(unsorted_list):
    """
    Calculate the median value from an unsorted list of numbers.

    Parameters:
    unsorted_list (list): A list of numbers in any order.

    Returns:
    float: The median value of the list. Returns None if the list is empty.
    """
    if not unsorted_list:
        return None
    sorted_list = sorted(unsorted_list)
    return median_from_sorted_list(sorted_list)

def solution1(expenses):
    """
    Calculate the median value of expenses that occur on or before the first Sunday
    of each month from a nested dictionary of expenses.

    Parameters:
    expenses (dict): A nested dictionary where keys are months in 'YYYY-MM' format,
                     values are dictionaries with days as keys, and categories as keys 
                     within those days, with expense lists as values.

    Returns:
    float: The median value of the expenses. Returns None if there are no valid expenses 
           or if a TypeError occurs.
    """
    sublists = []
    try:
        for month in expenses:
            for day in expenses[month]:
                if int(day) <= sunday_by_key(month):
                    for category in expenses[month][day]:
                        sublists.append(expenses[month][day][category])
    except TypeError:
        return None

    expenses_flattened = []

    for sublist in sublists:
        for expense in sublist:
            expenses_flattened.append(expense)

    if not expenses_flattened:
        return None

    return median_from_unsorted_list(expenses_flattened)

def solution2(expenses):
    """
    Calculate the median value of expenses that occur on or before the first Sunday
    of each month from a nested dictionary of expenses.
    This solution is optimized for better performance compared to solution1.

    Following algorithms were taken into account to optimize the speed of the function:
        - quickselect
        - priority queue
        - quicksort
        - Rivest-Tarjan algorithm.
    Implementations of these algorithms were tested to find the most efficient one.
    Theoretically, quickselect or Rivest-Tarjan should the fastest algorithm for finding the median of an unsorted list 
    ( due to time complexity of O(n) ).
    Due to limitations for the task('Należy użyć tylko funkcji/modułów ze standardowej biblioteki (np. math).') own implementations 
    in Python of these algorithms appeared not faster than the standard solutions (sorted, median, sort - which are based on C libraries).
    Thus, the function uses built-in functions (sorted) to find the median of the list.
    The greater emphasis is placed on memory optimization by using a generator expression to process the expenses lazily.
    
    The main differences between solution1 and solution2 are:

    - **Memory Usage**: 
        - `solution1` creates two intermediate lists (`sublists` and `expenses_flattened`) to store the data before processing it. 
            This increases memory usage, especially for large datasets.
        - `solution2` uses a generator expression (`total`) to process the expenses lazily, without creating intermediate lists, 
            making it much more memory-efficient.

    - **Speed**: 
        - `solution1` uses multiple nested loops and appends to flatten the data into a single list (`expenses_flattened`),
            which introduces additional overhead and increases execution time.
        - `solution2` processes the expenses directly through the generator expression, yielding values one at a time and 
            converting them to a list only when necessary. This avoids the overhead of flattening and appending, resulting
            in faster execution, especially for large datasets.

    The optimizations in `solution2` make it more efficient in both speed and memory usage compared to `solution1`.

    Parameters:
    expenses (dict): A nested dictionary where keys are months in 'YYYY-MM' format,
                     values are dictionaries with days as keys, and categories as keys 
                     within those days, with expense lists as values.

    Returns:
    float: The median value of the expenses. Returns None if there are no valid expenses 
           or if a TypeError occurs.
    """
    try:
        total = (expense for month in expenses
                 for day in expenses[month]
                 if int(day) <= sunday_by_key(month)
                 for category in expenses[month][day]
                 for expense in expenses[month][day][category])
    except TypeError:
        return None

    return median_from_unsorted_list(list(total))

"""
WORKING CODE AND SOME TESTS

import random
import timeit
import heapq
from statistics import median, mean, stdev

def generate_random_unordered_list(length, start, end):
   
    random_floats = [round(random.uniform(start, end), 2)
                     for _ in range(length)]
    return random_floats


def generate_random_ordered_list(length, start, end):
    
    random_floats = generate_random_unordered_list(length, start, end)
    random_floats.sort()
    return random_floats


def quickselect(arr, k):
    
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


expenses2 = {
    "2023-01": {
        "01": {
            "food": [1, 2, 3, 4, 5, 6, 7],
            "fuel": [8, 9]
        },
    },
    "2023-04": {}
}

expenses3 = {
    "2023-01": {},
    "2023-04": {}
}


expenses4 = {
    "2023-01": {
        "01": {
            "food": [1, 2, 3, 4, 5, 6, 7],
            "fuel": [8, 9, 10]
        },
    },
    "2023-04": {}
}

# Testing function 'first_sunday'
assert first_sunday(1970, 1) == 4, "Test case 1 failed"
assert first_sunday(1988, 8) == 7, "Test case 2 failed"
assert first_sunday(1997, 6) == 1, "Test case 3 failed"
assert first_sunday(2008, 3) == 2, "Test case 4 failed"
assert first_sunday(2016, 5) == 1, "Test case 5 failed"
assert first_sunday(2024, 11) == 3, "Test case 6 failed"

# Testing function 'sunday_by_key'
assert sunday_by_key("2023-01") == 1, "Test case 7 failed"
assert sunday_by_key("2023-03") == 5, "Test case 8 failed"
assert sunday_by_key("2023-04") == 2, "Test case 9 failed"
assert sunday_by_key("1970-01") == 4, "Test case 10 failed"
assert sunday_by_key("1988-08") == 7, "Test case 11 failed"
assert sunday_by_key("1997-06") == 1, "Test case 12 failed"
assert sunday_by_key("2008-03") == 2, "Test case 13 failed"
assert sunday_by_key("2016-05") == 1, "Test case 14 failed"
assert sunday_by_key("2024-11") == 3, "Test case 15 failed"

# Testing function 'solution1'
assert solution1(expenses2) == 5, "Test case 16 failed"
assert solution1(expenses3) == None, "Test case 17 failed"
assert solution1(expenses4) == 5.5, "Test case 19 failed"

# Testing function 'solution2'
assert solution2(expenses2) == 5, "Test case 20 failed"
assert solution2(expenses3) == None, "Test case 21 failed"
assert solution2(expenses4) == 5.5, "Test case 23 failed"

ex = [5]
assert median_from_sorted_list(ex) == median(
    ex) == find_median_quickselect(ex), "Test case 10 failed"


big_list = generate_random_unordered_list(1000000, 0.15, 500)

to_compare = [median_from_unsorted_list, median, find_median_quickselect,
              find_median_priorityqueque, find_median_quicksort, find_median_with_nsmallest, find_median_with_rt]
to_compare2 = [solution1,solution2]

"""
