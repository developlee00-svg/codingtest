message = "my phone number is 01012345678 and may i have your phone number"
spoiler_ranges = [[5, 5], [25, 28], [34, 40], [53, 59]]

# 1 & 2. flag 리스트 생성 및 범위 할당
flag = [False] * len(message)
for start, end in spoiler_ranges:
    for i in range(start, end + 1):
        if i < len(message):
            flag[i] = True

# 3. candidates와 others 분리
words = message.split()
candidates = []
others = []
current_idx = 0

for word in words:
    start_pos = message.find(word, current_idx)
    end_pos = start_pos + len(word) - 1
    if any(flag[i] for i in range(start_pos, end_pos + 1)):
        candidates.append(word)
    else:
        others.append(word)
    current_idx = end_pos + 1

# 4 & 5. candidates를 역순으로 순회하며 조건 미달 시 즉시 삭제
important = []

# range(시작, 끝, 증감단위)를 이용해 뒤에서부터 인덱스로 접근
for i in range(len(candidates) - 1, -1, -1):
    cand = candidates[i]
    
    # 조건: (1) others에 없고 (2) candidates 내에서 유일함
    if cand not in others and candidates.count(cand) == 1:
        # important에 중복 없이 추가 (뒤에서부터 검사하므로 순서 유지를 위해 insert 사용 가능)
        if cand not in important:
            important.append(cand)
    else:
        # 조건에 맞지 않으면 candidates 리스트에서 즉시 삭제
        del candidates[i]

# 최종 결과 출력
print(len(important))