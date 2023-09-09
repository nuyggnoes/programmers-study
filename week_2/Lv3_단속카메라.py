def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    camera = -30001

    for i in routes:
        if camera < i[0]:
            answer += 1
            camera = i[1]
    return answer


routes = [[-20, -15], [-14, -5], [-18, -13], [-5, -3]]
# return 2
routes = [[-20, -18], [-15, -14], [-13, -5], [-3, -1]]
# # return 4
print(solution(routes))
