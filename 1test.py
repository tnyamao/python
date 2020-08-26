def search(data, target):
    print(len(data))
    for i in range(len(data)):
        print("添え字: ",i)
        print("検査値: ",target)
        if data[i] == target:
            return i
    return -1

data = [1,2,3,4,5,6,7,8,9]
target = 7
print("要素番号{}にデータ{}を見つけました。".format(search(data, target), target))
