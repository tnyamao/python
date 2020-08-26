def search(data, target):
    start, end = 0, len(data)
    print("開始: ",start, "終了: ",end)
    while start <= end:
        i = (start + end) // 2
        print("start: ", start, "end: ",end, "data[i] :", data[i])
        if data[i] == target:
            return i
        elif data[i] < target:
            start = i + 1
        else:
            end = i - 1
    return -1

data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
target = 10
print("要素番号{}にデータ{}を見つけました。".format(search(data, target), target))
