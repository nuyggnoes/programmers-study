def solution(operations):
    answer = []
    for i in operations:
        if(i[0] == "I"):
            answer.append(int(i[2:]))
        else:
            if(i[2] == "-" and answer):
                answer.remove(min(answer))
            elif answer:
                answer.remove(max(answer))
    if not answer : return [0,0]
    return [max(answer), min(answer)]

operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
result = solution(operations) 
print(result)