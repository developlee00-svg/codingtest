import sys

n,t= map(int, input().split())

#2차원 배열 형태에 인접행렬로 저장(n,n인덱스까지 사용해야한다)
arr =[[0]*(n+1) for _ in range(n+1)]

for i in range(t):
    From,To = map(int, input().split())
    #단방향연결
    arr[From][To] = 1
    #arr[To][From] = 1


# for i in range(1,n+1) : 
#     for j in range(1,n+1):
#         print(arr[i][j], end=' ')
#     print()

for row in arr[1:]:
    print(*row[1:])