def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    while B:
        print(A, B)
        if A[-1] < B[-1]:
            answer += 1
            A.pop()
            B.pop()
        else:
            B.pop()
    return answer


A = [5, 1, 3, 7]
B = [2, 2, 6, 8]
print(solution(A, B))
