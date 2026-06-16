import sys
from collections import deque
'''
7
6
1 2
2 3
1 5
5 2
5 6
4 7
'''
#노드번호는 1번 ~n번까지 사용
n = int(input())
t = int(input())

#인접리스트
al = [[] for _ in range(n+1)]

#모든 노드 딱 한번씩만 들려야 하기 때문에!

for i in range(t):
    From,To = map(int, input().split())
    #양방향 연결
    al[From].append(To)
    al[To].append(From)

#index를 n번까지 써야하면 n+1 이상 사이즈로 만들어야 합니다.
visited = [0]*(n+1)

cnt = 0

def bfs(startNode):
    global cnt
    q = deque()
    q.append(startNode)
    visited[startNode] = 1
    while q : 
        now = q.popleft()
        cnt+=1
        for next in al[now]:
            if visited[next] == 1 :continue
            q.append(next)
            visited[next] = 1

bfs(1)
print(cnt - 1)