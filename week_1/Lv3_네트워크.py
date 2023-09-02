def solution(n, computers):
    answer = 0
    visited = []

    def dfs(i, n, visited):
        for j in range(n):
            if j not in visited and computers[i][j] == 1:
                visited.append(j)
                dfs(j, n, visited)

    for i in range(n):
        if i not in visited:
            visited.append(i)
            answer += 1
            dfs(i, n, visited)

    return answer


n = 3
computers = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1],
]
