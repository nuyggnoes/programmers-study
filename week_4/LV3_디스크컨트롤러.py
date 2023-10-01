from heapq import heappush, heappop


def solution(jobs):
    n = len(jobs)
    answer = 0
    heap = []
    for j in jobs:
        heappush(heap, [j[1], j[0]])

    st, end = 0, 0
    while heap:
        cur = heappop(heap)
        st = end
        end += cur[0]
        answer += end - cur[1]
    return answer // n


# import heapq


# def solution(jobs):
#     answer, now, i = 0, 0, 0
#     start = -1
#     heap = []
#     while i < len(jobs):
#         for j in jobs:
#             if start < j[0] <= now:
#                 heapq.heappush(heap, [j[1], j[0]])
#         print(heap)
#         if len(heap) > 0:
#             current = heapq.heappop(heap)
#             print("현재", current)
#             start = now
#             now += current[0]
#             answer += now - current[1]
#             i += 1
#         else:
#             now += 1
#     return int(answer / len(jobs))


jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))
a = [1, 2, 3, 4, 5]
print(a)


def solution(jobs):
    t = 0
    tesk = 0
    length = len(jobs)
    jobs.sort(key=lambda x: x[1])
    while len(jobs) > 0:
        for i in jobs:
            if i[0] <= t:
                jobs.remove(i)
                t += i[1] - 1
                tesk += t - i[0] + 1
                break
        t += 1
    return tesk // length
