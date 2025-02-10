def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    L = []
    R = []

    for num in range(n1):
        L.append(arr[left + num])

    for num in range(n2):
        R.append(arr[mid + 1 + num])

    i = 0
    j = 0
    k = left
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
            k += 1
        else:
            arr[k] = R[j]
            j += 1
            k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        merge(arr, left, mid, right)


def merge_practice(arr, low, mid, high):
    # Create two temporary arrays to store the left and right portion of the original array
    n1 = mid - low + 1  # Add one to include zero index element
    n2 = high - mid

    # Initialize two empty lists
    L = []
    R = []

    # Fill the two empty lists with left and right portion of the array
    for num in range(n1):
        L.append(arr[num + low])  # Until mid

    for num in range(n2):
        R.append(arr[num + mid + 1])  # One element after mid

    # Loop through both L and R and merge the two in arr in sorted order
    i = 0
    j = 0
    k = low
    while i < n1 and j < n2:
        # Check which of the corresponding elements in i L and R are greater and shift to arr
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
            k += 1
        else:
            arr[k] = R[j]
            j += 1
            k += 1

    # Move the remaining elements from either of the arrays to main arr
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort_practice(arr, left, right):
    if left < right:
        # find the middle element
        mid = (left + right) // 2
        merge_sort_practice(arr, left, mid)
        merge_sort_practice(arr, mid + 1, right)
        merge_practice(arr, left, mid, right)


def merge_practice1(arr, left, mid, right):
    # Create two temporary arrays to store the left and right portion of the original array
    n1 = mid - left + 1
    n2 = right - mid

    # Initialize two empty lists to store
    L = []
    R = []

    # Fill these two empty lists with left and right portion
    for num in range(n1):
        L.append(arr[num + left])

    for num in range(n2):
        R.append(arr[num + mid + 1])

    # Merge the two left and right lists in to the original list in sorted order
    # Declare pointers for the first elements in each of L, R and arr
    i = 0
    j = 0
    k = left
    while i < n1 and j < n2:
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
            k += 1
        else:
            arr[k] = R[j]
            j += 1
            k += 1
    # Move the remaining elements from either of the two arrays into the original array

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort_practice1(arr, left, right):
    if left < right:
        # find the mid
        mid = (left + right) // 2
        # Call Merge sort on left portion
        merge_sort_practice1(arr, left, mid)
        # Call merge sort on right portion
        merge_sort_practice1(arr, mid + 1, right)
        # Merge the two sorted array
        merge_practice1(arr, left, mid, right)


