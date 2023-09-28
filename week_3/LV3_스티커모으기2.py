def solution(sticker):
    dp_first = [0] * len(sticker)
    dp_last = [0] * len(sticker)

    dp_first[0] = sticker[0]
    for i in range(1, len(sticker) - 1):
        dp_first[i] = max(dp_first[i - 1], dp_first[i - 2] + sticker[i])

    dp_last[0] = 0
    for i in range(1, len(sticker)):
        dp_last[i] = max(dp_last[i - 1], dp_last[i - 2] + sticker[i])

    return max(dp_first[len(sticker) - 2], dp_last[len(sticker) - 1])


sticker = [14, 6, 5, 11, 3, 9, 2, 10]

print(solution(sticker))

# answer 36
