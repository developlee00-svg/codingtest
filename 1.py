def solution(arr : list) -> list:
  # 리스트를 오름차순으로 정렬하는 함수
  arr.sort()
  
  # 리스트를 내림차순으로 정렬하는 함수
  # arr.sort(reverse = True)
  
  return arr
  

# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
print(solution([1,-5,2,4,3])) #반환값 : [-5, 1, 2, 3, 4]
print(solution([2,1,1,3,2,5,4])) # 반환값 : [1, 1, 2, 2, 3, 4, 5]
print(solution([1,6,7])) # 반환값 : [1, 6, 7]