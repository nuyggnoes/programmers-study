def solution(triangle):
    dp = [[0 for j in i] for i in triangle]
    dp[0][0] = triangle[0][0]
    for i in range(len(triangle)):
        for j in range(i):
            dp[i][j] = max(dp[i][j], dp[i - 1][j] + triangle[i][j])
            dp[i][j + 1] = dp[i - 1][j] + triangle[i][j + 1]
    return max(dp[-1])


# def solution(triangle):
#     dp = []
#     for t in range(1, len(triangle)):
#         for i in range(t + 1):
#             if i == 0:
#                 triangle[t][0] += triangle[t - 1][0]
#             elif i == t:
#                 triangle[t][-1] += triangle[t - 1][-1]
#             else:
#                 triangle[t][i] += max(triangle[t - 1][i - 1], triangle[t - 1][i])
#             print(triangle)
#     return max(triangle[-1])


triangle = [
    [7],
    [3, 8],
    [8, 1, 0],
    [2, 7, 4, 4],
    [4, 5, 2, 6, 5],
]
print(solution(triangle))
