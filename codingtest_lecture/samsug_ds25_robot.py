# TODO Later : 일단 정답코드임, 나중에 풀어봐야 함.

import sys
from collections import deque

input = sys.stdin.readline

n, k, l = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

site = []
for _ in range(k):
    y, x = map(int, input().split())
    site.append([y - 1, x - 1])

# 이동용: 위, 왼쪽, 오른쪽, 아래
dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

# 청소 방향 우선순위: 오른쪽, 아래쪽, 왼쪽, 위쪽
direct = [
    [(-1, 0), (0, 0), (0, 1), (1, 0)],   # 오른쪽 방향
    [(0, -1), (0, 0), (0, 1), (1, 0)],   # 아래쪽 방향
    [(-1, 0), (0, -1), (0, 0), (1, 0)],  # 왼쪽 방향
    [(-1, 0), (0, -1), (0, 0), (0, 1)]   # 위쪽 방향
]


def move_robot(idx):
    occupied = set()

    for i in range(k):
        if i == idx:
            continue
        occupied.add((site[i][0], site[i][1]))

    sy, sx = site[idx]

    visited = [[0] * n for _ in range(n)]
    q = deque()
    q.append((sy, sx))
    visited[sy][sx] = 1

    while q:
        level = []

        for _ in range(len(q)):
            y, x = q.popleft()
            level.append((y, x))

        candidates = []

        for y, x in level:
            if arr[y][x] > 0:
                candidates.append((y, x))

        if candidates:
            target_y, target_x = min(candidates)
            site[idx][0] = target_y
            site[idx][1] = target_x
            return

        for y, x in level:
            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]

                if ny < 0 or nx < 0 or ny >= n or nx >= n:
                    continue
                if visited[ny][nx] == 1:
                    continue
                if arr[ny][nx] == -1:
                    continue
                if (ny, nx) in occupied:
                    continue

                visited[ny][nx] = 1
                q.append((ny, nx))


def clean_robot(idx):
    y, x = site[idx]

    best_dir = 0
    best_amount = -1

    for d in range(4):
        amount = 0

        for i in range(4):
            ny = y + direct[d][i][0]
            nx = x + direct[d][i][1]

            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue
            if arr[ny][nx] == -1:
                continue

            amount += min(arr[ny][nx], 20)

        if amount > best_amount:
            best_amount = amount
            best_dir = d

    for i in range(4):
        ny = y + direct[best_dir][i][0]
        nx = x + direct[best_dir][i][1]

        if ny < 0 or nx < 0 or ny >= n or nx >= n:
            continue
        if arr[ny][nx] == -1:
            continue

        arr[ny][nx] -= min(arr[ny][nx], 20)


for _ in range(l):
    # 1. 이동
    for i in range(k):
        move_robot(i)

    # 2. 청소
    for i in range(k):
        clean_robot(i)

    # 3. 먼지 축적
    for y in range(n):
        for x in range(n):
            if arr[y][x] > 0:
                arr[y][x] += 5

    # 4. 먼지 확산
    old = [row[:] for row in arr]

    for y in range(n):
        for x in range(n):
            if old[y][x] == 0:
                total = 0

                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]

                    if ny < 0 or nx < 0 or ny >= n or nx >= n:
                        continue
                    if old[ny][nx] == -1:
                        continue

                    total += old[ny][nx]

                arr[y][x] = total // 10

    # 5. 출력
    result = 0

    for y in range(n):
        for x in range(n):
            if arr[y][x] == -1:
                continue
            result += arr[y][x]

    print(result)