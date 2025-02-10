def smith_waterman(sequence1, sequence2, match_score=2, mismatch_penalty=-1, gap_penalty=-1):
    # Initialize two tables of len(sequence1)+1 and len(sequence2)+1
    rows = len(sequence1) + 1
    cols = len(sequence2) + 1
    score = [[0 for _ in range(cols)] for _ in range(rows)]
    traceback = [["" for _ in range(cols)] for _ in range(rows)]

    # Initialize variables to store the maximum score and its position
    max_score = 0
    max_i = 0
    max_j = 0

    # Fill in the scoring and the traceback matrices
    for i in range(1, rows):
        for j in range(1, cols):
            match = score[i-1][j-1] + (match_score if sequence1[i-1] == sequence2[j-1] else mismatch_penalty)
            delete = score[i-1][j] + gap_penalty
            insert = score[i][j-1] + gap_penalty
            score[i][j] = max(0, match, delete, insert)

            if score[i][j] == match:
                traceback[i][j] = "diagonal"
            elif score[i][j] == delete:
                traceback[i][j] = "up"
            else:
                traceback[i][j] = "left"

            if score[i][j] > max_score:
                max_score = score[i][j]
                max_i = i
                max_j = j

    # Perform traceback starting from the cell with the maximum score
    alignment1 = ""
    alignment2 = ""
    i = max_i
    j = max_j
    while i > 0 and j > 0 and score[i][j] > 0:
        if traceback[i][j] == "diagonal":
            if sequence1[i - 1] == sequence2[j - 1]:
                alignment1 = sequence1[i - 1] + alignment1
                alignment2 = sequence2[j - 1] + alignment2
            else:
                alignment1 = sequence1[i - 1] + alignment1
                alignment2 = sequence2[j - 1] + alignment2
            i -= 1
            j -= 1
        elif traceback[i][j] == "up":
            alignment1 = sequence1[i-1] + alignment1
            alignment2 = "-" + alignment2
            i -= 1
        else:
            alignment1 = "-" + alignment1
            alignment2 = sequence2[j-1] + alignment2
            j -= 1

    return alignment1, alignment2, max_score

# # Test case 1: Identical sequences
# sequence1 = "AGTACGCA"
# sequence2 = "AGTACGCA"
# alignment1, alignment2, score = smith_waterman(sequence1, sequence2)
# print("Test Case 1:")
# print("Alignment 1:", alignment1)
# print("Alignment 2:", alignment2)
# print("Alignment Score:", score)
# print()
#
# # Test case 2: Completely different sequences
# sequence1 = "AGTACGCA"
# sequence2 = "TTTTTTTT"
# alignment1, alignment2, score = smith_waterman(sequence1, sequence2)
# print("Test Case 2:")
# print("Alignment 1:", alignment1)
# print("Alignment 2:", alignment2)
# print("Alignment Score:", score)
# print()
#
# # Test case 3: Sequences with some similarity but also some differences
# sequence1 = "abababda"
# sequence2 = "acbababa"
# alignment1, alignment2, score = smith_waterman(sequence1, sequence2)
# print("Test Case 3:")
# print("Alignment 1:", alignment1)
# print("Alignment 2:", alignment2)
# print("Alignment Score:", score)
# print()


sequence1 = "caacbdacca"
sequence2 = "bccbcdccba"
alignment1, alignment2, score = smith_waterman(sequence1, sequence2)
print("Test Case 4:")
print("Alignment 1:", alignment1)
print("Alignment 2:", alignment2)
print("Alignment Score:", score)
print()

# Test case 5: Longer sequences
sequence1 = "CGTGAATTCAT"
sequence2 = "GACTTAC"
alignment1, alignment2, score = smith_waterman(sequence1, sequence2, match_score=5, mismatch_penalty=-3, gap_penalty=-4)
print("Test Case 5:")
print("Alignment 1:", alignment1)
print("Alignment 2:", alignment2)
print("Alignment Score:", score)
print()
