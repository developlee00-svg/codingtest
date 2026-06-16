# from itertools import product
# from itertools import combinations_with_replacement
# from itertools import permutations

# n, m = list(map(int,input().split()))
# if m == 1:
#     arr = list(product([1,2,3,4,5,6], repeat=n))
# elif m == 2:
#     arr = list(combinations_with_replacement([1,2,3,4,5,6], n))
# elif m == 3:
#     arr = list(permutations([1,2,3,4,5,6], n))

# for row in arr:
#     for i in row:
#         print(i, end='')
#     print()

# 나올 수 있는 모든 조합
def func1(cnt):
    if cnt == N: # 모든 주사위를 던졌음 (==depth)
        print(*path)
        return
    
    for num in range(1, 7): # 한 번의 선택에서 나올 수 있는 경우의 수 (==branch)
        path.append(num)
        func1(cnt + 1) 
        path.pop() # 마지막 경우의 수 제거

# 2. 중복되는 조합 없애기
# - 1 1 2와 1 2 1은 같은 것이라 보고 제거함
def func2(cnt, prev):
    if cnt == N:
        print(*path)
        return
    
    # 이전 선택부터 고려
    for num in range(prev, 7): 
        path.append(num)
        func2(cnt + 1, num) # 지금 선택을 다음으로 함께 전달
        path.pop()

# 3.  숫자 중복 없애기 (한 번이라도 해당 숫자가 선택된 적이 있으면 고르지 말기)
# --> 선택된 숫자를 따로 관리 (visited 배열)
def func3(cnt):
    if cnt == N:
        print(*path)
        return
    
    for num in range(1, 7): 
        # 만약 num이 이전에 선택된 적이 있다면 continue
        # 왜 for num in path 안 쓰고 visited를 쓸까?
        # -> "in"을 쓰면 전체 리스트를 한 번 통째로 탐색한다 - O(N). -> 성능이 저하된다.
        if visited[num]: # O(1) : index 접근 1번만에 체크 완료
            continue
        visited[num] = 1 # 등장 체크
        path.append(num)
        func3(cnt + 1)
        path.pop()
        visited[num] = 0 # pop 했으니 등장 취소

# N : 주사위 수 / M : 메뉴
N, M= map(int, input().split())
path = list()
visited = [0] * 7 # 1~6번 주사위 숫자 등장 여부
if M == 1:
    func1(0)
elif M == 2:
    func2(0, 1)
elif M == 3:
    func3(0)