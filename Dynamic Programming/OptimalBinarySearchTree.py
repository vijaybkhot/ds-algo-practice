import math

#
# def optimal_bst(p, n):
#     # Initialize tables e, w, and root
#     e = [[0] * (n + 2) for _ in range(n + 2)]
#     w = [[0] * (n + 2) for _ in range(n + 2)]
#     R = [[None] * (n + 1) for _ in range(n + 1)]
#
#     # Initialize base cases
#     for i in range(1, n + 2):
#         e[i][i - 1] = 0
#         w[i][i - 1] = 0
#
#     # Calculate optimal cost matrix e and root matrix R
#     for d in range(1, n + 2):
#         for i in range(1, n - d + 2):
#             j = i + d - 1
#             e[i][j] = float('inf')
#             w[i][j] = w[i][j - 1] + p[j - 1]
#             for r in range(i, j + 1):
#                 t = e[i][r - 1] + e[r + 1][j] + w[i][j]
#                 if t < e[i][j]:
#                     e[i][j] = t
#                     R[i][j] = r
#     return e, R


def optimal_bst(arr):
    n = len(arr)
    cache = [[0 for j in range(len(arr) + 1)] for i in range(len(arr) + 2)]
    index_root_table = [[0 for j in range(len(arr) + 1)] for i in range(len(arr) + 2)]
    for i in range(1, len(cache) - 1):
        cache[i][i] = arr[i - 1][1]
        # index_root_table has the key number from 1 - len(arr) == 0 - len(arr)-1 indexes of array arr
        # To get the original key index in array we have to subtract 1 from the value in index_root_table
        # So, Here index_root_table[i][i] has i as key number = arr[i-1] as key
        index_root_table[i][i] = i
    for d in range(1, len(arr)):
        for i in range(1, len(arr) + 1 - d):
            j = d + i
            minVal = float('Inf')
            rootKey = -1
            additionalCost = 0
            for l in range(i, j + 1):
                additionalCost += arr[l - 1][1]
                curVal = cache[i][l - 1] + cache[l + 1][j]
                if curVal < minVal:
                    minVal = curVal
                    rootKey = l
            cache[i][j] = minVal + additionalCost
            # index_root_table has the key number from 1 - len(arr) == 0 - len(arr)-1 indexes of array arr
            # To get the original key index in array we have to subtract 1 from the value in index_root_table
            # So, Here index_root_table[i][j] has rootKey as key number = arr[rootKey-1] as key
            index_root_table[i][j] = rootKey
    reconstructedKeys = []
    # While reconstruction, it's important to note that index_root_table has the key
    # number from 1 - len(arr) == 0 - len(arr)-1 indexes of array arr.
    # To get the original key index in array we have to subtract 1 from the value in index_root_table
    stack = [(index_root_table[1][len(arr)], 1, len(arr))]
    while stack:
        cur_root_idx, i, j = stack.pop()
        reconstructedKeys.append(arr[cur_root_idx - 1])
        if cur_root_idx > i:
            stack.append((index_root_table[i][cur_root_idx - 1], i, cur_root_idx - 1))
        if cur_root_idx < j:
            stack.append((index_root_table[cur_root_idx + 1][j], cur_root_idx + 1, j))
    # Construct E, W, and R tables
    E = [[cache[i][j] for j in range(1, len(arr) + 1)] for i in range(1, len(arr) + 1)]
    W = [[sum(arr[k - 1][1] for k in range(i, j + 1))] for i in range(1, n + 1) for j in range(i, n + 1)]
    R = [[index_root_table[i][j] for j in range(1, len(arr) + 1)] for i in range(1, len(arr) + 1)]

    return reconstructedKeys[0], reconstructedKeys, E, W, R


# Example usage
keys = [(1, 0.21), (2, 0.15), (3, 0.28), (4, 0.12), (5, 0.24)]
root, reconstructed_keys, E, W, R = optimal_bst(keys)

# Print E, W, and R tables
print("E Table:")
for row in E:
    print(row)

print("\nW Table:")
for row in W:
    print(row)

print("\nR Table:")
for row in R:
    print(row)