# 대각선까지 고려하는 델타배열
# 12시 방향부터 시계방향
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

first_bomb_y,  first_bomb_x = map(int, input().split())
second_bomb_y,  second_bomb_x = map(int, input().split())
# test_ground = [
#     ['_'] * 5,
#     ['_'] * 5,
#     ['_'] * 5,
#     ['_'] * 5,
# ]
test_ground = [['_']*5 for _ in range(4)]
for dir in range(8):
    y1 = first_bomb_y + dy[dir]
    x1 = first_bomb_x + dx[dir]


    if y1 < 0 or y1 >= 4 or x1 < 0 or x1 >= 5:
        continue
    test_ground[y1][x1] = '#'

for dir in range(8):
    y2 = second_bomb_y + dy[dir]
    x2 = second_bomb_x + dx[dir]

    if y2 < 0 or y2 >= 4 or  x2 < 0 or x2 >= 5:
        continue
    test_ground[y2][x2] = '#'

for i in range(4):
    for j in range(5):
        print(test_ground[i][j], end=' ')
    print()

for row in test_ground:
    print(*row)