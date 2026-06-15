def solution(s):
    while s :
        for i in range(len(s) - 1) :
            if s[i] == s[i+1]:
                s = s[:i] + s[i+2:]
                break
        else: return 0
    else: return 1

solution('cdcd')