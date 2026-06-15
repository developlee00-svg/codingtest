N = int(input())
# [정의] 전체 필드
field = [input().split() for _ in range(N)]
field = [[int(x) for x in row] for row in field]
# [정의] 몇초 걸리는지 저장할 변수
answer = 0
# [정의] 남아있는 폭탄 추적
destroyed = [False for _ in range(N*N+1)]
# [정의] 남아있는 폭탄 개수
remaining = N*N

# [정의] 델타 배열
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]
ny = 0
nx = 0
# 1부터 N*N까지
for a in range(1, N*N+1):
    loc = a
    if destroyed[loc] == True:
        continue
    # 좌표 찾고 그 자리 부수기
    for i in range(N):
        for j in range(N):
            if field[i][j] == loc:
                ny = i
                nx = j
                destroyed[field[ny][nx]] = True
                remaining -= 1
                # 마지막으로 터진 폭탄 번호 반환
                answer = field[ny][nx]
    # 좌표 주변 구역 부수기
    for dir in range(4):
        y = ny + dy[dir]
        x = nx + dx[dir]
        if y < 0 or y >= N or x < 0 or x >= N:
            continue
        # 이미 부숴진 맵이면 다시 부수지 않기
        if destroyed[field[y][x]] == True:
            continue
        destroyed[field[y][x]] = True
        remaining -= 1
    # for row in field:
    #     print(*row)
    # print()

    # 맵이 다 부숴졌으면 종료
    if remaining == 0:
        break

print(f'{answer}초')
