import sys
from collections import deque
'''
10 9
1 2
7 1
6 7
3 7
5 4
10 9
9 8
3 8
4 3
1 3
'''
#노드번호는 1번 ~n번까지 사용
n,t = map(int, input().split())

#인접리스트
al = [[] for _ in range(n+1)]

#모든 노드 딱 한번씩만 들려야 하기 때문에!

for i in range(t):
    From,To = map(int, input().split())
    #양방향 연결
    al[From].append(To)
    al[To].append(From)

startNode, K = map(int, input().split())
#index를 n번까지 써야하면 n+1 이상 사이즈로 만들어야 합니다.
visited = [0]*(n+1)


def bfs(startNode):
    q = deque()
    q.append(startNode)
    visited[startNode] = 1
    while q : 
        now = q.popleft()
        for next in al[now]:
            if visited[next] != 0 :continue
            q.append(next)
            #now노드에서 한칸 더 왔어요! 라고 기록
            visited[next] = visited[now]+1

bfs(startNode)
cnt = 0
for i in range(1,n+1):
    #visited배열에 시작노드를 1로 기록했기 때문에 빼서 계산
    #0으로는 기록못하니까!!!!
    if 0 <= visited[i]-1 <= K :cnt+=1
print(cnt)