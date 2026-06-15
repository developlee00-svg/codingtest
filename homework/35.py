def solution(n, words):
    answers = list()
    answers.append(words[0])
    for i in range(1, len(words)):
        now_turn=i%n + 1
        turns = i//n + 1
        if words[i][0:1] != words[i-1][-1:]:
            return [now_turn, turns]
        elif words[i] in answers:
            return [now_turn, turns]
        else:
            answers.append(words[i])
    else : return [0,0]

# tmp1 = solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])
tmp2 = solution(2, ["hello", "one", "even", "never", "now", "world", "draw"])
print(tmp2)