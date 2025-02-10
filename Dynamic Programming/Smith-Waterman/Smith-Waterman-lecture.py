
def smith_waterman(X, Y):
    n = len(X)
    m = len(Y)
    H = [[0] * (m + 1) for _ in range(n + 1)]
    P = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(0, n + 1):
        H[i][0] = P[i][0] = 0

    for j in range(0, m + 1):
        H[0][j] = P[0][j] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if X[i - 1] == Y[j - 1]:
                P1 = H[i - 1][j - 1] + 2
            else:
                P1 = H[i - 1][j - 1] - 1

            P2 = H[i - 1][j] - 1
            P3 = H[i][j - 1] - 1

            H[i][j] = max(P1, P2, P3)

            if H[i][j] == P1:
                P[i][j] = 'diagonal'
            elif H[i][j] == P2:
                P[i][j] = 'up'
            else:
                P[i][j] = 'left'

    return H, P


def print_seq_align_x(X, P, n, m):
    if n == 0 or m == 0:
        print()
        return
    if P[n][m] == 'diagonal':
        print_seq_align_x(X, P, n - 1, m - 1)
        print(X[n-1], end=" ")
    else:
        if P[n][m] == 'left':
            print_seq_align_x(X, P, n, m - 1)
            print("-", end=" ")
        else:
            print_seq_align_x(X, P, n - 1, m)
            print(X[n-1], end=" ")


def print_seq_align_y(Y, P, n, m):
    if n == 0 or m == 0:
        print()
        return
    if P[n][m] == 'diagonal':
        print_seq_align_y(Y, P, n - 1, m - 1)
        print(Y[m-1], end=" ")
    else:
        if P[n][m] == 'up':
            print_seq_align_y(Y, P, n - 1, m)
            print("-", end=" ")
        else:
            print_seq_align_y(Y, P, n, m - 1)
            print(Y[m-1], end=" ")


X = "baababdbba"
Y = "cbaccbaaba"
H, P = smith_waterman(X, Y)

# Print the transpose of the alignment score matrix H
for j in range(len(H[0])):
    print([H[i][j] for i in range(len(H))])

print("traceback")
# Print the traceback matrix P
for j in range(len(P[0])):
    print([P[i][j] for i in range(len(P))])

print_seq_align_x(X, P, len(X), len(Y))
print_seq_align_y(Y, P, len(X), len(Y))
