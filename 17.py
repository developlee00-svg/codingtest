
from collections import deque

def solution(cards1, cards2, goal):
    # 모든 배열을 스택처럼 쓸 계획 deque로 바꿔서 popleft() 쓰면 빠름
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)
    while True:
        # cards1의 첫번째와 goal의 첫번째가 같으면 둘 다 pop
        if cards1 and (cards1[0] == goal[0]):
            cards1.popleft()
            goal.popleft()
        # 위 word1 로직과 동일
        elif cards2 and (cards2[0] == goal[0]):
            cards2.popleft()
            goal.popleft()
        # 둘 다 맞지 않으면 No 반환
        else :
            return "No"
        
        if not goal:
            return "Yes"

print(solution(['a', 'b', 'c'], ['e'], ['a', 'b', 'c', 'd']))