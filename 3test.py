# バブルソート
def sort(data):
    for i in  range(len(data)-1, 0, -1):
        for j in range(i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

data = [1, 3, 2, 6, 4, 5, 1]
print("Befor. : ", data)
sort(data)
print("After. : ", data)
