N = int(input())
T = int(input())

arr =[[0]*(N+1) for _ in range(N+1)]
visited = [0] * (N+1)
for i in range(T):
    From, To = map(int, input().split())
    arr[From][To] = 1
    arr[To][From] = 1

def dfs(now):
    visited[now] = 1
    for i in range(1, len(arr[now])):
        if arr[now][i] and not visited[i]:
            dfs(i)

dfs(1)
answer = sum(visited) - 1
print(answer)