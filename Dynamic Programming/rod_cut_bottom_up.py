def bottom_up_cut_rod(price_index, rod_length):
    r = [0] * (rod_length + 1)
    for j in range(1, rod_length + 1):
        q = float("-inf")
        for i in range(1, j + 1):
            q = max(q, price_index[i] + r[j - 1])
        r[j] = q
    return r[n]


def bottom_up_cut_rod_matrix_table(price_table, rod_length):
    # Initialize a 2D table T with dimensions (rod_length+1) x (rod_length+1)
    T = [[0 for _ in range(rod_length + 1)] for _ in range(rod_length + 1)]
    # Iterate over rod lengths from 1 to n
    for i in range(1, rod_length + 1):
        for j in range(1, rod_length + 1):
            if j >= i:
                T[i][j] = max(T[i - 1][j], price_table[i] + T[i][j - i])
            else:
                T[i][j] = T[i - 1][j]
    # Return the maximum revenue for a rod of length n
    return T[rod_length][rod_length]


def rod_cut_matrix_1(price_list, rod_length):
    T = [[0 for _ in range(rod_length + 1)] for _ in range(rod_length + 1)]
    for i in range(1, rod_length + 1):
        for j in range(1, rod_length + 1):
            if j >= i:
                T[i][j] = max(T[i - 1][j], price_list[i] + T[i][j - i])
            else:
                T[i][j] = T[i - 1][j]
    return T[rod_length][rod_length]


def rod_cut_matrix_2(price_list, rod_length):
    T = [[0 for _ in range(rod_length + 1)] for _ in range(rod_length + 1)]

    for i in range(1, rod_length + 1):
        for j in range(1, rod_length + 1):
            if j >= i:
                T[i][j] = max(T[i - 1][j], price_list[i] + T[i][j - i])
            else:
                T[i][j] = T[i - 1][j]
    return T[rod_length][rod_length]


def rod_cut_matrix_3(price_list, rod_length):
    n = len(price_list)
    T = [[0] * (rod_length + 1) for _ in range(n)]

    for i in range(1, n):
        for j in range(1, rod_length + 1):
            if j >= i:
                T[i][j] = max(T[i - 1][j], price_list[i] + T[i][j - i])
            else:
                T[i][j] = T[i - 1][j]

    return T[n - 1][rod_length]


def rod_cut_matrix_4(price_list, rod_length):
    n = len(price_list)
    T = [[0] * (rod_length + 1) for _ in range(n)]

    for i in range(1, n):
        for j in range(1, rod_length + 1):
            if j >= i:
                T[i][j] = max(T[i - 1][j], price_list[i] + T[i][j - 1])
            else:
                T[i][j] = T[i - 1][j]
    return T[n - 1][rod_length]


def rod_cut_matrix_5(price_list, rod_length):
    n = len(price_list)  # Price list start at index 1, because index 0 is 0. So no need to increment price list
    T = [[0] * (rod_length + 1) for _ in range(n)]

    for i in range(1, n):
        for j in range(1, rod_length + 1):
            if j >= i:
                T[i][j] = max(T[i - 1][j], price_list[i] + T[i][j - i])
            else:
                T[i][j] = T[i - 1][j]
    return T[n - 1][rod_length]


def rod_cut_matrix_6(price_list, rod_length):
    # Get the length of the price list
    n = len(price_list)

    # Create a 2D list to store the maximum revenue for different lengths of the rod
    # Initialize the list with all zeros
    # The number of rows is determined by the minimum of (n) and (rod_length + 1)
    # This ensures that we don't create unnecessary rows if the price list is shorter than rod_length
    T = [[0] * (rod_length + 1) for _ in range(n if n <= rod_length + 1 else rod_length + 1)]

    # Loop through each possible length of the rod
    for i in range(1, n if n <= rod_length + 1 else rod_length + 1):
        # Loop through each possible length of the rod (from 1 to rod_length)
        for j in range(1, rod_length + 1):
            # Check if the current length of the rod is greater than or equal to the current piece length (i)
            if j >= i:
                # If the current length of the rod is greater than or equal to the current piece length (i),
                # calculate the maximum revenue by either: 1. Not cutting the rod at this length (T[i - 1][j]) 2.
                # Cutting the rod at this length and adding the price of the piece to the revenue (price_list[i] + T[
                # i][j - i])
                T[i][j] = max(T[i - 1][j], price_list[i] + T[i][j - i])
            else:
                # If the current length of the rod is less than the current piece length (i),
                # the maximum revenue is the same as the maximum revenue for the previous length of the rod
                T[i][j] = T[i - 1][j]

    # Return the maximum revenue for the given rod length
    # If the length of the price list is less than or equal to the rod length, return T[n - 1][rod_length]
    # Otherwise, return T[rod_length][rod_length]
    return T[n - 1 if n - 1 <= rod_length else rod_length][rod_length]


def rod_cut_matrix_7(priceList, rodLength):
    # Get the length of the price list
    n = len(priceList)

    # Create a 2-D array to store the maximum revenue for different lengths of rods
    # Initialize the array with all 0's
    # Columns in the 2-D array represent the different lengths of the rod from 0, 1, 2, 3, ...., rodLength
    # Whereas the rows in the 2-D array represent individual lengths of the rod from 1, 2, 3,..., min(n, rodLength+1)
    # This ensures that we don't create unnecessary rows if the price list is shorter than rod_length

    T = [[0] * (rodLength + 1) for _ in range(n if n <= rodLength + 1 else rodLength + 1)]
    # Loop through each possible length of rod
    for i in range(1, n if n <= rodLength + 1 else rodLength + 1):
        # Loop through each possible length of the rod (from 1 to rodLength)
        for j in range(1, rodLength + 1):
            # Check if the current length of the rod is greater than or equal to the current piece length (i)
            if j >= i:
                T[i][j] = max(T[i - 1][j], priceList[i] + T[i][j - i])
            else:
                T[i][j] = T[i - 1][j]

    # Return the maximum revenue for the given length of the rod
    return T[n - 1 if n - 1 <= rodLength else rodLength][rodLength]


def rod_cut_matrix_8(priceList, rodLength):
    n = len(priceList)
    T = [[0]*(rodLength+1) for _ in range(n if n <= rodLength+1 else rodLength+1)]
    for i in range(1, len(T)):
        for j in range(1, len(T[0])):
            if j >= i:
                T[i][j] = max(T[i-1][j], priceList[i]+T[i][j-i])
            else:
                T[i][j] = T[i-1][j]
    return T[-1][-1]

# Example usage
# price_ = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]  # Price list for rods of lengths 0 to 10
# n = 5  # Length of the rod
# print("Maximum revenue:", rod_cut_matrix_7(price_, n))  # Output: 13
# price_list = [0, 2, 4, 7, 8]
# rod_length = 5
# assert rod_cut_matrix_7(price_list, rod_length) == 11
#
# price_list = [0, 1, 5, 8, 9, 10, 17, 17, 20]
# rod_length = 8
# assert rod_cut_matrix_7(price_list, rod_length) == 22
#
# price_list = [0, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# rod_length = 4
# assert rod_cut_matrix_7(price_list, rod_length) == 40
#
# price_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# rod_length = 10
# assert rod_cut_matrix_7(price_list, rod_length) == 10
#
# __, a, b, _ = [1,2,3,4]
# print(__,_)

priceList = [0, 1, 5, 8, 9, 10, 17, 17, 20]
rodLength = 8
print(rod_cut_matrix_8(priceList, rodLength))  # Output: 22
