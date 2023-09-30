from collections import deque


def solution(n, edge):
    answer = 0
    map = {i: [] for i in range(1, n + 1)}
    for i in edge:
        map[i[0]].append(i[1])
        map[i[1]].append(i[0])
    q = deque([])
    d = [n] * (n + 1)
    d[1] = 0
    q.append(1)

    while q:
        cur = q.popleft()
        for i in map[cur]:
            if d[i] == n:
                q.append(i)
                d[i] = d[cur] + 1
    far = max(d[1:])
    answer = d[1:].count(far)
    return answer


n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, vertex))
