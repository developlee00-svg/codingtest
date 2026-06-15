# from itertools import product
# x = int(input())
# arr = list(product([1,2,3,4,5,6], repeat=x))
# for row in arr:
#     print(*row)

# depth : 주사위의 개수
# barnch : 1~6. 총 6가지 경우의 수
def func(cnt):
    if cnt == N: # 모든 주사위를 던졌음 (==depth)
        for num in path:
            print(num, end='')
        print()
        return
    
    for num in range(1, 7): # 한 번의 선택에서 나올 수 있는 경우의 수 (==branch)
        path.append(num)
        func(cnt + 1) 
        path.pop() # 마지막 경우의 수 제거

N = int(input())
path = list()
func(0)