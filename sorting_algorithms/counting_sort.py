def counting_sort_stable(A, B, k):
    C = [0] * (k + 1)

    for num in range(len(A)):
        C[A[num]] += 1
    # Create a cumulative array of C in place of C
    for num in range(1, k + 1):
        C[num] += C[num - 1]
    # Now, fill B as the Sorted A
    for num in range(len(A) - 1, -1, -1):
        B[C[A[num]] - 1] = A[num]
        C[A[num]] -= 1
    return B


def CS_stable_p(A, B, k):
    C = [0] * (k + 1)
    for num in A:
        C[num] += 1
    for num in range(1, k + 1):
        C[num] += C[num - 1]
    for num in range(len(A) - 1, -1, -1):
        B[C[A[num]] - 1] = A[num]
        C[A[num]] -= 1
    return B


def CS_stable_p1(A, B):
    # Calculate the maximum value in A
    k = max(A)
    #  Initialize a temporary count 0 array of size k+1
    C = [0] * (k + 1)
    # Fill C with the frequency count values of its indices in A
    for num in A:
        C[num] += 1
    # Adjust C to get the cumulative array
    for num in range(1, k + 1):
        C[num] += C[num - 1]

    # Fill B with elements from A in sorted order
    # Start from the last element of A
    # Find the index to insert in B by using the cumulative score of A[i]
    for i in range(len(A) - 1, -1, -1):
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1
    return B


def counting_sort_simple(A):
    max_A = max(A)
    C = [0] * (max_A + 1)
    for num in A:
        C[num] += 1

    # Set pointers for A and C
    i = 0  # Pointer for C
    j = 0  # Pointer for A
    # Loop through C and copy the value of index of C in to A at j, as many times as there are elements at C[i]
    while i < (len(C)):
        if C[i] > 0:
            A[j] = i
            j += 1
            C[i] -= 1
        else:
            i += 1
    return A


def CS_simple_p(A):
    max_a = max(A)
    # Create and array of size max+1 and initialize it with zero
    C = [0] * (max_a + 1)
    # Fill C with frequency of index occurrences in A
    for num in A:
        C[num] += 1

    # Fill A in sorted order
    # Initialize pointers for A and C
    i = 0
    j = 0
    # Loop through C from index 0
    while i < (len(C)):
        if C[i] > 0:
            A[j] = i
            C[i] -= 1
            j += 1
        else:
            i += 1
    return A


def CS_stable_p2(A):
    # Get Max value
    k = max(A)
    # Get length of A
    n = len(A)
    # Initialize a count array of length k+1
    C = [0] * (k + 1)
    # Initialize a temporary array of length len(A) to store sorted elements
    B = [0] * n
    # Fill C with the frequency of its index values occurring in A
    for i in range(n):
        C[A[i]] += 1
    # Modify C to Get the cumulative array of values of C
    for i in range(1, len(C)):
        C[i] += C[i - 1]
    # Fill B with elements from A in Sorted Order
    # Start looping over elements from A in reverse order
    # Looping in reverse helps maintain the stability of the sorted elements
    for i in range(n - 1, -1, -1):
        index = C[A[i]]
        B[index - 1] = A[i]
        C[A[i]] -= 1

    # Copy elements from B to A
    for i in range(n):
        A[i] = B[i]


def CS_stable_p3(arr):
    k = max(arr)
    n = len(arr)
    # Create a count array
    C = [0] * (k + 1)
    B = [0] * n
    for i in range(n):
        C[A[i]] += 1
    for i in range(1, len(C)):
        C[i] += C[i - 1]
    for i in range(n - 1, -1, -1):
        index = C[A[i]] - 1
        B[index] = A[i]
        C[A[i]] -= 1
    for i in range(n):
        A[i] = B[i]


def CS_stable_p4(A):
    n = len(A)
    k = max(A)
    C = [0] * (k + 1)
    B = [0] * n
    for i in range(n):
        C[A[i]] += 1
    for i in range(1, k + 1):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1
    for i in range(n):
        A[i] = B[i]


def CS_stable_p5(A):
    n = len(A)
    k = max(A)
    C = [0] * (k + 1)
    B = [0] * n
    for i in range(n):
        C[A[i]] += 1
    for i in range(1, k + 1):
        C[i] += C[i - 1]
    for i in range(n - 1, -1, -1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]
    for i in range(n):
        A[i] = B[i]


def counting_sort_stable_6(arr):
    max_digit = max(arr)
    length_arr = len(arr)
    C = [0] * (max_digit + 1)
    B = [0] * length_arr
    for i in range(length_arr):
        C[A[i]] += 1
    for i in range(1, max_digit + 1):
        C[i] += C[i - 1]

    for i in range(length_arr - 1, -1, -1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]
    for i in range(length_arr):
        A[i] = B[i]


