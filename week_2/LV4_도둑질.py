def solution(money):
    answer = 0
    dp = []
    max_money = 0
    for i in range(0, len(money) - 1):
        if money[i] + money[i + 1] > max_money:
            max_money = money[i] + money[i + 1]
    return answer


money = [1, 2, 3, 1]
