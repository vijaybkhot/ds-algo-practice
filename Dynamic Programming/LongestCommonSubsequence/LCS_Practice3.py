def lcs_recursive(s1, s2, m, n):
    if m == 0 or n == 0:
        return ""
    if s1[m - 1] == s2[n - 1]:
        return lcs_recursive(s1, s2, m - 1, n - 1) + s1[m - 1]
    else:
        lcs1 = lcs_recursive(s1, s2, m - 1, n)
        lcs2 = lcs_recursive(s1, s2, m, n - 1)
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


def lcs_bottom_up(s1, s2):
    m = len(s1)
    n = len(s2)
    memo = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                memo[i][j] = memo[i - 1][j - 1] + 1
            else:
                memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])

    # Reconstruct LCS
    lcs = ""
    i = m
    j = n
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs = s1[i - 1] + lcs
            i -= 1
            j -= 1
        else:
            if memo[i - 1][j] > memo[i][j - 1]:
                i -= 1
            else:
                j -= 1

    return lcs
