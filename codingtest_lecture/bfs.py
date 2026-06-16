import sys
from collections import deque

#인접행렬
arr = [
    [0,1,0,0,1,0],
    [1,0,1,1,0,0],
    [0,1,0,0,0,0],
    [0,1,0,0,0,0],
    [1,0,0,0,0,1],
    [0,0,0,0,1,0]
]
#인접 리스트
al =[[1,4],[0,2,3],[0,1],[1],[0,5],[4]]

#모든 노드 딱 한번씩만 들려야 하기 때문에!
visited_arr = [0]*6
visited_al =[0]*6

def bfs_arr(startNode) : 
    q = deque()
#1. q에 시작노드 대기
    q.append(startNode)
    visited_arr[startNode] =1
#2. q의 맨앞을 꺼냅니다.
    while q :
        now = q.popleft()
        print(now , end = " ")
        #3. 연결정보 확인
        for next in range(6):
            if arr[now][next] == 0 : continue
            #visited검사
            if visited_arr[next] == 1 : continue
            #4. q에 대기
            q.append(next)
            visited_arr[next] = 1

def bfs_al(startNode) : 
    q = deque()
#1. q에 시작노드 대기
    q.append(startNode)
    visited_al[startNode] =1
#2. q의 맨앞을 꺼냅니다.
    while q :
        ## 내가 지금 탐색중인 노드 번호
        now = q.popleft()
        print(now , end = " ")
        #3. 연결정보 확인
        for next in al[now]:
            #visited검사
            if visited_al[next] == 1 : continue
            #4. q에 대기
            q.append(next)
            visited_al[next] = 1


bfs_arr(0)
print()
bfs_al(0)
