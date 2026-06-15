def solution(n, k, cmd):
    results = ['O'] * n
    deletes = [] # (이전행, 현재행, 다음행)의 튜플 리스트임
    # n = 처음 표의 행 개수
    # k = 현재 위치
    table = {i: [i - 1, i + 1] for i in range(n)} # {현재행: [이전행, 다음행]}
    
    table[0][0] = None
    table[n - 1][1] = None
    
    for index, command in enumerate(cmd) :
        if len(command) >= 2 : 
            direction, count = command.split()
            count = int(count)
            if direction == 'U' :
                for _ in range(count) :
                    k = table[k][0] # 이전행으로 한칸 이동
            else :
                for _ in range(count) :
                    k = table[k][1] # 다음행으로 한칸 이동
        else :
            if command == 'C' :
                prev, next = table[k] # 이전행/다음행
                
                deletes.append((prev, k, next)) # deletes에 삭제 데이터 넣기
                results[k] = 'X' # result에 반영
                
                if prev is not None: # 삭제한 후 이전행이 처음이 아니라면 
                    table[prev][1] = next # 이전행의 다음은 현재행이 아니라 다음행임
                if next is not None: # 삭제한 후 다음행이 마지막이 아니라면 
                    table[next][0] = prev # 다음행의 이전은 현재행이 아니라 이전행임
                
                if next is not None : # 삭제한 행의 다음이 존재한다면
                    k = next # 현재행을 다음행으로 변경
                else : # 삭제한 행이 끝에 있다면
                    k = prev  # 현재행을 이전행으로 변경
                
            else : #Z
                prev, restored, next = deletes.pop() #deletes에서 꺼내오기
                results[restored] = 'O' # 복구한 행의 result 상태 변경
                
                if prev is not None: # 이전 행이 처음이 아닌경우 
                    table[prev][1] = restored # 이전행의 다음행은 다음행이 아니라 현재행
                if next is not None: # 다음 행이 마지막 아닌경우
                    table[next][0] = restored # 다음행의 이전행은 이전행이 아니라 현재행
        
    return "".join(results)



array = solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])
print(array )