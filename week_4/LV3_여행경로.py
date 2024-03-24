def solution(tickets):
    answer = []
    route = {}
    for st, en in tickets:
        if st not in route:
            route[st] = [en]
        else:
            route[st].append(en)

    for st in route.keys():
        route[st].sort(reverse=True)

    path = ["ICN"]
    print(route)
    while path:
        cur = path[-1]
        if cur not in route or len(route[cur]) == 0:
            answer.append(path.pop())
        else:
            path.append(route[cur].pop())

    return answer[::-1]


# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
# tickets = [
#     ["ICN", "SFO"],
#     ["ICN", "ATL"],
#     ["SFO", "ATL"],
#     ["ATL", "ICN"],
#     ["ATL", "SFO"],
# ]
tickets = [["ICN", "JFK"], ["ICN", "AAD"], ["JFK", "ICN"]]  # 테스트 1,2 반례
# return ["ICN", "JFK", "ICN", "AAD"]
print(solution(tickets))

# def solution(tickets):
#     route = {}
#     for st, en in tickets:
#         if st not in route:
#             route[st] = [en]
#         else:
#             route[st].append(en)

#     for st in route.keys():
#         route[st].sort(reverse=True)

#     path = ["ICN"]

#     while True:
#         cur = path[-1]
#         if cur not in route or len(route[cur]) == 0:
#             break
#         path.append(route[cur].pop())
#     return path