def merge_practice2(arr, low, mid, high):
    # Form two empty arrays
    n1 = mid - low + 1
    n2 = high - mid
    L = []
    R = []
    for num in range(n1):
        L.append(arr[low + num])
    for num in range(n2):
        R.append(arr[mid + 1 + num])

    i = 0
    j = 0
    k = low
    while i < n1 and j < n2:
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
            k += 1
        else:
            arr[k] = R[j]
            j += 1
            k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort_practice2(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort_practice2(arr, low, mid)
        merge_sort_practice2(arr, mid + 1, high)
        merge_practice2(arr, low, mid, high)


def m_p3(arr, start, mid, end):
    n1 = mid - start + 1
    n2 = end - mid
    L = []
    R = []
    for i in range(n1):
        L.append(arr[start + i])
    for i in range(n2):
        R.append(arr[mid + 1 + i])
    i = 0
    j = 0
    k = start
    while i < n1 and j < n2:
        if L[i] < R[j]:
            arr[k] = L[i]
            k += 1
            i += 1
        else:
            arr[k] = R[j]
            j += 1
            k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def ms_p3(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        ms_p3(arr, start, mid)
        ms_p3(arr, mid + 1, end)
        m_p3(arr, start, mid, end)


def m_p4(arr, start, mid, end):
    n1 = mid - start + 1
    n2 = end - mid

    L = []
    R = []

    for i in range(n1):
        L.append(arr[start + i])
    for i in range(n2):
        R.append(arr[mid + 1 + i])

    i = 0
    j = 0
    k = start

    while i < n1 and j < n2:
        if L[i] < R[j]:
            arr[k] = L[i]
            k += 1
            i += 1
        else:
            arr[k] = R[j]
            j += 1
            k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        k += 1
        j += 1


def ms_p4(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        ms_p4(arr, start, mid)
        ms_p4(arr, mid + 1, end)
        m_p4(arr, start, mid, end)


def m_p5(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    L = []
    R = []

    for i in range(n1):
        L.append(arr[left + i])

    for i in range(n2):
        R.append(arr[mid + 1 + i])

    i = 0
    j = 0
    k = left
    while i < n1 and j < n2:
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
            k += 1
        else:
            arr[k] = R[j]
            j += 1
            k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def ms_p5(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        ms_p5(arr, left, mid)
        ms_p5(arr, mid + 1, right)
        m_p5(arr, left, mid, right)


def m_p6(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    L = []
    R = []
    for i in range(n1):
        L.append(arr[left + i])
    for i in range(n2):
        R.append(arr[mid + 1 + i])

    i = 0
    j = 0
    k = left
    while i < n1 and j < n2:
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
            k += 1
        else:
            arr[k] = R[j]
            j += 1
            k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        k += 1
        j += 1


def ms_p6(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        ms_p6(arr, start, mid)
        ms_p6(arr, mid + 1, end)
        m_p6(arr, start, mid, end)


def merge_7(arr, start, mid, end):
    n1 = mid - start + 1
    n2 = end - mid
    L = []
    R = []
    for i in range(n1):
        L.append(arr[start + i])
    for i in range(n2):
        R.append(arr[mid + 1 + i])

    i = 0
    j = 0
    k = start
    while i < n1 and j < n2:
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
            k += 1
        else:
            arr[k] = R[j]
            j += 1
            k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort_7(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort_7(arr, start, mid)
        merge_sort_7(arr, mid + 1, end)
        merge_7(arr, start, mid, end)


def merge_8(arr, start, mid, end):
    n1 = mid - start + 1
    n2 = end - mid
    L = []
    R = []
    for i in range(n1):
        L.append(arr[start + i])
    for i in range(n2):
        R.append(arr[mid + 1 + i])
    i = 0
    j = 0
    k = start
    while i < n1 and j < n2:
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
            k += 1
        else:
            arr[k] = R[j]
            j += 1
            k += 1
    while i < n1:
        arr[k] = L[i]
        k += 1
        i += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort_8(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort_8(arr, start, mid)
        merge_sort_8(arr, mid + 1, end)
        merge_8(arr, start, mid, end)


def merge_9(array, start, mid, end):
    n1 = mid - start + 1
    n2 = end - mid

    L = []
    R = []

    for i in range(n1):
        L.append(array[start + i])
    for i in range(n2):
        R.append(array[mid + 1 + i])

    i = j = 0
    k = start

    while i < n1 and j < n2:
        if L[i] < R[j]:
            array[k] = L[i]
            i += 1
            k += 1
        else:
            array[k] = R[j]
            j += 1
            k += 1

    while i < n1:
        array[k] = L[i]
        k += 1
        i += 1

    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1


def merge_sort_9(array, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort_9(array, start, mid)
        merge_sort_9(array, mid + 1, end)
        merge_9(array, start, mid, end)


def merge_10(array, start, mid, end):
    n1 = mid - start + 1
    n2 = end - mid

    L = []
    R = []

    for i in range(n1):
        L.append(array[start + i])

    for i in range(n2):
        R.append(array[mid + 1 + i])

    i = j = 0
    k = start

    while i < n1 and j < n2:
        if L[i] < R[j]:
            array[k] = L[i]
            i += 1
            k += 1
        else:
            array[k] = R[j]
            k += 1
            j += 1

    while i < n1:
        array[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1


def merge_sort_10(array, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort_10(array, start, mid)
        merge_sort_10(array, mid + 1, end)
        merge_10(array, start, mid, end)


def merge_11(array, start, mid, end):
    n1 = mid - start + 1
    n2 = end - mid

    L = []
    R = []

    for i in range(n1):
        L.append(array[start + i])

    for i in range(n2):
        R.append(array[mid + 1 + i])

    i = j = 0
    k = start

    while i < n1 and j < n2:
        if L[i] < R[j]:
            array[k] = L[i]
            i += 1
            k += 1
        else:
            array[k] = R[j]
            k += 1
            j += 1

    while i < n1:
        array[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1


def merge_sort_11(array, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort_11(array, start, mid)
        merge_sort_11(array, mid + 1, end)
        merge_11(array, start, mid, end)


def merge_12(array, start, mid, end):
    n1 = mid - start + 1
    n2 = end - mid
    L = []
    R = []
    for i in range(n1):
        L.append(array[start + i])
    for i in range(n2):
        R.append(array[mid + 1 + i])
    i = j = 0
    k = start
    while i < n1 and j < n2:
        if L[i] < R[j]:
            array[k] = L[i]
            i += 1
            k += 1
        else:
            array[k] = R[j]
            j += 1
            k += 1
    while i < n1:
        array[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1


def merge_sort_12(array, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort_12(array, start, mid)
        merge_sort_12(array, mid + 1, end)
        merge_12(array, start, mid, end)


def merge_13(array, start, mid, end):
    n1 = mid - start + 1
    n2 = end - mid

    L = []
    R = []

    for i in range(n1):
        L.append(array[start + i])
    for i in range(n2):
        R.append(array[mid + 1 + i])

    i = j = 0
    k = start

    while i < n1 and j < n2:
        if L[i] < R[j]:
            array[k] = L[i]
            i += 1
            k += 1
        else:
            array[k] = R[j]
            j += 1
            k += 1
    while i < n1:
        array[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1


def merge_sort_13(array, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort_13(array, start, mid)
        merge_sort_13(array, mid + 1, end)
        merge_13(array, start, mid, end)


def merge_14(array, start, mid, end):
    n1 = mid - start + 1
    n2 = end - mid
    L = []
    R = []

    for i in range(n1):
        L.append(array[start + i])

    for i in range(n2):
        R.append(array[mid + 1 + i])

    i = j = 0
    k = start

    while i < n1 and j < n2:
        if L[i] < R[j]:
            array[k] = L[i]
            i += 1
            k += 1
        else:
            array[k] = R[j]
            j += 1
            k += 1

    while i < n1:
        array[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1


def merge_sort_14(array, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort_14(array, start, mid)
        merge_sort_14(array, mid + 1, end)
        merge_14(array, start, mid, end)


def merge_15(array, start, mid, end):
    n1 = mid - start + 1
    n2 = end - mid
    L = []
    R = []
    for i in range(n1):
        L.append(array[start + i])
    for i in range(n2):
        R.append(array[mid + 1 + i])

    i = j = 0
    k = start

    while i < n1 and j < n2:
        if L[i] < R[j]:
            array[k] = L[i]
            i += 1
            k += 1
        else:
            array[k] = R[j]
            j += 1
            k += 1
    while i < n1:
        array[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1


def merge_sort_15(array, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort_15(array, start, mid)
        merge_sort_15(array, mid + 1, end)
        merge_15(array, start, mid, end)


def merge_16(array, start, mid, end):
    n1 = mid - start + 1
    n2 = end - mid
    L = []
    R = []

    for i in range(n1):
        L.append(array[start + i])
    for j in range(n2):
        R.append(array[mid + 1 + j])
    i = j = 0
    k = start
    while i < n1 and j < n2:
        if L[i] < R[j]:
            array[k] = L[i]
            i += 1
            k += 1
        else:
            array[k] = R[j]
            j += 1
            k += 1
    while i < n1:
        array[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1


def merge_sort_16(array, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort_16(array, start, mid)
        merge_sort_16(array, mid + 1, end)
        merge_16(array, start, mid, end)


def merge_17(array, start, mid, end):
    n1 = mid - start + 1
    n2 = end - mid

    L = []
    R = []

    for i in range(n1):
        L.append(array[start + i])
    for j in range(n2):
        R.append(array[mid + 1 + j])

    i = j = 0
    k = start
    while i < n1 and j < n2:
        if L[i] < R[j]:
            array[k] = L[i]
            i += 1
            k += 1
        else:
            array[k] = R[j]
            j += 1
            k += 1
    while i < n1:
        array[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1


def merge_sort_17(array, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort_17(array, start, mid)
        merge_sort_17(array, mid + 1, end)
        merge_17(array, start, mid, end)


def merge_18(array, start, mid, end):
    n1 = mid - start + 1
    n2 = end - mid

    L = []
    R = []
    for i in range(n1):
        L.append(array[start+i])

    for j in range(n2):
        R.append(array[mid+1+j])

    i = j = 0
    k = start
    while i < n1 and j < n2:
        if L[i] < R[j]:
            array[k] = L[i]
            i += 1
            k += 1
        else:
            array[j] = R[j]
            j += 1
            k += 1
    while i < n1:
        array[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1


def merge_sort_18(array, start, end):
    if start < end:
        mid = (start+end) // 2
        merge_sort(array, start, mid)
        merge_sort(array, mid+1, end)
        merge(array, start, mid, end)


def merge_19(array, start, mid, end):
    n1 = mid - start + 1
    n2 = end - mid

    L = []
    R = []
    for i in range(n1):
        L.append(array[start+i])

    for j in range(n2):
        R.append(array[mid+1+j])

    i = j = 0
    k = start

    while i < n1 and j < n2:
        if L[i] < R[j]:
            array[k] = L[i]
            i += 1
            k += 1
        else:
            array[k] = R[j]
            j += 1
            k += 1
    while i < n1:
        array[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1

def merge_sort_19(array, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort_19(array, start, mid)
        merge_sort_19(array, mid+1, end)
        merge_19(array, start, mid, end)



def test_merge_sort(merge_sort_test):
    # Test case 1: Random array
    arr1 = [-12, 11, -13, 5, 6, 7]
    merge_sort_test(arr1, 0, len(arr1) - 1)
    print("Sorted array:", arr1)
    # Expected output: [5, 6, 7, 11, 12, 13]

    # Test case 2: Already sorted array
    arr2 = [1, 2, 3, 4, 5]
    merge_sort_test(arr2, 0, len(arr2) - 1)
    print("Sorted array:", arr2)
    # Expected output: [1, 2, 3, 4, 5]

    # Test case 3: Reverse sorted array
    arr3 = [50, 41, 33, 24, 15]
    merge_sort_test(arr3, 0, len(arr3) - 1)
    print("Sorted array:", arr3)
    # Expected output: [1, 2, 3, 4, 5]

    # Test case 4: Array with duplicate elements
    arr4 = [5, 2, 8, 2, 5, 7, 3, 5]
    merge_sort_test(arr4, 0, len(arr4) - 1)
    print("Sorted array:", arr4)
    # Expected output: [2, 2, 3, 5, 5, 5, 7, 8]

    arr = []
    merge_sort_test(arr, 0, len(arr) - 1)
    assert arr == []

    arr = [5]
    merge_sort_test(arr, 0, len(arr) - 1)
    assert arr == [5]

    arr = [1, 2, 3, 4, 5]
    merge_sort_test(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3, 4, 5]

    arr = [5, 4, 3, 2, 1]
    merge_sort_test(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3, 4, 5]

    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    merge_sort_test(arr, 0, len(arr) - 1)
    assert arr == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

    print("All arrays sorted")


test_merge_sort(merge_sort_18)
