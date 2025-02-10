def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


def selection_sort_1(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]


def selection_sort_2(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]


def selection_sort_3(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]


def selection_sort_4(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]


def selection_sort_5(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]


def selection_sort_6(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]


def selection_sort_7(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]



def test_selection_sort(selection_sort_test):
    arr = [5]
    selection_sort_test(arr)
    assert arr == [5]
    arr = []
    selection_sort_test(arr)
    assert arr == []
    arr = [1, 2, 3, 4, 5]
    selection_sort_test(arr)
    assert arr == [1, 2, 3, 4, 5]
    arr = [5, 4, 3, 2, 1]
    selection_sort_test(arr)
    assert arr == [1, 2, 3, 4, 5]
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    selection_sort_test(arr)
    assert arr == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    print("All arrays sorted")


test_selection_sort(selection_sort_6)