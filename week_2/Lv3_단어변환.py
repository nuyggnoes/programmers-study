from collections import deque


def solution(begin, target, words):
    def compare_words(word1, word2):
        cnt = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                cnt += 1
        if cnt == 1:
            return True
        return False

    answer = 0
    if target not in words:
        return 0
    deq = deque()
    check = [False for _ in range(len(words))]
    deq.append([begin, 0])

    while deq:
        tmp_word, depth = deq.popleft()
        if tmp_word == target:
            return depth
        for i in range(len(words)):
            if compare_words(tmp_word, words[i]) and not check[i]:
                deq.append([words[i], depth + 1])
                check[i] = True

    return answer


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
# return 4
print(solution(begin, target, words))
