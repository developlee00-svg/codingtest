# 1. 기본 재귀 호출 함수
# - [에러 발생] maximum recursion depth exceeded
#   - 약 1000번의 재귀호출 깊이가 가능하다.
def func(cnt):
    print(f'{cnt}번 호출')
    func(cnt + 1)

# 2. 기본 응용
# 문제: 1~10까지 순서대로 출력해라. 재귀호출로 구현해보세요.
# - [재귀호출 팁1] 시작점과 종료지점을 분석하고 구현하자.
#   - 문제예시
#     - 시작점: 숫자 1
#     - 종료점: 숫자 10
#     -> 누적값: 숫자(1~10), 숫자가 10이 되면 종료
def func2(num):
    if num > 10:  # 종료점(숫자가 10초과)이면 재귀호출 종료
        return

    print(num)
    
    # 1번 방법: 현재 시점의 num 값을 수정하지 않는다.
    func2(num + 1)

    # 2번 방법: 현재 시점의 num 값을 수정해버린다. --> 권장 X
    # num += 1
    # func2(num)

# 3. 기본 응용2
# - 특정 시점까지 들어갔다가, 되돌아오면서 다시 출력
# - 1 2 3 3 2 1
def func3(num):
    if num > 3: 
        return

    print(num)
    func3(num + 1)
    print(num)

arr = input().split()
def func4(index):
    if index >= len(arr):
        return
    print(arr[index], end=' ')
    func4(index+1)
    if index == len(arr)-1:
        return
    print(arr[index], end=' ')

func4(0)