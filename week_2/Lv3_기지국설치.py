from math import ceil


def solution(n, stations, w):
    answer = 0
    max_spread = (w * 2) + 1
    start = 1
    for i in stations:
        answer += ceil((i - w - start) / max_spread)
        start = i + w + 1
    if start <= n:
        answer += ceil((n - start + 1) / max_spread)
    return answer


N = 11
stations = [4, 11]
W = 1
# return 3

N = 16
stations = [9]
W = 2
print(solution(N, stations, W))
