def partition(arr, start, end):
    pivot = arr[end]
    pi = start  # Potential Index
    # Imagine shifting the pivot to pi which is before arr[i]
    # Would this violate the condition that all numbers smaller than the pivot should be to its left?
    # If yes, then swap arr[pi] and arr[i] and increment pi
    # Else check from next element, i.e. increment i
    for i in range(start, end):
        if arr[i] <= pivot:
            # Swap arr[pi] and a[i]
            arr[pi], arr[i] = arr[i], arr[pi]
            pi += 1
    arr[pi], arr[end] = arr[end], arr[pi]
    return pi


def quick_sort(arr, start, end):
    # Base case: if start >= end return nothing

    if start < end:
        # Get the partition index
        pi = partition(arr, start, end)
        # Quick sort the left of partition index
        quick_sort(arr, start, pi - 1)
        # Quick sort the right of partition
        quick_sort(arr, pi + 1, end)


def partition_practice(arr, start, end):
    pivot = arr[end]
    pi = start
    for i in range(start, end):
        if arr[i] <= pivot:
            arr[i], arr[pi] = arr[pi], arr[i]
            pi += 1
    arr[pi], arr[end] = arr[end], arr[pi]
    return pi


def quick_sort_practice(arr, start, end):
    if start < end:
        pi = partition_practice(arr, start, end)
        quick_sort_practice(arr, start, pi - 1)
        quick_sort_practice(arr, pi + 1, end)


def partition_practice1(arr, start, end):
    pivot = arr[end]
    pi = start
    for i in range(start, end):
        if arr[i] <= pivot:
            arr[pi], arr[i] = arr[i], arr[pi]
            pi += 1
    arr[pi], arr[end] = arr[end], arr[pi]
    return pi


def quick_sort_practice1(arr, start, end):
    if start < end:
        pi = partition_practice1(arr, start, end)
        quick_sort_practice1(arr, start, pi - 1)
        quick_sort_practice1(arr, pi + 1, end)


def partition_practice2(arr, start, end):
    pivot = arr[end]
    pi = start  # Remember that pi is always the start index and not 0
    for i in range(start, end):
        if arr[i] <= pivot:
            arr[i], arr[pi] = arr[pi], arr[i]
            pi += 1
    arr[pi], arr[end] = arr[end], arr[pi]
    return pi


def quick_sort_practice2(arr, start, end):
    if start < end:
        pi = partition_practice2(arr, start, end)
        quick_sort_practice2(arr, start, pi - 1)
        quick_sort_practice2(arr, pi + 1, end)


def pi_p3(arr, start, end):
    pi = start
    pivot = arr[end]
    for i in range(start, end):
        if arr[i] <= pivot:
            arr[i], arr[pi] = arr[pi], arr[i]
            pi += 1
    arr[pi], arr[end] = arr[end], arr[pi]
    return pi


def qs_p3(arr, start, end):
    if start < end:
        pi = pi_p3(arr, start, end)
        qs_p3(arr, start, pi - 1)
        qs_p3(arr, pi + 1, end)


def pi_4(arr, start, end):
    pi = start
    pivot = arr[end]
    for i in range(start, end):
        if arr[i] > pivot:
            continue
        else:
            arr[i], arr[pi] = arr[pi], arr[[i]]
            pi += 1
    arr[pi], arr[end] = arr[end], arr[pi]
    return pi


def qs_4(arr, start, end):
    if start < end:
        pi = pi_4(arr, start, end)
        qs_4(arr, start, pi - 1)
        qs_4(arr, pi + 1, end)


def pi_5(arr, start, end):
    pivot = arr[end]
    pi = start
    for i in range(start, end):
        if arr[i] < pivot:
            arr[i], arr[pi] = arr[pi], arr[i]
            pi += 1

    arr[end], arr[pi] = arr[pi], arr[end]
    return pi


def qs_5(arr, start, end):
    if start < end:
        pi = pi_5(arr, start, end)
        qs_5(arr, start, pi - 1)
        qs_5(arr, pi + 1, end)


def pi_6(arr, start, end):
    pivot = arr[end]
    pi = start
    for i in range(start, end):
        if arr[i] < pivot:
            arr[pi], arr[i] = arr[i], arr[pi]
            pi += 1
    arr[pi], arr[end] = arr[end], arr[pi]
    return pi


def qs_6(arr, start, end):
    if start < end:
        pi = pi_6(arr, start, end)
        qs_6(arr, start, pi - 1)
        qs_6(arr, pi + 1, end)


def pi_7(arr, start, end):
    pivot = arr[end]
    potential_index = start
    for i in range(start, end):
        if arr[i] < pivot:
            arr[i], arr[potential_index] = arr[potential_index], arr[i]
            potential_index += 1
    arr[potential_index], arr[end] = arr[end], arr[potential_index]
    return potential_index


