def lcs_recursive(s1, s2, m, n):
    if m == 0 or n == 0:
        return ""
    if s1[m - 1] == s2[n - 1]:
        return lcs_recursive(s1, s2, m - 1, n - 1) + s1[m - 1]
    else:
        lcs1 = lcs_recursive(s1, s2, m - 1, n)
        lcs2 = lcs_recursive(s1, s2, m, n - 1)
        return lcs1 if len(lcs1) > len(lcs2) else lcs2


def lcs_recursive_1(s1, s2, m, n):
    if m == 0 or n == 0:
        return ""
    if s1[m - 1] == s2[n - 1]:
        return lcs_recursive_1(s1, s2, m - 1, n - 1) + s1[m - 1]
    else:
        lcs1 = lcs_recursive_1(s1, s2, m - 1, n)
        lcs2 = lcs_recursive_1(s1, s2, m, n - 1)

        return lcs1 if len(lcs1) > len(lcs2) else lcs2


def lcs_top_down(s1, s2, m, n, memo):
    if m == 0 or n == 0:
        return ""
    if memo[m][n] != "":
        return memo[m][n]
    else:
        if s1[m - 1] == s2[n - 1]:
            memo[m][n] = lcs_top_down(s1, s2, m - 1, n - 1, memo) + s1[m - 1]
        else:
            lcs1 = lcs_top_down(s1, s2, m - 1, n, memo)
            lcs2 = lcs_top_down(s1, s2, m, n - 1, memo)
            memo[m][n] = lcs1 if len(lcs1) > len(lcs2) else lcs2

        return memo[m][n]


def lcs_top_down_1(s1, s2, m, n, memo):
    if m == 0 or n == 0:
        return ""
    if memo[m][n] != "":
        return memo[m][n]
    if s1[m-1] == s2[n-1]:
        memo[m][n] = lcs_top_down(s1, s2, m-1, n-1, memo) + s1[m-1]
    else:
        lcs1 = lcs_top_down_1(s1, s2, m-1, n, memo)
        lcs2 = lcs_top_down_1(s1, s2, m, n-1, memo)
        memo[m][n] = lcs1 if len(lcs1) > len(lcs2) else lcs2

    return memo[m][n]


def lcs_bottom_up(s1, s2):
    m = len(s1)
    n = len(s2)
    memo = [[0] * (n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                memo[i][j] = memo[i-1][j-1] + 1
            else:
                memo[i][j] = max(memo[i-1][j], memo[i][j-1])

    # Reconstruct LCS
    lcs = ""
    i = m
    j = n
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            lcs = s1[i-1] + lcs
            i -= 1
            j -= 1
        else:
            if memo[i-1][j] > memo[i][j-1]:
                i -= 1
            else:
                j -= 1

    return lcs


def lcs_bottom_up_1(s1, s2):
    m = len(s1)
    n = len(s2)
    memo = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                memo[i][j] = memo[i-1][j-1] + 1
            else:
                memo[i][j] = max(memo[i-1][j], memo[i][j-1])

    # Reconstruct lcs
    lcs = ""
    i = m
    j = n
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            lcs = s1[i-1] + lcs
            i -= 1
            j -= 1
        else:
            if memo[i-1][j] > memo[i][j-1]:
                i -= 1
            else:
                j -= 1

    return lcs



# Test case 1: Both strings are empty
s1 = ""
s2 = ""
assert lcs_bottom_up_1(s1, s2) == ""

# Test case 2: One string is empty
s1 = "abc"
s2 = ""
assert lcs_bottom_up_1(s1, s2) == ""

# Test case 3: Both strings are the same
s1 = "abc"
s2 = "abc"
assert lcs_bottom_up_1(s1, s2) == "abc"

# Test case 4: No common subsequence
s1 = "abc"
s2 = "def"
assert lcs_bottom_up_1(s1, s2) == ""

# Test case 5: Common subsequence in the middle
s1 = "abcdef"
s2 = "azbxcxdxe"
assert lcs_bottom_up_1(s1, s2) == "abcde"

# Test case 6: Common subsequence at the beginning
s1 = "abcdef"
s2 = "abcxyz"
assert lcs_bottom_up_1(s1, s2) == "abc"

# Test case 7: Common subsequence at the end
s1 = "abcdef"
s2 = "xyzdef"
assert lcs_bottom_up_1(s1, s2) == "def"

#
# #
# # # Test case 1
# # s1 = "ABCBDAB"
# # s2 = "BDCAB"
# # print("Test case 1:", lcs_recursive_1(s1, s2, len(s1), len(s2)))  # Output: "BCAB"
# #
# # # Test case 2
# # s1 = "AGGTAB"
# # s2 = "GXTXAYB"
# # print("Test case 2:", lcs_recursive_1(s1, s2, len(s1), len(s2)))  # Output: "GTAB"
# #
# # # Test case 3
# # s1 = "ABC"
# # s2 = "DEF"
# # print("Test case 3:", lcs_recursive_1(s1, s2, len(s1), len(s2)))  # Output: ""
# #
# # # Test case 4
# # s1 = "AAAAAA"
# # s2 = "AA"
# # print("Test case 4:", lcs_recursive_1(s1, s2, len(s1), len(s2)))  # Output: "AA"
#
# # Test case 1
# s1 = "ABCBDAB"
# s2 = "BDCAB"
# memo = [["" for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
# print("Test case 1:", lcs_top_down_1(s1, s2, len(s1), len(s2), memo))  # Output: "BCAB"
#
# # Test case 2
# s1 = "AGGTAB"
# s2 = "GXTXAYB"
# memo = [["" for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
# print("Test case 2:", lcs_top_down_1(s1, s2, len(s1), len(s2), memo))  # Output: "GTAB"
#
# # Test case 3
# s1 = "ABC"
# s2 = "DEF"
# memo = [["" for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
# print("Test case 3:", lcs_top_down_1(s1, s2, len(s1), len(s2), memo))  # Output: ""
#
# # Test case 4
# s1 = "AAAAAA"
# s2 = "AA"
# memo = [["" for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
# print("Test case 4:", lcs_top_down_1(s1, s2, len(s1), len(s2), memo))  # Output: "AA"
