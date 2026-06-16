import sys

n,t= map(int, input().split())

arr = {i: [] for i in range(1, n+1)}

for i in range(t):
    From, At = map(int, input().split())
    arr[From].append(At)

#print(arr)

for i in range(1,n+1) : 
    if len(arr[i]) ==0 :continue
    print(i, ":", end = ' ')
    for j in arr[i]:
        print(j, end = ' ')
    print()