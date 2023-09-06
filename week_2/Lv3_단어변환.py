from collections import deque


def solution(begin, target, words):
    def compare_words(word1, word2):
        diff = 0
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                diff += 1
        if diff == 1:
            return True
        return False

    answer = 0
    deq = deque()
    deq.append([begin, 0])
    check = [False] * len(words)

    while deq:
        word, cnt = deq.popleft()
        if word == target:
            answer = cnt
            break
        for i in range(len(words)):
            if not check[i] and compare_words(word, words[i]):
                deq.append([words[i], cnt + 1])
                check[i] = True

    return answer


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))