def qs_7(arr, start, end):
    if start < end:
        partition_index = pi_7(arr, start, end)
        qs_7(arr, start, partition_index - 1)
        qs_7(arr, partition_index + 1, end)


def partition_8(arr, start, end):
    pivot = arr[end]
    potential_index = start
    for i in range(start, end):
        if arr[i] < pivot:
            arr[i], arr[potential_index] = arr[potential_index], arr[i]
            potential_index += 1
    arr[potential_index], arr[end] = arr[end], arr[potential_index]
    return potential_index


def quick_sort_8(arr, start, end):
    if start < end:
        partition_index = partition_8(arr, start, end)
        quick_sort_8(arr, start, partition_index - 1)
        quick_sort_8(arr, partition_index + 1, end)


def partition_9(arr, start, end):
    pivot = arr[end]
    potential_index = start
    for i in range(start, end):
        if arr[i] < pivot:
            arr[i], arr[potential_index] = arr[potential_index], arr[i]
            potential_index += 1
    arr[potential_index], arr[end] = arr[end], arr[potential_index]
    return potential_index


def quick_sort_9(arr, start, end):
    if start < end:
        partition_index = partition_9(arr, start, end)
        quick_sort_9(arr, start, partition_index - 1)
        quick_sort_9(arr, partition_index + 1, end)


def partition_10(arr, start, end):
    pivot = arr[end]
    potential_index = start
    for i in range(start, end):
        if arr[i] < pivot:
            arr[i], arr[potential_index] = arr[potential_index], arr[i]
            potential_index += 1
    arr[end], arr[potential_index] = arr[potential_index], arr[end]
    return potential_index


def quick_sort_10(arr, start, end):
    if start < end:
        partition_index = partition_10(arr, start, end)
        quick_sort_10(arr, start, partition_index - 1)
        quick_sort_10(arr, partition_index + 1, end)


def partition_11(arr, start, end):
    pivot = arr[end]
    potential_index = start
    for i in range(start, end):
        if arr[i] < pivot:
            arr[potential_index], arr[i] = arr[i], arr[potential_index]
            potential_index += 1
    arr[potential_index], arr[end] = arr[end], arr[potential_index]
    return potential_index


def quick_sort_11(arr, start, end):
    if start < end:
        partition_index = partition_11(arr, start, end)
        quick_sort_11(arr, start, partition_index - 1)
        quick_sort_11(arr, partition_index + 1, end)


def partition_12(arr, start, end):
    pivot = arr[end]
    potential_index = start
    for i in range(start, end):
        if arr[i] < pivot:
            arr[i], arr[potential_index] = arr[potential_index], arr[i]
            potential_index += 1
    arr[end], arr[potential_index] = arr[potential_index], arr[end]
    return potential_index


def quick_sort_12(arr, start, end):
    if start < end:
        partition_index = partition_12(arr, start, end)
        quick_sort_12(arr, start, partition_index - 1)
        quick_sort(arr, partition_index + 1, end)


def partition_13(array, start, end):
    pivot = array[end]
    potential_index = start
    for i in range(start, end):
        if array[i] < pivot:
            array[i], array[potential_index] = array[potential_index], array[i]
            potential_index += 1
    array[end], array[potential_index] = array[potential_index], array[end]
    return potential_index


def quick_sort_13(array, start, end):
    if start < end:
        partition_index = partition_13(array, start, end)
        quick_sort_13(array, start, partition_index - 1)
        quick_sort_13(array, partition_index + 1, end)


def partition_14(array, start, end):
    pivot = array[end]
    potential_index = start
    for i in range(start, end):
        if array[i] < pivot:
            array[i], array[potential_index] = array[potential_index], array[i]
            potential_index += 1
    array[end], array[potential_index] = array[potential_index], array[end]
    return potential_index


def quick_sort_14(array, start, end):
    if start < end:
        partition_index = partition_14(array, start, end)
        quick_sort_14(array, start, partition_index - 1)
        quick_sort_14(array, partition_index + 1, end)


def partition_15(array, start, end):
    pivot = array[end]
    potential_index = start
    for i in range(start, end):
        if array[i] < pivot:
            array[potential_index], array[i] = array[i], array[potential_index]
            potential_index += 1
    array[potential_index], array[end] = array[end], array[potential_index]
    return potential_index


def quick_sort_15(array, start, end):
    if start < end:
        partition_index = partition_15(array, start, end)
        quick_sort_15(array, start, partition_index - 1)
        quick_sort_15(array, partition_index + 1, end)


