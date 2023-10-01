def solution(user_id, banned_id):
    answer = []
    total_list = []

    def check(user, ban):
        if len(user) != len(ban):
            return False
        else:
            for i, j in zip(user, ban):
                if j == "*":
                    continue
                if i != j:
                    return False
            return True

    for i in range(len(user_id)):
        cnt = 0
        for j in range(len(user_id)):
            if i != j:
                total_list.append((user_id[i], user_id[j]))

    for i in total_list:
        if check(i[0], banned_id[0]) and check(i[1], banned_id[1]):
            cnt += 1

    return cnt

    # if cnt == len(banned_id):
    #     if set(i) not in answer:
    #         answer.append(set(i))


user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]

print(solution(user_id, banned_id))
