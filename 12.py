def solution(prices):
    answer = []
    for index_i, i in enumerate(prices[:-1]):
        count = 0
        for j in prices[index_i+1:]:
            count+=1
            if i > j :
                answer.append(count)
                break
        else:
            answer.append(count)
    answer.append(0)
    return answer


print(solution([1,2,3,2,3]))