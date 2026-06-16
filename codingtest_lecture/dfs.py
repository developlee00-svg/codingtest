'''
 DFS 기본 코드
'''

import sys
#인접행렬
arr = [
    [0,1,1,0,0,0],
    [1,0,0,1,1,0],
    [1,0,0,0,0,1],
    [0,1,0,0,0,0],
    [0,1,0,0,0,0],
    [0,0,1,0,0,0]
]
#인접 리스트
al =[[1,2],[0,3,4],[0,5],[1],[1],[2]]

#모든 노드 딱 한번씩만 들려야 하기 때문에!
visited_arr = [0]*6
visited_al =[0]*6


def dfs_arr(now):
    visited_arr[now] = 1
    print(now,end = " ")
    #연결정보 확인
    for next in range(6):
        #연결되지 않은 노드
        if arr[now][next] == 0 : continue
        #이미 들린 노드
        if visited_arr[next] == 1 : continue
        dfs_arr(next)

def dfs_al(now):
    visited_al[now] = 1
    print(now , end = " ")
    #연결정보 확인
    for next in al[now]:
        #이미들린 노드
        if visited_al[next] == 1: continue
        dfs_al(next)


dfs_arr(0)

print()

dfs_al(0)