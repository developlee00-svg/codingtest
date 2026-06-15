def solution(progresses, speeds):
    answer = []
    length = len(speeds)
    # progesses가 빌 때까지 반복
    while progresses:
        for i in range(length):
            progresses[i] += speeds[i]
        # progresses가 100보다 크면
        if progresses[0] >= 100:
            count = 0
            # 크지 않은 게 나올 때까지 pop()하면서 비교
            while progresses and progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                count+=1
            # 100보다 작은 게 나왔으면 반복문 멈추고 return할 배열에 append()
            answer.append(count)
            # 위에서 줄어든 길이에 맞춰 length 조절
            length = len(speeds)

    return answer


print(solution([93,30,55], [1,30,5]))