def counting_sort_stable_7(arr):
    max_digit = max(arr)
    length_arr = len(arr)
    C = [0] * (max_digit + 1)
    B = [0] * length_arr
    for i in range(length_arr):
        C[A[i]] += 1
    for i in range(1, max_digit + 1):
        C[i] += C[i - 1]
    for i in range(length_arr - 1, -1, -1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]
    for i in range(length_arr):
        A[i] = B[i]


def counting_sort_stable_8(arr):
    n = len(arr)
    k = max(arr)
    C = [0] * (k + 1)
    B = [0] * n
    for i in range(n):
        C[arr[i]] += 1

    for i in range(1, len(C)):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        C[arr[i]] -= 1
        B[C[arr[i]]] = arr[i]
    for i in range(n):
        arr[i] = B[i]


def counting_sort_stable_9(arr):
    n = len(arr)
    k = max(arr)
    C = [0] * (k + 1)
    B = [0] * n
    for i in range(n):
        C[arr[i]] += 1
    for i in range(1, len(C)):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        C[arr[i]] -= 1
        B[C[arr[i]]] = arr[i]
    for i in range(n):
        arr[i] = B[i]


def counting_sort_stable_10(array):
    k = max(array)
    n = len(array)
    C = [0] * (k + 1)
    B = [0] * n
    for i in range(n):
        C[array[i]] += 1

    for i in range(1, len(C)):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        C[array[i]] -= 1
        B[C[array[i]]] = array[i]
    for i in range(n):
        array[i] = B[i]


def counting_sort_stable_11(array):
    k = max(array)
    n = len(array)
    C = [0] * (k + 1)
    B = [0] * n
    for i in range(n):
        C[array[i]] += 1

    for i in range(1, len(C)):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        C[array[i]] -= 1
        B[C[array[i]]] = array[i]

    for i in range(n):
        array[i] = B[i]


def counting_sort_stable_12(array):
    n = len(array)
    k = max(array)
    C = [0] * (k + 1)
    B = [0] * n
    for i in range(n):
        C[array[i]] += 1
    for i in range(1, len(C)):
        C[i] += C[i - 1]
    for i in range(n - 1, -1, -1):
        C[array[i]] -= 1
        B[C[array[i]]] = array[i]
    for i in range(n):
        array[i] = B[i]


def counting_sort_stable_13(array):
    k = max(array)
    n = len(array)
    C = [0] * (k + 1)
    B = [0] * n

    for i in range(n):
        C[array[i]] += 1

    for i in range(1, k + 1):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        C[array[i]] -= 1
        B[C[array[i]]] = array[i]

    for i in range(n):
        array[i] = B[i]


def counting_sort_stable_14(array):
    k = max(array)
    n = len(array)
    C = [0] * (k + 1)
    B = [0] * n

    for i in range(n):
        C[array[i]] += 1
    for i in range(1, k + 1):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        C[array[i]] -= 1
        B[C[array[i]]] = array[i]

    for i in range(n):
        array[i] = B[i]


def counting_sort_stable_15(arr):
    k = max(arr)
    n = len(arr)
    C = [0] * (k + 1)
    B = [0] * n
    for i in range(n):
        C[arr[i]] += 1

    for i in range(1, k + 1):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        C[arr[i]] -= 1
        B[C[arr[i]]] = arr[i]

    for i in range(n):
        arr[i] = B[i]


def counting_sort_stable_16(arr):
    k = max(arr)
    n = len(arr)
    C = [0] * (k + 1)
    B = [0] * n

    for i in range(n):
        C[arr[i]] += 1

    for i in range(1, k + 1):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        C[arr[i]] -= 1
        B[C[arr[i]]] = arr[i]

    for i in range(n):
        arr[i] = B[i]


def test_counting_sort(counting_sort):
    A = [3, 1, 5, 2, 4]
    counting_sort(A)
    print(A)  # Output should be [1, 2, 3, 4, 5]

    A = [4, 2, 3, 2, 1, 4]
    counting_sort(A)
    print(A)  # Output should be [1, 2, 2, 3, 4, 4]

    import random

    A = [random.randint(1, 10) for _ in range(100)]
    counting_sort(A)
    print(A)  # Output should be a sorted array with stability preserved

    A = [1, 2, 3, 4, 5]
    counting_sort(A)
    print(A)  # Output should be the same sorted array

    A = [5, 4, 3, 2, 1]
    counting_sort(A)
    print(A)  # Output should be [1, 2, 3, 4, 5]


test_counting_sort(counting_sort_stable_16)
