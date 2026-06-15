def solution(s):
    answer = 0
    queue = []
    for c in s:
        queue.append(c)
    
    for i in range(len(s)) :
        tmp = queue.pop(0)
        queue.append(tmp)
        print(queue)
        checked = check(queue)
        if checked == True :
            answer += 1
    return answer

def check(queue) :
    count = 0
    stack = []
    if queue[0] == ')' or queue[0] == '}' or queue[0] == ']':
        return False
    
    for mem in queue:
        if mem == ')' :
            if len(stack)!= 0 and stack.pop() == '(':
                count -= 1
            else:
                return False
        elif mem == '}':
            if len(stack)!= 0 and stack.pop() == '{':
                count -= 1
            else:
                return False
        elif mem == ']':
            if len(stack)!= 0 and stack.pop() == '[':
                count -= 1
            else:
                return False
        else :
            stack.append(mem)
            count += 1
        if count < 0:
            return False
    return count == 0




print(solution("}]()[{"))