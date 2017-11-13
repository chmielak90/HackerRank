def solution(A):
    A.sort()

    while len(A) > 1:
        if A[0] == A[1]:
            del A[:2]
        else:
            del A[-2:]

    return A[0]


print(solution([9, 3, 9, 3, 9, 7, 9])