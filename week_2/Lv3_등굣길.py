def solution(m, n, puddles):
    answer = 0
    if puddles[0]:
        puddles = [[n, m] for [m, n] in puddles]
    dp = [[0 for j in range(m + 1)] for i in range(n + 1)]
    dp[1][1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            if [i, j] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007
    answer = dp[-1][-1]
    return answer


# m = 4
# n = 3
# puddles = [[2, 2]]
# return 4

m = 4
n = 4
puddles = [[3, 2], [2, 4]]
# return 7

print(solution(m, n, puddles))
