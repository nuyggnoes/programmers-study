def solution(m, n, puddles):
    answer = 0
    dp = [[0 for j in range(m + 1)] for i in range(n + 1)]
    dp[1][1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            if [i, j] in puddles:
                dp[j][i] = 0
            else:
                dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % 1000000007
    print(dp)
    answer = dp[-1][-1]
    return answer


m = 4
n = 3
puddles = [[2, 2]]

# print(solution(m, n, puddles))
