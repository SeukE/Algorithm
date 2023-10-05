n,m = map(int,input().split())
numbers = sorted(list(map(int,input().split())))

def backTrack(array):
    if len(array) >= m:
        print(*array)
        return
    for i in numbers:
        if not i in array:
            array.append(i)
            backTrack(array)
            array.pop()

backTrack([])