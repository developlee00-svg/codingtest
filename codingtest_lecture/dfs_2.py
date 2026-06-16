import sys

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
start, end = map(int, input().split())
visited = [0] * N

cur_max = -21e8
cur_min = 21e8

def dfs(curr, total):
    global cur_max, cur_min
    visited[curr] = 1
    if curr == end:
        cur_max = max(total, cur_max)
        cur_min = min(total, cur_min)
        visited[curr] = 0   # end 도달 시에도 방문 해제
        return
    for i in range(N):
        if arr[curr][i] and not visited[i]:
            dfs(i, total + arr[curr][i])
    visited[curr] = 0

dfs(start, 0)
print(int(cur_min))
print(int(cur_max))