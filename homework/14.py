def solution(n, k, cmd):
    answer = ''
    pointer = k
    answer_arr = ['O'] * n
    last = n-1
    first = 0
    deleted = []
    for i in cmd:
        if i == 'C':
            answer_arr[pointer] = 'X'
            deleted.append(pointer)
            if pointer == last : 
                pointer-=1
                last = next(i for i in range(len(answer_arr)-1, -1, -1) if answer_arr[i] == 'O')
            else : 
                pointer+=1
        elif i == 'Z':
            rollback = deleted.pop()
            answer_arr[rollback] = 'O'
            last = next(i for i in range(len(answer_arr)-1, -1, -1) if answer_arr[i] == 'O')
        else : 
            dir = i.split()[0]
            amt = int(i.split()[1])
            if dir == 'D': 
                pointer += amt
                start = pointer-amt+1
                end = pointer+1
                for j in range(start, end):
                    if answer_arr[j] == 'X': pointer+=1
            else : 
                pointer -= amt
                start = pointer+1
                end = pointer+amt+1
                for j in range(start, end):
                    if answer_arr[j] == 'X': pointer-=1
    answer = ''.join(answer_arr)
        
    return answer


array = solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])
print(array)