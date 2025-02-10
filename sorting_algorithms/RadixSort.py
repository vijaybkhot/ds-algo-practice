import math


def get_digit(num, place):
    if place > 0:
        divisor = (10 ** (place - 1))
        return int(num / divisor) % 10
    else:
        return num


def countDigit(n):
    if n == 0:
        return 1
    return math.floor(math.log10(abs(n)) + 1)


def most_digits(arr):
    count = 0
    for num in arr:
        new_count = countDigit(num)
        if new_count > count:
            count = new_count
    return count


def radix_sort(arr):
    k = most_digits(arr)
    for num in range(k):
        place = num + 1
        buckets = [[] for _ in range(10)]  # Create buckets for digits 0-9
        for i in arr:
            place_digit = get_digit(i, place)
            buckets[place_digit].append(i)
        arr = [num for bucket in buckets for num in bucket]
    print(arr)


def radix_sort_counting(arr):
    if not arr:
        return
    # Find the maximum number of digits in the array
    max_digits = len(str(max(arr)))
    # Initialize the position to 1 (rightmost digit)
    pos = 1
    # Continue sorting until all digits are considered
    while pos <= 10 ** max_digits:
        # Perform a counting sort based on the current digit position
        count_sort_radix(arr, pos)
        # Move to the next digit position
        pos *= 10


