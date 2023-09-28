def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)

    while B:
        A_card = A[-1]
        B_card = B[-1]
        if B_card > A_card:
            A.pop()
            B.pop()
            answer += 1
        else:
            B.pop()
    return answer


A = [5, 1, 3, 7]
B = [2, 2, 6, 8]
# return 3
print(solution(A, B))
