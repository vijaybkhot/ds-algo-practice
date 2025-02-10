def dp(X, Y, i, j, memo_H, memo_P):
    if memo_H[i][j] is not None:
        return memo_H[i][j], memo_P[i][j]

    if i == 0 or j == 0:
        memo_H[i][j] = 0
        memo_P[i][j] = ''
        return 0, ''

    if X[i - 1] == Y[j - 1]:
        P1, P1_dir = dp(X, Y, i - 1, j - 1, memo_H, memo_P)
        P1 += 2
    else:
        P1, P1_dir = dp(X, Y, i - 1, j - 1, memo_H, memo_P)
        P1 -= 1

    P2, P2_dir = dp(X, Y, i - 1, j, memo_H, memo_P)
    P2 -= 1
    P3, P3_dir = dp(X, Y, i, j - 1, memo_H, memo_P)
    P3 -= 1

    H = max(P1, P2, P3)

    if H == P1:
        memo_P[i][j] = 'diagonal'
    elif H == P2:
        memo_P[i][j] = 'up'
    else:
        memo_P[i][j] = 'left'

    memo_H[i][j] = H
    return H, memo_P[i][j]


def smith_waterman_top_down(X, Y):
    n = len(X)
    m = len(Y)
    memo_H = [[None] * (m + 1) for _ in range(n + 1)]
    memo_P = [[None] * (m + 1) for _ in range(n + 1)]

    max_score = 0
    max_i = max_j = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            score, _ = dp(X, Y, i, j, memo_H, memo_P)
            if score > max_score:
                max_score = score
                max_i, max_j = i, j

    return memo_H, memo_P


def print_seq_align_x(X, P, n, m):
    if n == 0 or m == 0:
        print()
        return
    if P[n][m] == 'diagonal':
        print_seq_align_x(X, P, n - 1, m - 1)
        print(X[n - 1], end=" ")
    else:
        if P[n][m] == 'left':
            print_seq_align_x(X, P, n, m - 1)
            print("-", end=" ")
        else:
            print_seq_align_x(X, P, n - 1, m)
            print(X[n - 1], end=" ")


def print_seq_align_y(Y, P, n, m):
    if n == 0 or m == 0:
        print()
        return
    if P[n][m] == 'diagonal':
        print_seq_align_y(Y, P, n - 1, m - 1)
        print(Y[m - 1], end=" ")
    else:
        if P[n][m] == 'up':
            print_seq_align_y(Y, P, n - 1, m)
            print("-", end=" ")
        else:
            print_seq_align_y(Y, P, n, m - 1)
            print(Y[m - 1], end=" ")


X = "cdbaabbdca"
Y = "cadcaccabd"
H, P = smith_waterman_top_down(X, Y)

# Print the transpose of the alignment score matrix H
for j in range(len(H[0])):
    print([H[i][j] for i in range(len(H))])

print("traceback")
# Print the traceback matrix P
for j in range(len(P[0])):
    print([P[i][j] for i in range(len(P))])

print_seq_align_x(X, P, len(X), len(Y))
print_seq_align_y(Y, P, len(X), len(Y))
