def solution(numbers : list) -> list :
    # 2중 for문으로 더하기 위해 리스트를 두개로 쪼갬
    numbers1 = numbers
    numbers2 = numbers

    # 숫자 더해서 저장할 list
    add_numbers = list()

    # 숫자 더해서 list에 저장
    for num1 in numbers1:
        for num2 in numbers2:
            add_numbers.append(num1 + num2)

    # 중복 제거      
    #add_numbers = list(set(add_numbers)).sort() # 왜 안되는지 모르겠음
    add_numbers = list(set(add_numbers))
    add_numbers.sort()  
    return add_numbers


res = solution([1,2,3])
print(res)

