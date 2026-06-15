def solution(participant, completion):
    hash_dict = {}
    temp = 0
    
    # 1. 모든 참가자의 이름을 해시값으로 변환하여 딕셔너리에 저장하고, 해시값들의 총합을 구함
    for p in participant:
        hash_dict[hash(p)] = p
        temp += hash(p)
    
    # 2. 완주자들의 해시값을 총합에서 뺌
    for c in completion:
        temp -= hash(c)
    
    # 3. 마지막에 남은 해시값(temp)이 완주하지 못한 선수의 해시값임
    return hash_dict[temp]
        

solution(["leo", "kiki", "eden"], ["eden", "kiki"])