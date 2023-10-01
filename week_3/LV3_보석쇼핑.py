def solution(gems):
    n = len(gems)  # 8
    answer = [0, n - 1]
    kind = len(set(gems))  # 4
    dic = {gems[0]: 1}
    l, r = 0, 0
    while l < n and r < n:
        if len(dic) < kind:
            r += 1
            if r == n:
                break
            dic[gems[r]] = dic.get(gems[r], 0) + 1
        else:
            if (r - l + 1) < (answer[1] - answer[0] + 1):
                answer = [l, r]

            if dic[gems[l]] == 1:
                del dic[gems[l]]
            else:
                dic[gems[l]] -= 1
            l += 1

    answer[0] += 1
    answer[1] += 1
    return answer


gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
# return [3, 7]
print(solution(gems))