def count_sort_radix(arr, pos):
    n = len(arr)
    # Create an array to store the count of each digit (0-9)
    C = [0] * 10
    # Count the occurrences of each digit at the current position
    for i in range(n):
        digit = (arr[i] // pos) % 10  # Extract the digit at the current position
        C[digit] += 1
    # Modify C to store the cumulative count of digits
    for i in range(1, 10):
        C[i] = C[i] + C[i - 1]
    # Create a temporary array to store the sorted result
    B = [0] * n
    for i in range(n - 1, -1, -1):  # Iterate over the input array in reverse
        digit = (arr[i] // pos) % 10  # Extract the digit at the current position
        # Place the element at the correct position in the temporary array
        B[C[digit] - 1] = arr[i]
        # Decrement the count of the current digit in the count array
        C[digit] -= 1
    # Copy the sorted elements from the temporary array back to the input array
    for i in range(n):
        arr[i] = B[i]


def rsc_p1(arr):
    max_digits = len(str(max(arr)))
    pos = 1
    while pos <= 10 ** max_digits:
        csr_p1(arr, pos)
        pos *= 10


def csr_p1(arr, pos):
    C = [0] * 10
    n = len(arr)
    B = [0] * n
    # Fill C
    for i in range(n):
        digit = (arr[i] // pos) % 10
        C[digit] += 1
    # Get cumulative array
    for i in range(1, 10):
        C[i] += C[i - 1]
    # Fill B
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // pos) % 10
        B[C[digit] - 1] = arr[i]
        C[digit] -= 1
    for i in range(n):
        arr[i] = B[i]


def rsc_p2(A):
    max_digits = len(str(max(A)))
    pos = 1
    while pos <= 10 ** max_digits:
        csr_p2(A, pos)
        pos *= 10


def csr_p2(A, pos):
    n = len(A)
    C = [0] * 10
    B = [0] * n
    for i in range(n):
        index = (A[i] // pos) % 10
        C[index] += 1
    for i in range(1, 10):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        index = (A[i] // pos) % 10
        C[index] -= 1
        B[C[index]] = A[i]
    for i in range(n):
        A[i] = B[i]


def rsc_p3(A):
    max_digits = len(str(max(A)))
    pos = 1
    while pos <= 10 ** max_digits:
        csr_p3(A, pos)
        pos *= 10


def csr_p3(A, pos):
    n = len(A)
    C = [0] * 10
    B = [0] * n
    for i in range(n):
        digit = (A[i] // pos) % 10
        C[digit] += 1
    for i in range(1, 10):
        C[i] += C[i - 1]
    for i in range(n - 1, -1, -1):
        digit = (A[i] // pos) % 10
        C[digit] -= 1
        B[C[digit]] = A[i]
    for i in range(n):
        A[i] = B[i]


def rsc_p4(A):
    max_digits = len(str(max(A)))
    pos = 1
    while pos <= 10 ** max_digits:
        csr_p4(A, pos)
        pos *= 10


def csr_p4(A, pos):
    n = len(A)
    C = [0] * 10
    B = [0] * n
    for i in range(n):
        digit = (A[i] // pos) % 10
        C[digit] += 1
    for i in range(1, 10):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        digit = (A[i] // pos) % 10
        C[digit] -= 1
        B[C[digit]] = A[i]

    for i in range(n):
        A[i] = B[i]


def counting_sort_radix_5(array, position):
    length_array = len(array)
    C = [0] * 10
    B = [0] * length_array
    for i in range(length_array):
        digit = (array[i] // position) % 10
        C[digit] += 1
    for i in range(1, 10):
        C[i] += C[i - 1]
    for i in range(length_array - 1, -1, -1):
        digit = (array[i] // position) % 10
        C[digit] -= 1
        B[C[digit]] = array[i]
    for i in range(length_array):
        array[i] = B[i]


def radix_sort_counting_5(array):
    max_digits = len(str(max(array)))
    position = 1
    while position <= 10 ** max_digits:
        counting_sort_radix_5(array, position)
        position *= 10


def counting_sort_radix_6(array, position):
    length_array = len(array)
    C = [0] * 10
    B = [0] * length_array
    for i in range(length_array):
        digit = (array[i] // position) % 10
        C[digit] += 1
    for i in range(1, 10):
        C[i] += C[i - 1]
    for i in range(length_array - 1, -1, -1):
        digit = (array[i] // position) % 10
        C[digit] -= 1
        B[C[digit]] = array[i]
    for i in range(length_array):
        array[i] = B[i]


def radix_sort_counting_6(array):
    max_digits = len(str(max(array)))
    position = 1
    while position <= 10 ** max_digits:
        counting_sort_radix_6(array, position)
        position *= 10


def counting_sort_radix_7(array, pos):
    C = [0] * 10
    n = len(array)
    B = [0] * n
    for i in range(n):
        digit = (array[i] // pos) % 10
        C[digit] += 1
    for i in range(1, 10):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        digit = (array[i] // pos) % 10
        C[digit] -= 1
        B[C[digit]] = array[i]

    for i in range(n):
        array[i] = B[i]


def radix_sort_counting_7(array):
    max_digits = len(str(max(array)))
    pos = 1
    while pos <= 10 ** max_digits:
        counting_sort_radix_7(array, pos)
        pos *= 10


def counting_sort_radix_8(array, pos):
    n = len(array)
    C = [0] * 10
    B = [0] * n
    for i in range(n):
        digit = (array[i] // pos) % 10
        C[digit] += 1

    for i in range(1, 10):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        digit = (array[i] // pos) % 10
        C[digit] -= 1
        B[C[digit]] = array[i]

    for i in range(n):
        array[i] = B[i]


def radix_sort_counting_8(array):
    max_digits = len(str(max(array)))
    pos = 1
    while pos <= 10 ** max_digits:
        counting_sort_radix_8(array, pos)
        pos *= 10


def counting_sort_radix_9(array, pos):
    n = len(array)
    C = [0] * 10
    B = [0] * n
    for i in range(n):
        digit = (array[i] // pos) % 10
        C[digit] += 1
    for i in range(1, 10):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        digit = (array[i] // pos) % 10
        C[digit] -= 1
        B[C[digit]] = array[i]

    for i in range(n):
        array[i] = B[i]


def radix_sort_counting_9(array):
    max_digits = len(str(max(array)))
    pos = 1
    while pos <= 10 ** max_digits:
        counting_sort_radix_9(array, pos)
        pos *= 10


def counting_sort_radix_10(array, pos):
    n = len(array)
    C = [0] * 10
    B = [0] * n
    for i in range(n):
        digit = (array[i] // pos) % 10
        C[digit] += 1
    for i in range(1, 10):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        digit = (array[i] // pos) % 10
        C[digit] -= 1
        B[C[digit]] = array[i]

    for i in range(n):
        array[i] = B[i]


def radix_sort_counting_10(array):
    if not array:
        return array

    max_digits = len(str(max(array)))
    pos = 1
    while pos <= 10 ** max_digits:
        counting_sort_radix_10(array, pos)
        pos *= 10
    return array


def radix_sort_negative_10(array):
    positive_nums = [num for num in array if num >= 0]
    negative_nums = [-num for num in array if num < 0]
    positive_nums = radix_sort_counting_10(positive_nums)
    negative_nums = radix_sort_counting_10(negative_nums)
    sorted_negative_nums = [-num for num in reversed(negative_nums)]
    return sorted_negative_nums + positive_nums


def counting_sort_radix_11(array, pos):
    C = [0] * 10
    B = [0] * len(array)
    for i in range(len(array)):
        digit = (array[i] // pos) % 10
        C[digit] += 1
    for i in range(1, 10):
        C[i] += C[i - 1]
    for i in range(len(array) - 1, -1, -1):
        digit = (array[i] // pos) % 10
        C[digit] -= 1
        B[C[digit]] = array[i]
    return B


def radix_sort_counting_11(array):
    if array:
        max_digits = len(str(max(array)))
        pos = 1
        while pos <= 10 ** max_digits:
            array = counting_sort_radix_11(array, pos)
            pos *= 10
        return array
    else:
        return array


def radix_sort_negative_11(array):
    negative_nums = [-num for num in array if num < 0]
    positive_nums = [num for num in array if num >= 0]
    positive_nums = radix_sort_counting_11(positive_nums)
    negative_nums = radix_sort_counting_11(negative_nums)
    sorted_negative_nums = [-num for num in reversed(negative_nums)]
    return sorted_negative_nums + positive_nums


def counting_sort_radix_12(array, pos):
    C = [0] * 10
    B = [0] * len(array)

    for i in range(len(array)):
        digit = (array[i] // pos) % 10
        C[digit] += 1

    for i in range(1, 10):
        C[i] += C[i - 1]

    for i in range(len(array) - 1, -1, -1):
        digit = (array[i] // pos) % 10
        C[digit] -= 1
        B[C[digit]] = array[i]

    return B


def radix_sort_counting_12(array):
    if array:
        max_digits = len(str(max(array)))
        pos = 1
        while pos <= 10 ** max_digits:
            array = counting_sort_radix_12(array, pos)
            pos *= 10
    return array


def radix_sort_negative_12(array):
    negative_nums = [-num for num in array if num < 0]
    positive_nums = [num for num in array if num >= 0]
    negative_nums = radix_sort_counting_12(negative_nums)
    positive_nums = radix_sort_counting_12(positive_nums)
    sorted_negative_nums = [-num for num in reversed(negative_nums)]
    return sorted_negative_nums + positive_nums


def counting_sort_radix_13(array, pos):
    n = len(array)
    C = [0] * 10
    B = [0] * n
    for i in range(n):
        digit = (array[i] // pos) % 10
        C[digit] += 1
    for i in range(1, 10):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        digit = (array[i] // pos) % 10
        C[digit] -= 1
        B[C[digit]] = array[i]
    return B


def radix_sort_counting_13(array):
    if array:
        max_digits = len(str(max(array)))
        pos = 1
        while pos <= 10 ** max_digits:
            array = counting_sort_radix_13(array, pos)
            pos *= 10
    return array


def radix_sort_negative_13(array):
    negative_nums = [-num for num in array if num < 0]
    positive_nums = [num for num in array if num >= 0]
    negative_nums = radix_sort_counting_13(negative_nums)
    positive_nums = radix_sort_counting_13(positive_nums)
    sorted_negatives = [-num for num in reversed(negative_nums)]
    return sorted_negatives + positive_nums


def counting_sort_radix_14(array, pos):
    n = len(array)
    C = [0] * 10
    B = [0] * n
    for i in range(n):
        digit = (array[i] // pos) % 10
        C[digit] += 1
    for i in range(1, 10):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        digit = (array[i] // pos) % 10
        C[digit] -= 1
        B[C[digit]] = array[i]
    return B


def radix_sort_counting_14(array):
    if array:
        max_digits = len(str(max(array)))
        pos = 1
        while pos <= 10 ** max_digits:
            array = counting_sort_radix_14(array, pos)
            pos *= 10
    return array


def radix_sort_negatives_14(array):
    positive_nums = [num for num in array if num >= 0]
    negative_nums = [-num for num in array if num < 0]
    positive_nums = radix_sort_counting_14(positive_nums)
    negative_nums = radix_sort_counting_14(negative_nums)
    sorted_negatives = [-num for num in reversed(negative_nums)]
    return sorted_negatives + positive_nums


def counting_sort_radix_15(array, pos):
    n = len(array)
    C = [0] * 10
    B = [0] * n
    for i in range(n):
        digit = (array[i] // pos) % 10
        C[digit] += 1
    for i in range(1, 10):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        digit = (array[i] // pos) % 10
        C[digit] -= 1
        B[C[digit]] = array[i]

    return B


def radix_sort_counting_15(array):
    if array:
        max_digits = len(str(max(array)))
        pos = 1
        while pos <= 10 ** max_digits:
            array = counting_sort_radix_15(array, pos)
            pos *= 10
    return array


def radix_sort_negatives_15(array):
    positive_nums = [num for num in array if num >= 0]
    negative_nums = [-num for num in array if num < 0]
    positive_nums = radix_sort_counting_15(positive_nums)
    negative_nums = radix_sort_counting_15(negative_nums)
    sorted_negatives = [-num for num in reversed(negative_nums)]
    return sorted_negatives + positive_nums


def counting_sort_radix_16(array, pos):
    n = len(array)
    C = [0] * 10
    B = [0] * n

    for i in range(n):
        digit = (array[i]//pos) % 10
        C[digit] += 1

    for i in range(1, 10):
        C[i] += C[i-1]

    for i in range(n-1, -1, -1):
        digit = (array[i]//pos) % 10
        C[digit] -= 1
        B[C[digit]] = array[i]

    return B


def radix_sort_counting_16(array):
    if array:
        max_digits = len(str(max(array)))

        pos = 1

        while pos <= 10**max_digits:
            array = counting_sort_radix_16(array, pos)
            pos *= 10

    return array


def radix_sort_negatives_16(array):
    positive_nums = [num for num in array if num >= 0]
    negative_nums = [-num for num in array if num < 0]
    sorted_positives = radix_sort_counting_16(positive_nums)
    negative_nums = radix_sort_counting_16(negative_nums)
    sorted_negatives = [-num for num in reversed(negative_nums)]
    return sorted_negatives + sorted_positives






def test_radix(radix_sort_test):
    # Test case with positive and negative numbers
    array1 = [-23, 45, -12, 7, -10, 0, 2, -5, 13]
    print(radix_sort_test(array1))
    # Output: [-23, -12, -10, -5, 0, 2, 7, 13, 45]

    # Test case with only positive numbers
    array1 = [5, 2, 8, 10, 3, 1]
    print(radix_sort_test(array1))
    # Output: [1, 2, 3, 5, 8, 10]

    # Test case with only negative numbers
    array1 = [-5, -2, -8, -10, -3, -1]
    print(radix_sort_test(array1))
    # Output: [-10, -8, -5, -3, -2, -1]

    # Test case with an empty array
    array1 = []
    print(radix_sort_test(array1))
    # Output: []


test_radix(radix_sort_test=radix_sort_negatives_16)
