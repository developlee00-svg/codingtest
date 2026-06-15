class Bomb:
    def __init__(self, y, x):
        self.y = y
        self.x = x
        self.is_bombed = False

# 본인 + 상하좌우 순서
dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, -1, 1]

# 1초부터 N*N 초를 보면서
# 폭탄을 하나 씩 터뜨린다.
# - 중간에 다 터지면 즉시 종료
# ---> 함수로 빼주면 좋다.
def solution():
    cnt = 0  # 터진 폭탄 수

    for b_num in range(1, N * N + 1):
        bomb = bombs[b_num]

        # 현재 폭탄이 이미 터졌다면 다음 폭탄을 고려
        if bomb.is_bombed:
            continue

        # 본인 + 상하좌우를 보면서 터뜨리자.
        for dir in range(5):
            ny = bomb.y + dy[dir]
            nx = bomb.x + dx[dir]

            # 범위 밖 체크
            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue
                
            # 범위 안이라면 폭탄을 터뜨린다.
            target_num = game_map[ny][nx]
            target_bomb = bombs[target_num]

            # 해당 폭탄이 이미 터졌다면 pass
            if target_bomb.is_bombed:
                continue
        
            target_bomb.is_bombed = True
            cnt += 1

            # 모든 폭탄이 터졌다면 return
            if cnt == N * N:
                return b_num

N = int(input())
game_map = []  # 전체 맵
bombs = [None] * (N*N+1) # 전체 폭탄 관리 리스트

for y in range(N):
    row = list(map(int, input().split()))
    game_map.append(row)

    for x in range(N):
        bomb_num = row[x]
        bombs[bomb_num] = Bomb(y, x)

result = solution()
print(f'{result}초')