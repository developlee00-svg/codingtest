# def func(cnt):
#     global answer, count
#     if cnt == x:
#         if answer <= 10:
#             count += 1
#         return
#     for i in range(1, 7):
#         answer += i
#         func(cnt + 1)
#         answer -= i

# x = int(input())
# answer = 0
# count = 0
# func(0)
# print(count)

# N 개의 주사위를 던진다.
# - 모든 경우의 수를 본다
# - [차이점] 합을 계산해야 한다.

# 시작점: 0개의 주사위
# 종료점: N개의 주사위
# 계산조건: 합이 10이하
# - 누적값: cnt / 주사위 눈금 합

# total: 현재까지의 주사위 눈금의 합
def func(cnt, total):
    global answer
    
    if cnt == N:
        if total <= 10:
            answer += 1
        return
    
    for num in range(1, 7):
        # 현재 선택된 숫자값을 total 에 더해주면서 다음 재귀호출로 진행
        func(cnt + 1, total + num)

N = int(input())
answer = 0
func(0, 0)
print(answer)