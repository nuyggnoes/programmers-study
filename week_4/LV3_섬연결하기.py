import sys


def solution(n, costs):
    answer = 0
    visited = []
    map = {i: [] for i in range(n)}

    for i in costs:
        map[i[0]].append((i[1], i[2]))
        map[i[1]].append((i[0], i[2]))

    visited.append(0)

    while len(visited) != n:
        M = sys.maxsize
        for i in visited:
            for j in map[i]:
                if M > j[1] and j[0] not in visited:
                    M = j[1]
                    idx = j[0]
        answer += M
        visited.append(idx)
    return answer


# n = 4
# costs = [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]
n = 7
costs = [
    [2, 3, 7],
    [3, 6, 13],
    [3, 5, 23],
    [5, 6, 25],
    [0, 1, 29],
    [1, 5, 34],
    [1, 2, 35],
    [4, 5, 53],
    [0, 4, 75],
]
print(solution(n, costs))