def partition_16(array, start, end):
    pivot = array[end]
    pi = start
    for i in range(start, end):
        if array[i] < pivot:
            array[i], array[pi] = array[pi], array[i]
            pi += 1
    array[end], array[pi] = array[pi], array[end]
    return pi


def quick_sort_16(array, start, end):
    if start < end:
        partition_index = partition_16(array, start, end)
        quick_sort_16(array, start, partition_index - 1)
        quick_sort_16(array, partition_index + 1, end)


def partition_17(array, start, end):
    pivot = array[end]
    pi = start
    for i in range(start, end):
        if array[i] < pivot:
            array[pi], array[i] = array[i], array[pi]
            pi += 1
    array[end], array[pi] = array[pi], array[end]
    return pi


def quick_sort_17(array, start, end):
    if start < end:
        pi = partition_17(array, start, end)
        quick_sort_17(array, start, pi - 1)
        quick_sort_17(array, pi + 1, end)


def partition_18(array, start, end):
    pivot = array[end]
    pi = start
    for i in range(start, end):
        if array[i] < pivot:
            array[pi], array[i] = array[i], array[pi]
            pi += 1
    array[end], array[pi] = array[pi], array[end]
    return pi


def quick_sort_18(array, start, end):
    if start < end:
        pi = partition_18(array, start, end)
        quick_sort_18(array, start, pi - 1)
        quick_sort_18(array, pi + 1, end)


def partition_19(array, start, end):
    pivot = array[end]
    pi = start
    for i in range(start, end):
        if array[i] < pivot:
            array[i], array[pi] = array[pi], array[i]
            pi += 1
    array[pi], array[end] = array[end], array[pi]
    return pi


def quick_sort_19(array, start, end):
    if start < end:
        pi = partition_19(array, start, end)
        quick_sort_19(array, start, pi - 1)
        quick_sort(array, pi + 1, end)


def partition_20(array, start, end):
    pivot = array[end]
    pi = start
    for i in range(start, end):
        if array[i] < pivot:
            array[i], array[pi] = array[pi], array[i]
            pi += 1
    array[end], array[pi] = array[pi], array[end]
    return pi


def quick_sort_20(array, start, end):
    if start < end:
        pi = partition_20(array, start, end)
        quick_sort_20(array, start, pi - 1)
        quick_sort_20(array, pi + 1, end)


def partition_21(array, start, end):
    pivot = array[end]
    pi = start
    for i in range(start, end):
        if array[i] < pivot:
            array[i], array[pi] = array[pi], array[i]
            pi += 1
    array[end], array[pi] = array[pi], array[end]
    return pi


def quick_sort_21(array, start, end):
    if start < end:
        pi = partition_21(array, start, end)
        quick_sort_21(array, start, pi - 1)
        quick_sort_21(array, pi + 1, end)


def partition_22(array, start, end):
    pivot = array[end]
    pi = start
    for i in range(start, end):
        if array[i] < pivot:
            array[i], array[pi] = array[pi], array[i]
            pi += 1
    array[end], array[pi] = array[pi], array[end]
    return pi


def quick_sort_22(array, start, end):
    if start < end:
        pi = partition_22(array, start, end)
        quick_sort_22(array, start, pi - 1)
        quick_sort_22(array, pi + 1, end)


def partition_23(array, start, end):
    pivot = array[end]
    pi = start

    for i in range(start, end):
        if array[i] < pivot:
            array[i], array[pi] = array[pi], array[i]
            pi += 1

    array[end], array[pi] = array[pi], array[end]
    return pi


def quick_sort_23(array, start, end):
    if start < end:
        pi = partition_23(array, start, end)
        quick_sort_23(array, start, pi - 1)
        quick_sort_23(array, pi + 1, end)


def partition_24(array, start, end):
    pivot = array[end]
    pi = start
    for i in range(start, end):
        if array[i] < pivot:
            array[pi], array[i] = array[i], array[pi]
            pi += 1
    array[end], array[pi] = array[pi], array[end]
    return pi


def quick_sort_24(array, start, end):
    if start < end:
        pi = partition_24(array, start, end)
        quick_sort_24(array, start, pi - 1)
        quick_sort_24(array, pi + 1, end)


# Test cases
test_cases = [
    ([], []),
    ([5], [5]),
    ([4, 10, 3, 5, 1, 10, 3], [1, 3, 3, 4, 5, 10, 10]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([5, -10, 3, -5, 1], [-10, -5, 1, 3, 5])
]

for arr1, expected in test_cases:
    n = len(arr1)
    quick_sort_23(arr1, 0, n - 1)
    assert arr1 == expected, f"Expected: {expected}, Got: {arr1}"

print("All test cases passed!")
print(quick_sort_22(array=[3, 15, 18, 3, 0], start=0, end=4))
