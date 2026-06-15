'''
1. 연산자를 가지고 만들 수 있는 조합을 만든다.
-> 
1-1. 연산자의 개수가 n-1이 되면 숫자에 대입해서 계산하고 min, max 계산 -> 이건 global로 관리
1-2. list에 append하는 식으로 재귀호출, 재귀 전에 append, 재귀 후에 pop. 중복 허용 조합.
	-> operator['+', '-', '*'] 구성하고 remains[1, 1, 0] 구성함. for ops in operator: path.append() 하고 remains는 앞에서부터 차감
							if ops == "+" and remains[0] > 0:
								func(cnt+1, result + num)
							if ops == "-" and remains[1] > 0:
								func(cnt+1, result - num)
							if ops == "*" and remains[2] > 0:
								func(cnt+1, result * num)
2. 이걸 싹 계산해서 max, min 도출
'''

def func(cnt, result):
    global maxValue, minValue
    if cnt == N:
        maxValue = max(maxValue, result)
        minValue = min(minValue, result)
        return
    
    #     for ops in operators:
    #       if ops == "+" and  여기가 필요 없나?
    for ops in operators:
        if ops == "+" and remains[0] > 0:
            remains[0] -= 1
            func(cnt+1, result + nums[cnt])
            remains[0] += 1
        elif ops == "-" and remains[1] > 0:
            remains[1] -= 1
            func(cnt+1, result - nums[cnt])
            remains[1] += 1
        elif ops == "*" and remains[2] > 0:
            remains[2] -= 1
            func(cnt+1, result * nums[cnt])
            remains[2] += 1


N = int(input())
nums = list(map(int, input().split()))
operators = ['+', '-', '*']
remains = list(map(int, input().split()))
maxValue = -1000000000
minValue = 1000000000
func(1, nums[0])
print(minValue, maxValue)