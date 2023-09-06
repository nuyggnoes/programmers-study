from heapq import heapify, heappop, heappush


def solution(n, works):
    max_heap = [-i for i in works]
    heapify(max_heap)
    for _ in range(n):
        if max_heap[0] < 0:
            max_value = heappop(max_heap)
            max_value += 1
            heappush(max_heap, max_value)
    return sum([i**2 for i in max_heap])


works = [1, 1]
n = 3


# 시간초과
# def solution(n, works):
#     answer = 0
#     if n >= sum(works):
#         return 0
#     for _ in range(n):
#         works[works.index(max(works))] -= 1
#     return sum(i**2 for i in works)
