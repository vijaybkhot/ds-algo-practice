class MaxBinaryHeap:
    def __init__(self):
        self.values = []

    def insert_element(self, element):
        self.values.append(element)
        self.bubble_up()

    def bubble_up(self):
        index = len(self.values) - 1
        while index > 0:
            parent_index = (index - 1) // 2
            if self.values[index] <= self.values[parent_index]:
                break
            else:
                self.values[parent_index], self.values[index] = self.values[index], self.values[parent_index]
                index = parent_index

    def delete(self):
        if len(self.values) > 1:
            self.values[0], self.values[-1] = self.values[-1], self.values[0]
            root = self.values.pop()
            i = 0
            j = (2 * i) + 1
            while j < len(self.values):
                if j < len(self.values) - 1 and self.values[j + 1] > self.values[j]:
                    j = j + 1
                if self.values[j] > self.values[i]:
                    temp = self.values[i]
                    self.values[i] = self.values[j]
                    self.values[j] = temp
                    i = j
                    j = (2 * i) + 1
                else:
                    break
            return root
        elif len(self.values) == 1:
            return self.values.pop()
        else:
            return None

    # Optional to using delete function extract max
    def max_heapify(self, node, size):
        largest = node
        j = (2 * node) + 1
        if j < size - 1 and self.values[j + 1] > self.values[j]:
            j = j + 1
        if self.values[largest] < self.values[j]:
            # Swap largest with j
            self.values[largest], self.values[j] = self.values[j], self.values[largest]
            largest = j
            self.max_heapify(largest, size)

    def build_max_heap(self):
        n = len(self.values)
        for i in range(n // 2 - 1, -1, -1):
            self.max_heapify(i, n)
        # Or
        # for element in self.values:
        #     self.insert_element(element)

    # def delete_practice(self):
    #     if len(self.values) > 1:
    #         # Swap first and last element
    #         self.values[0], self.values[-1] = self.values[-1], self.values[0]
    #         # Store the original root to return
    #         root = self.values.pop()
    #         # Store index as 0
    #         i = 0
    #         # Store left child index as 2i+1
    #         j = 2*i + 1
    #         # Bubble down the new root to maintain heap property
    #         # Loop while child index is inside the array length
    #         while j < len(self.values):
    #             # Check if the index 'i' also has a right child and if that right child is greater that left child
    #             if j < (len(self.values) - 1) and self.values[j] < self.values[j+1]
    #                 # Set j to right child
    #                 j = j+1
    #             # Check if parent is not smaller than the child
    #             if self.values[j] <= self.values[i]:
    #                 break
    #             else:
    #                 # Swap parent and child
    #                 self.values[j], self.values[i] = self.values[i], self.values[j]
    #                 i = j
    #                 j = (2*i) + 1
    #         # Return the original root
    #         return root
    #     elif len(self.values) == 1:
    #         return self.values.pop()
    #     else:
    #         return None


# Practice code
# def heap_insert(arr, key):
#     arr.append(key)
#     index = len(arr) - 1
#     while index > 0:
#         parent_index = (index - 1) // 2
#         if key <= arr[parent_index]:
#             break
#         else:
#             arr[index], arr[parent_index] = arr[parent_index], arr[index]
#             index = parent_index
#     print(arr)

# Lengthy extract_max():
# def extract_max(self):
#     if not self.values:
#         return None
#     elif len(self.values) > 1:
#         self.values[-1], self.values[0] = self.values[0], self.values[-1]  # Swap the first and last elements
#         root = self.values.pop()  # Store the original root
#         parent_index = 0
#         parent_element = self.values[0]
#         last_index = len(self.values) - 1
#
#         while True:
#             left_child = right_child = None
#             left_child_index = (parent_index * 2) + 1
#             right_child_index = (parent_index * 2) + 2
#             if left_child_index <= last_index:
#                 left_child = self.values[left_child_index]
#             if right_child_index <= last_index:
#                 right_child = self.values[right_child_index]
#             if left_child and right_child:
#                 max_child_index = self.values.index(max(left_child, right_child))
#                 if self.values[max_child_index] > parent_element:
#                     self.values[parent_index] = self.values[max_child_index]
#                     self.values[max_child_index] = parent_element
#                     parent_index = max_child_index
#                     parent_element = self.values[parent_index]
#                 else:
#                     break
#             elif left_child and not right_child:
#                 if left_child > parent_element:
#                     self.values[parent_index] = left_child
#                     self.values[left_child_index] = parent_element
#                     parent_index = left_child_index
#                     parent_element = self.values[parent_index]
#                 else:
#                     break
#             elif right_child and not left_child:
#                 if right_child > parent_element:
#                     self.values[parent_index] = right_child
#                     self.values[right_child_index] = parent_element
#                     parent_index = right_child_index
#                     parent_element = self.values[parent_index]
#                 else:
#                     break
#             else:
#                 break
#         return root
#     else:
#         return self.values.pop()


def heap_insert_practice1(arr, element):
    arr.append(element)
    index = len(arr) - 1
    while index > 0:
        parent_index = (index - 1) // 2
        if arr[index] <= arr[parent_index]:
            break
        else:
            arr[index], arr[parent_index] = arr[parent_index], arr[index]
            index = parent_index


def delete_practice1(arr):
    if len(arr) > 1:
        arr[0], arr[-1] = arr[-1], arr[0]
        root = arr.pop()
        index = 0
        j = (2 * index) + 1
        while j < len(arr):
            if j < len(arr) - 1 and arr[j] < arr[j + 1]:
                j = j + 1
            if arr[index] < arr[j]:
                arr[index], arr[j] = arr[j], arr[index]
                index = j
                j = (2 * index) + 1
            else:
                break  # Don't forget to break the loop
        return root
    elif len(arr) == 1:
        return arr.pop()
    else:
        return None


def build_heap_practice1(arr):
    heap = []
    for i in arr:
        heap_insert_practice1(heap, i)
    return heap


def heap_sort_practice1(arr):
    sorted_arr = []
    heap = build_heap_practice1(arr)
    for i in range(len(heap)):
        sorted_arr.insert(0, delete_practice1(heap))
    return sorted_arr


def heap_insert_p2(arr, element):
    arr.append(element)
    index = len(arr) - 1
    while index > 0:
        pi = (index - 1) // 2
        if arr[pi] < arr[index]:
            arr[pi], arr[index] = arr[index], arr[pi]
            index = pi
        else:
            break


def delete_p2(arr):
    if len(arr) > 1:
        arr[0], arr[-1] = arr[-1], arr[0]
        root = arr.pop()
        i = 0
        j = 2 * i + 1
        while j < len(arr):
            if j < len(arr) - 1 and arr[j] < arr[j + 1]:
                j = j + 1
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                i = j
                j = 2 * i + 1
            else:
                break
        return root
    elif len(arr) == 1:
        return arr.pop()
    else:
        return None


def build_heap_2(arr):
    heap = []
    for i in arr:
        heap_insert_p2(heap, i)
    return heap


def heap_sort_2(arr):
    heap = build_heap_2(arr)
    sorted_arr = []
    for i in range(len(heap)):
        sorted_arr.insert(0, delete_p2(heap))
    return sorted_arr


def heap_insert_3(arr, element):
    arr.append(element)
    i = len(arr) - 1
    while i > 0:
        j = (i - 1) // 2
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
            i = j
        else:
            break


def delete_3(arr):
    n = len(arr)
    if n > 1:
        arr[0], arr[-1] = arr[-1], arr[0]
        root = arr.pop()
        parent_index = 0
        child_index = 2 * parent_index + 1
        while child_index < n - 1:
            if child_index < n - 2 and arr[child_index] < arr[child_index + 1]:
                child_index = child_index + 1
            if arr[parent_index] < arr[child_index]:
                arr[parent_index], arr[child_index] = arr[child_index], arr[parent_index]
                parent_index = child_index
                child_index = 2 * parent_index + 1
            else:
                break
        return root
    elif n == 1:
        return arr.pop()
    else:
        return None


def build_heap_3(arr):
    heap = []
    for i in arr:
        heap_insert_3(heap, i)
    return heap


def heap_sort_3(arr):
    heap = build_heap_3(arr)
    sorted_array = []
    for i in range(len(arr)):
        sorted_array.insert(0, delete_3(heap))
    return sorted_array


def heap_insert_4(arr, element):
    arr.append(element)
    element_index = len(arr) - 1
    while element_index > 0:
        parent_index = (element_index - 1) // 2
        if arr[element_index] > arr[parent_index]:
            arr[element_index], arr[parent_index] = arr[parent_index], arr[element_index]
            element_index = parent_index
        else:
            break


def delete_4(arr):
    if len(arr) > 1:
        arr[0], arr[-1] = arr[-1], arr[0]
        root = arr.pop()
        index = 0
        child_index = (2 * index) + 1
        while child_index < len(arr):
            if child_index < len(arr) - 1 and arr[child_index] < arr[child_index + 1]:
                child_index = child_index + 1
            if arr[child_index] > arr[index]:
                arr[child_index], arr[index] = arr[index], arr[child_index]
                index = child_index
                child_index = (2 * index) + 1
            else:
                break
        return root
    elif len(arr) == 1:
        return arr.pop()
    else:
        return None


def build_heap_4(arr):
    heap = []
    for i in range(len(arr)):
        heap_insert_4(heap, arr[i])
    return heap


def heap_sort_4(arr):
    heap = build_heap_4(arr)
    sorted_array = []
    for i in range(len(heap)):
        sorted_array.insert(0, delete_4(heap))
    return sorted_array


def heap_insert_5(array, element: int):
    array.append(element)
    element_index = len(array) - 1
    element = array[element_index]
    while element_index > 0:
        parent_index = (element_index - 1) // 2
        parent = array[parent_index]
        if parent < element:
            array[element_index] = parent
            element_index = parent_index
        else:
            break
    array[element_index] = element


def delete_5(array):
    if len(array) > 1:
        array[0], array[-1] = array[-1], array[0]
        root = array.pop()
        index = 0
        child_index = (2 * index) + 1
        while child_index < len(array):
            if child_index < len(array) - 1 and array[child_index] < array[child_index + 1]:
                child_index = child_index + 1
            if array[index] < array[child_index]:
                array[index], array[child_index] = array[child_index], array[index]
                index = child_index
                child_index = (2 * index) + 1
            else:
                break
        return root
    elif len(array) == 1:
        return array.pop()
    else:
        return None


def build_heap_5(array):
    heap = []
    for i in range(len(array)):
        heap_insert_5(heap, array[i])
    return heap


def heap_sort_5(array):
    heap = build_heap_5(array)
    sorted_array = []
    for i in range(len(heap)):
        sorted_array.insert(0, delete_5(heap))
    return sorted_array


def heap_insert_6(array, element):
    array.append(element)
    index = len(array) - 1
    key = array[index]
    while index > 0:
        parent_index = (index - 1) // 2
        if array[parent_index] < key:
            array[index] = array[parent_index]
            index = parent_index
        else:
            break
    array[index] = key


def delete_6(array):
    if len(array) > 1:
        array[0], array[-1] = array[-1], array[0]
        root = array.pop()
        index = 0
        child_index = (2 * index) + 1
        while child_index < len(array):
            if child_index < len(array) - 1 and array[child_index] < array[child_index + 1]:
                child_index = child_index + 1

            if array[index] < array[child_index]:
                array[child_index], array[index] = array[index], array[child_index]
                index = child_index
                child_index = (2 * index) + 1
            else:
                break
        return root
    elif len(array) == 1:
        return array.pop()
    else:
        return None


def build_heap_6(array):
    heap = []
    for i in range(len(array)):
        heap_insert_6(heap, array[i])
    return heap


def heap_sort_6(array):
    heap = build_heap_5(array)
    sorted_array = []
    for i in range(len(heap)):
        sorted_array.insert(0, delete_5(heap))
    return sorted_array


def heap_insert_7(array, element):
    array.append(element)
    index = len(array) - 1
    element = array[index]
    while index > 0:
        parent_index = (index - 1) // 2
        if array[parent_index] >= element:
            break
        else:
            array[index] = array[parent_index]
            index = parent_index
    array[index] = element


def delete_7(array):
    if len(array) > 1:
        array[0], array[-1] = array[-1], array[0]
        root = array.pop()
        index = 0
        child_index = (2 * index) + 1
        while child_index < len(array):
            if child_index < len(array) - 1 and array[child_index] < array[child_index + 1]:
                child_index += 1
            if array[index] < array[child_index]:
                array[index], array[child_index] = array[child_index], array[index]
                index = child_index
                child_index = (2 * index) + 1
            else:
                break
        return root
    elif len(array) == 1:
        return array.pop()
    else:
        return None


def build_heap_7(array):
    heap = []
    for num in array:
        heap_insert_7(heap, num)
    return heap


def heap_sort_7(array):
    heap = build_heap_7(array)
    sorted_array = []
    for i in range(len(array)):
        sorted_array.insert(0, delete_7(heap))
    return sorted_array


def heap_insert_8(array, element):
    array.append(element)
    index = len(array) - 1
    key = array[index]
    while index > 0:
        parent_index = (index - 1) // 2
        if array[parent_index] < key:
            array[index] = array[parent_index]
            index = parent_index
        else:
            break
    array[index] = key
    return array


def delete_8(array):
    if len(array) > 1:
        array[0], array[-1] = array[-1], array[0]
        root = array.pop()
        index = 0
        child_index = (2 * index) + 1
        while child_index < len(array):
            if child_index < len(array) - 1 and array[child_index] < array[child_index + 1]:
                child_index += 1
            if array[child_index] > array[index]:
                array[child_index], array[index] = array[index], array[child_index]
                index = child_index
                child_index = (2 * index) + 1
            else:
                break
        return root
    elif len(array) == 1:
        return array.pop()
    else:
        return None


def build_heap_8(array):
    heap = []
    for num in array:
        heap_insert_8(heap, num)
    return heap


def heap_sort_8(array):
    heap = build_heap_8(array)
    sorted_array = []
    for i in range(len(heap)):
        sorted_array.insert(0, delete_8(heap))
    return sorted_array


def heap_insert_9(array, element):
    array.append(element)
    index = len(array) - 1
    key = array[index]
    while index > 0:
        parent_index = (index - 1) // 2
        parent = array[parent_index]
        if parent < key:
            array[index] = parent
            index = parent_index
        else:
            break
    array[index] = key
    return array


def delete_9(array):
    if len(array) > 1:
        array[0], array[-1] = array[-1], array[0]
        max_element = array.pop()
        index = 0
        child_index = 2 * index + 1
        while child_index < len(array):
            if child_index < len(array) - 1 and array[child_index] < array[child_index + 1]:
                child_index += 1
            if array[child_index] > array[index]:
                array[child_index], array[index] = array[index], array[child_index]
                index = child_index
                child_index = 2 * index + 1
            else:
                break
        return max_element
    elif len(array) == 1:
        return array.pop()
    else:
        return None


def build_heap_9(array):
    heap = []
    for i in range(len(array)):
        heap_insert_9(heap, array[i])
    return heap


def heap_sort_9(array):
    heap = build_heap_9(array)
    sorted_array = []
    for i in range(len(array)):
        sorted_array.insert(0, delete_9(heap))
    return sorted_array


def heapify_floyd_9(array, n, i):
    largest = i
    left_child_index = (2 * i) + 1
    right_child_index = (2 * i) + 2

    if left_child_index < n and array[left_child_index] > array[largest]:
        largest = left_child_index
    if right_child_index < n and array[right_child_index] > array[largest]:
        largest = right_child_index
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify_floyd_9(array, n, largest)


def build_heap_floyd_9(array):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        heapify_floyd_9(array, n, i)
    return array


def heap_insert_10(array, element):
    array.append(element)
    index = len(array) - 1
    key = array[index]
    while index > 0:
        parent_index = (index - 1) // 2
        parent = array[parent_index]
        if parent < key:
            array[index] = parent
            index = parent_index
        else:
            break
    array[index] = key
    return array


def heapify_floyd_10(array, n, i):
    largest = i
    left_child_index = 2 * i + 1
    right_child_index = 2 * i + 2

    if left_child_index < n and array[left_child_index] > array[largest]:
        largest = left_child_index
    if right_child_index < n and array[right_child_index] > array[largest]:
        largest = right_child_index
    if i != largest:
        array[largest], array[i] = array[i], array[largest]
        heapify_floyd_10(array, n, largest)


def build_heap_floyd_10(array):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        heapify_floyd_10(array, n, i)
    return array


def heap_sort_10(array):
    n = len(array)
    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify_floyd_10(array, n, i)
    # Extract elements one by one

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify_floyd_10(array, i, 0)


def delete_10(array):
    if len(array) > 1:
        array[0], array[-1] = array[-1], array[0]
        max_element = array.pop()
        index = 0
        child_index = 2 * index + 1
        while child_index < len(array):
            if child_index < len(array) - 1 and array[child_index] < array[child_index + 1]:
                child_index += 1
            if array[index] < array[child_index]:
                array[index], array[child_index] = array[index], array[child_index]
                index = child_index
                child_index = 2 * index + 1
            else:
                break
        return max_element
    elif len(array) == 1:
        return array.pop()
    else:
        return None


def heap_insert(array, element):
    array.append(element)
    index = len(array) - 1
    key = array[index]
    while index > 0:
        parent_index = (i - 1) // 2
        parent = array[parent_index]
        if parent < key:
            array[index] = parent
            index = parent_index
        else:
            break
    array[index] = key
    return array


def heapify_floyd_11(array, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and array[left] > array[largest]:
        largest = left
    if right < n and array[right] > array[largest]:
        largest = right
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify_floyd_11(array, n, largest)


def build_heap_floyd_11(array):
    n = len(array)

    for i in range(n // 2 - 1, -1, -1):
        heapify_floyd_11(array, n, i)
    return array


def heap_sort_11(array):
    n = len(array)

    for i in range(n // 2 - 1, -1, -1):
        heapify_floyd_11(array, n, i)

    for i in range(n - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heapify_floyd_11(array, i, 0)


def heap_insert_12(array, element):
    array.append(element)
    index = len(array) - 1
    while index > 0:
        parent_index = (index - 1) // 2
        if array[parent_index] < array[index]:
            array[index], array[parent_index] = array[parent_index], array[index]
            index = parent_index
        else:
            break
    return array


def heapify_floyd_12(array, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and array[left] > array[largest]:
        largest = left
    if right < n and array[right] > array[largest]:
        largest = right

    if i != largest:
        array[i], array[largest] = array[largest], array[i]
        heapify_floyd_12(array, n, largest)


def build_heap_floyd_12(array):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        heapify_floyd_12(array, n, i)
    return array


def heap_sort_12(array):
    n = len(array)

    for i in range(n // 2 - 1, -1, -1):
        heapify_floyd_12(array, n, i)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify_floyd_12(array, i, 0)


def delete_12(array):
    if len(array) > 1:
        array[0], array[-1] = array[-1], array[0]
        root = array.pop()
        index = 0
        child_index = 2 * index + 1
        while child_index < len(array):
            if child_index < len(array) - 1 and array[child_index] < array[child_index + 1]:
                child_index += 1
            if array[index] < array[child_index]:
                array[index], array[child_index] = array[child_index], array[index]
                index = child_index
                child_index = 2 * index + 1
            else:
                break
        return root
    elif len(array) == 1:
        return array.pop()
    else:
        return None


def heapify_floyd_13(arr, n, idx):
    largest = idx
    left = 2 * idx + 1
    right = 2 * idx + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != idx:
        arr[largest], arr[idx] = arr[idx], arr[largest]
        heapify_floyd_13(arr, n, largest)


def heap_sort_13(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify_floyd_13(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify_floyd_13(arr, i, 0)
    return arr


def heapify_min_14(arr, n, idx):
    smallest = idx
    left = 2 * idx + 1
    right = 2 * idx + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left

    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if idx != smallest:
        arr[idx], arr[smallest] = arr[smallest], arr[idx]
        heapify_min_14(arr, n, smallest)


def heap_sort_14(arr):
    n = len(arr)
    # Build min Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify_min_14(arr, n, i)

    # Heap Sort
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify_min_14(arr, i, 0)
    return arr[::-1]


def heapify_max_15(arr, n, idx):
    largest = idx
    left = 2 * idx + 1
    right = 2 * idx + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != idx:
        arr[largest], arr[idx] = arr[idx], arr[largest]
        heapify_max_15(arr, n, largest)


def heap_sort_15(arr):
    n = len(arr)
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify_max_15(arr, n, i)

    # Heap Sort using the max heap
    for i in range(n - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify_max_15(arr, i, 0)


def heapify_max_16(array, n, idx):
    largest = idx
    left = 2 * idx + 1
    right = 2 * idx + 2

    if left < n and array[left] > array[largest]:
        largest = left

    if right < n and array[right] > array[largest]:
        largest = right

    if idx != largest:
        array[idx], array[largest] = array[largest], array[idx]
        heapify_max_16(array, n, largest)


def heap_sort_16(array):
    n = len(array)
    # Build Max-Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify_max_16(array, n, i)

    # Heap sort
    for i in range(n - 1, -1, -1):
        array[0], array[i] = array[i], array[0]
        heapify_max_16(array, i, 0)


# # Test heap_insert
# array = [10, 7, 8, 3, 1, 6, 5]
# element = 4
# expected_result = [10, 7, 8, 4, 1, 6, 5, 3]
# assert heap_insert_12(array, element) == expected_result
#
# # Test heapify_floyd_10
# array = [10, 5, 3, 4, 1]
# n = len(array)
# i = 0
# heapify_floyd_12(array, n, i)
# expected_result = [10, 5, 3, 4, 1]
# assert array == expected_result
#
# # Test build_heap_floyd
# array = [4, 10, 3, 5, 1]
# expected_result = [10, 5, 3, 4, 1]
# assert build_heap_floyd_12(array) == expected_result
#
# print("All tests passed!")

# Example usage
array = [12, 11, 13, 5, 6, 7]
heap_sort_16(array)
print("Sorted array is:", array)

# Example usage:
arr = [12, 11, 13, 5, 6, 7]
heap_sort_16(arr)
print(arr)  # Output: [5, 6, 7, 11, 12, 13]
