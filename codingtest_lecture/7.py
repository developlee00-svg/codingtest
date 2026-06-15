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
def func2(cnt):
    pass

# 3.  숫자 중복 없애기 (한 번이라도 해당 숫자가 선택된 적이 있으면 고르지 말기)
def func3(cnt):
    pass


# N : 주사위 수 / M : 메뉴
N, M= map(int, input().split())
path = list()

if M == 1:
    func1(0)
elif M == 2:
    func2(0)
elif M == 3:
    func3(0)