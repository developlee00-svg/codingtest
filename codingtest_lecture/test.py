# input_index = input().split()

# y = int(input_index[0])
# x = int(input_index[1])

y, x = map(int, input().split())

arr = [
    [3, 5, 4],
    [1, 1, 2],
    [1, 3, 9]
]

# 델타배열 : 상하좌우 순서
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
answer = 0
for dir in range(4):
    ny = y + dy[dir]
    nx = x + dx[dir]

    # [중요] 델타 배열을 쓸 때는 범위 체크를 항상 같이 해주어야 한다.
    # 좌표값을 벗어나는 범위라면 continue( 다음 방향을 봐라 )
    if ny < 0 or ny >= 3 or nx < 0 or nx >= 3:
        continue
    #print("좌표 : ", ny, nx)
    #print("값 : ", arr[ny][nx])
    answer += arr[ny][nx]

# print("정답 : ", answer)
print(answer)