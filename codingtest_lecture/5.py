arr = [3, 7, 4, 1, 9, 4, 6, 2]
num = int(input())
def func(index):
    if index < 0:
        return
    print(arr[index], end=' ')
    func(index-1)
    if index == 0:
        return
    print(arr[index], end=' ')

func(num)