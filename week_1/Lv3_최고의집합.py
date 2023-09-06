def solution(n, s):
    answer = []
    if n > s:
        return [-1]
    answer = [s // n for _ in range(n)]

    if s % n != 0:
        for i in range(s % n):
            answer[i] += 1
    return sorted(answer)


n = 2
s = 9
